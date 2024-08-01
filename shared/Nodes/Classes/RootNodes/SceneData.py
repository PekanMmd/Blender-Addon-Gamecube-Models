from ...Node import Node


# Scene Data
class SceneData(Node):
    fields = [
        ('models', 'ModelSet[]'),
        ('camera', 'CameraSet'),
        ('lights', 'LightSet[]'),
        ('fog', 'Fog')
    ]
