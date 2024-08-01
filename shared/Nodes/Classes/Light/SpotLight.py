from ...Node import Node


# Spot Light
class SpotLight(Node):
    fields = [
        ('cutoff', 'float'),
        ('spot_flags', 'uint'),
        ('reference_br', 'float'),
        ('reference_distance', 'float'),
        ('distance_attn_flags', 'uint'),
    ]
