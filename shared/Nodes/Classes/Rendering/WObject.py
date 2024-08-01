from ...Node import Node


# W Object
class WObject(Node):
    fields = [
        ('name', 'string'),
        ('position', 'vec3'),
        ('render', 'Render'),
    ]
