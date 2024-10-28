import numpy as np
from synthtiger import layers

class TextBox:
    def __init__(self, config):
        self.fill = config.get("fill", [1, 1])
        self.rtl = config.get("rtl", True)  # Add RTL option

    def generate(self, size, text, font):
        width, height = size

        line_layers = []
        fill = np.random.uniform(self.fill[0], self.fill[1])
        adjusted_width = np.clip(width * fill, height, width)  # Adjust width for fill
        font = {**font, "size": int(height)}
        left = adjusted_width if self.rtl else 0
        top = 0
        lines=[]
        
        for i,line in enumerate(text.split(" ")):
            if not line.strip():
                continue
            
            line_layer = layers.TextLayer(line, **font)
            line_scale = height / line_layer.height
            line_layer.bbox = [left, top, *(line_layer.size*line_scale)]
            
            left=left-line_layer.width
            line_layer = layers.TextLayer(line, **font)
            line_scale = height / line_layer.height
            line_layer.bbox = [left, top, *(line_layer.size*line_scale)]
            left = line_layer.left-2
     
            if left < 0:
                break
            line_layers.append(line_layer)
            lines.append(line)

        if len(line_layers) == 0:
            return None, None

        text_layer = layers.Group(line_layers).merge()
        return text_layer, " ".join(lines)