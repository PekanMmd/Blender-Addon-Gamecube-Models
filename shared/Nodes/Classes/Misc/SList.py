from ...Node import Node


# S List
class SList(Node):
    fields = [
        ('next', 'SList'),
        ('data', 'uint'),  # TODO: confirm what kind of data this points to
    ]
