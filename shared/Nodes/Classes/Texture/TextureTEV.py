from ...Node import Node

# Texture TEV
class TextureTEV(Node):
    class_name = "Texture TEV"
    fields = [
        ('color_op', 'uchar'),
        ('alpha_op', 'uchar'),
        ('color_bias', 'uchar'),
        ('alpha_bias', 'uchar'),
        ('color_scale', 'uchar'),
        ('alpha_scale', 'uchar'),
        ('color_clamp', 'uchar'),
        ('alpha_clamp', 'uchar'),
        ('color_a', 'uchar'),
        ('color_b', 'uchar'),
        ('color_c', 'uchar'),
        ('color_d', 'uchar'),
        ('alpha_a', 'uchar'),
        ('alpha_b', 'uchar'),
        ('alpha_c', 'uchar'),
        ('alpha_d', 'uchar'),
        ('konst', '@RGBX8Color'),
        ('tev0', '@RGBX8Color'),
        ('tev1', '@RGBX8Color'),
        ('active', 'uint'),
    ]

    def loadFromBinary(self, parser):
        super().loadFromBinary(parser)
        self.konst.transform()
        self.tev0.transform()
        self.tev1.transform()