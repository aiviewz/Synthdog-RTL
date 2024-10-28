"""
Donut
Copyright (c) 2022-present NAVER Corp.
MIT License
"""
from collections import OrderedDict

import numpy as np
from synthtiger import components

from elements.textbox import TextBox
from layouts import GridStack

class TextReader:
    def __init__(self, path):
        self.fp = open(path, "r", encoding="utf-8")
        self.lines = self.fp.readlines()  # Read all lines at once
        self.length = len(self.lines)
        self.idx = 0  # Track the current line index

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.length:
            line = self.lines[self.idx].strip('\n')  # Return the current line without the newline character
            self.idx += 1  # Move to the next line
            return line
        else:
            self.idx=0
            line = self.lines[self.idx].strip('\n')
            self.idx += 1  # Move to the next line
            return line
    def reset(self):
        self.idx = 0  # Reset to the first line

class Content:
    def __init__(self, config):
        self.margin = config.get("margin", [0, 0.1])
        self.reader = TextReader(**config.get("text", {}))
        self.font = components.BaseFont(**config.get("font", {}))
        self.layout = GridStack(config.get("layout", {}))
        self.textbox = TextBox(config.get("textbox", {}))
        self.textbox_color = components.Switch(components.Gray(), **config.get("textbox_color", {}))
        self.content_color = components.Switch(components.Gray(), **config.get("content_color", {}))
        self.rtl = config.get("rtl", False)  # RTL flag

    def generate(self, size):
        width, height = size

        layout_left = width * np.random.uniform(self.margin[0], self.margin[1])
        layout_top = height * np.random.uniform(self.margin[0], self.margin[1])
        layout_width = max(width - layout_left * 2, 0)
        layout_height = max(height - layout_top * 2, 0)
        layout_bbox = [layout_left, layout_top, layout_width, layout_height]

        text_layers, texts = [], []
        layouts = self.layout.generate(layout_bbox)
        

        for layout in layouts:
            font = self.font.sample()

            for bbox, align in layout:
                x, y, w, h = bbox
                text = next(self.reader, None)
                if text is None:
                  break
                text_layer, label_text = self.textbox.generate((w, h), text, font)

                if text_layer is None:
                    continue

                text_layer.center = (x + w / 2, y + h / 2)
                
                if self.rtl:
                    text_layer.right = x + w
                elif align == "left":
                    text_layer.left = x
                elif align == "right":
                    text_layer.right = x + w

                self.textbox_color.apply([text_layer])
                text_layers.append(text_layer)
                texts.append(label_text)

        self.content_color.apply(text_layers)

        return text_layers, texts
