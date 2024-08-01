from ...Node import Node


# Light Animation
class LightAnimation(Node):
    fields = [
        ('next', 'LightAnimation'),
        ('animation', 'Animation'),
        ('eye_position_animation', 'WObjectAnimation'),
        ('interest_animation', 'WObjectAnimation'),
    ]
