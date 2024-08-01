from ...Node import Node


# Shape Animation
class ShapeAnimation(Node):
    fields = [
        ('next', 'ShapeAnimation'),
        ('animation', 'Animation'),
    ]
