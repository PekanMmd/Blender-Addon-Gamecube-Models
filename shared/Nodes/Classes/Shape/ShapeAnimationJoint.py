from ...Node import Node


# Shape Animation Joint
class ShapeAnimationJoint(Node):
    fields = [
        ('child', 'ShapeAnimationJoint'),
        ('next', 'ShapeAnimationJoint'),
        ('animation', 'ShapeAnimation'),
    ]
