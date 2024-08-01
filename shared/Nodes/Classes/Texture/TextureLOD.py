from ...Node import Node


# Texture LOD
class TextureLOD(Node):
    fields = [
        ('min_filter', 'uint'),
        ('LOD_bias', 'float'),
        ('bias_clamp', 'uchar'),
        ('enable_edge_LOD', 'uchar'),
        ('max_anisotropy', 'uint'),
    ]
