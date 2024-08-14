import bpy
import math

from ..Constants import *
from ..Errors import *
from ..Nodes import *

class ModelBuilder(object):

	def __init__(self, context, sections, options):
		# Settings chosen for the parser
		# - "ik_hack"   : A boolean for whether or not to scale down bones so ik works correctly
		# - "max_frame" : An integer for the maximum number of frames to read from an animation, 0 for no limit
		# - "verbose"   : Prints more output for debugging purposes
		self.options = options

		self.context = context
		self.sections = sections

		self.armature_count = 0
		self.bone_count = 0
		self.mesh_count = 0

		self.models = []
		self.lights = []
		self.cameras = []
		self.fogs = []

		# Images that have been loaded from their texture data
		self.images_cache_by_image_id_and_tlut_id = {}

		# Sometimes there are sets which are separated across multiple sections.
		# We can load multiple sections at the same time and bundle them into sets.
		disjoint_modelset = ModelSet.emptySet()
		disjoint_cameraset = CameraSet.emptySet()
		disjoint_lightset = LightSet.emptySet()

		for section in sections:
			if section.root_node is None:
				continue

			if isinstance(section.root_node, Joint):
				disjoint_modelset.root_joint = section.root_node

			elif isinstance(section.root_node, AnimationJoint):
				disjoint_modelset.animated_joints.append(section.root_node)

			elif isinstance(section.root_node, MaterialAnimationJoint):
				disjoint_modelset.animated_material_joints.append(section.root_node)

			elif isinstance(section.root_node, ShapeAnimationJoint):
				disjoint_modelset.animated_shape_joints.append(section.root_node)

			elif isinstance(section.root_node, Camera):
				disjoint_cameraset.camera = section.root_node

			elif isinstance(section.root_node, CameraAnimation):
				disjoint_cameraset.animations.append(section.root_node)

			elif isinstance(section.root_node, CameraSet):
				self.cameras.append(section.root_node)

			elif isinstance(section.root_node, Light):
				disjoint_lightset.light = section.root_node

			elif isinstance(section.root_node, LightAnimation):
				disjoint_lightset.animations.append(section.root_node)

			elif isinstance(section.root_node, LightSet):
				self.lights.append(section.root_node)

			elif isinstance(section.root_node, SceneData):
				scene_data = section.root_node

				if scene_data.camera is not None:
					self.cameras.append(scene_data.camera)

				if scene_data.fog is not None:
					self.fogs.append(scene_data.fog)

				if scene_data.lights is not None:
					self.lights += scene_data.lights

				if scene_data.models is not None:
					self.models += scene_data.models

		if disjoint_modelset.root_joint is not None:
			self.models.append(disjoint_modelset)

		if disjoint_cameraset.camera is not None:
			self.cameras.append(disjoint_cameraset)

		if disjoint_lightset.light is not None:
			self.lights.append(disjoint_lightset)

	def build(self):
		if self.options.get("verbose"):
			print("Building model")

		for model in self.models:
			self.importModel(model)

		for light in self.lights:
			self.importLight(light)

		for camera in self.cameras:
			self.importCamera(camera)

		for fog in self.fogs:
			self.importFog(fog)


	# TODO: complete implementation
	def importModel(self, model):
		if model is None:
			return
		model.prepareForBlender(self)
		armature = model.build(self)

	def importLight(self, light):
		light.prepareForBlender(self)
		light.build(self)

	def importCamera(self, camera):
		camera.prepareForBlender(self)
		camera.build(self)

	def importFog(self, fog):
		fog.prepareForBlender(self)
		fog.build(self)

	def cacheImage(self, image_id, tlut_id, image_data):
		self.images_cache_by_image_id_and_tlut_id[(image_id, tlut_id)] = image_data

	def getCachedImage(self, image_id, tlut_id):
		return self.images_cache_by_image_id_and_tlut_id.get((image_id, tlut_id))



