from ...Node import Node


# Material Animation
class MaterialAnimation(Node):
    fields = [
        ('next', 'MaterialAnimation'),
        ('animation', 'Animation'),
        ('texture_animation', 'TextureAnimation'),
        ('render_animation', 'RenderAnimation'),
    ]
