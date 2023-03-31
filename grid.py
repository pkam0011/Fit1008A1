from __future__ import annotations
from data_structures.referential_array import ArrayR
from layer_store import SetLayerStore, AdditiveLayerStore, SequenceLayerStore
import random

class Grid:
    DRAW_STYLE_SET = "SET"
    DRAW_STYLE_ADD = "ADD"
    DRAW_STYLE_SEQUENCE = "SEQUENCE"
    DRAW_STYLE_OPTIONS = (
        DRAW_STYLE_SET,
        DRAW_STYLE_ADD,
        DRAW_STYLE_SEQUENCE
    )

    DEFAULT_BRUSH_SIZE = 2
    MAX_BRUSH = 5
    MIN_BRUSH = 0

   
    def __init__(self, draw_style, x, y) -> None:
        """
        Initialise the grid object.
        - draw_style:
            The style with which colours will be drawn.
            Should be one of DRAW_STYLE_OPTIONS
            This draw style determines the LayerStore used on each grid square.
        - x, y: The dimensions of the grid.

        Should also intialise the brush size to the DEFAULT provided as a class variable.
        """
        # Check that draw_style is valid
        if draw_style not in self.DRAW_STYLE_OPTIONS:
            raise ValueError(f"Invalid draw style '{draw_style}'. Must be one of {self.DRAW_STYLE_OPTIONS}") #produces eroor message if invalid input provided

        # Set instance variables
        self.draw_style = draw_style
        self.x = x
        self.y = y
        self.brush_size = self.DEFAULT_BRUSH_SIZE
        # raise NotImplementedError()


        self.grid = ArrayR(x)

        for i in range(x):
            self.grid[i] = ArrayR(y)
            for j in range(y):
                if draw_style == self.DRAW_STYLE_SET:
                    self.grid[i][j] = SetLayerStore()
                elif draw_style == self.DRAW_STYLE_ADD:
                    self.grid[i][j] = AdditiveLayerStore()
                elif draw_style == self.DRAW_STYLE_SEQUENCE:
                    self.grid[i][j] = SequenceLayerStore()



    def increase_brush_size(self):
        """
        Increases the size of the brush by 1,
        if the brush size is already MAX_BRUSH,
        then do nothing.
        """
        if self.brush_size < self.MAX_BRUSH:
            self.brush_size += 1
        # raise NotImplementedError() #comment out

    def decrease_brush_size(self):
        """
        Decreases the size of the brush by 1,
        if the brush size is already MIN_BRUSH,
        then do nothing.
        """
        if self.brush_size > self.MIN_BRUSH:
            self.brush_size -= 1
        #raise NotImplementedError()

    def special(self):
        #inverts the colour of each pixel
        """
        Activate the special affect on all grid squares.
        """
        for i in range(self.x):
            for j in range(self.y):
                layer = self.grid[i][j].get_layer(self.draw_style)
                layer.set_color(random.choice(self.colors))
        # raise NotImplementedError()

