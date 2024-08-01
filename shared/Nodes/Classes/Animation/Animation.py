from ...Node import Node


# Animation
class Animation(Node):
    fields = [
        ('flags', 'uint'),
        ('end_frame', 'float'),
        ('frame', 'Frame'),
        ('joint', 'Joint'),
    ]
