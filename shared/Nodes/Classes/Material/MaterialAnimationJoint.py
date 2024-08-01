from ...Node import Node


# Material Animation Joint
class MaterialAnimationJoint(Node):
    fields = [
        ('child', 'MaterialAnimationJoint'),
        ('next', 'MaterialAnimationJoint'),
        ('animation', 'MaterialAnimation'),
    ]
