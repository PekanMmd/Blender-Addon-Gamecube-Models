from ...Node import Node


# Shape Animation Mesh
class ShapeAnimationMesh(Node):
    fields = [
        ('next', 'ShapeAnimationMesh'),
        ('animation', 'ShapeAnimation'),
    ]
