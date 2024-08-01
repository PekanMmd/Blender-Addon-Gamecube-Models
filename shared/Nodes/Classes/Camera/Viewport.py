from ...Node import Node


# Viewport
class Viewport(Node):
    fields = [
        ('ix', 'ushort'),
        ('iw', 'ushort'),
        ('iy', 'ushort'),
        ('ih', 'ushort'),
    ]
