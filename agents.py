from kivy.uix.widget        import Widget
from kivy.vector            import Vector
from kivy.graphics          import Rectangle, Ellipse
import random
import nonagents


class Thing(nonagents.AObj):
    
    def __init__(self, texture_factory, size, position, **kw):
        super(Thing, self).__init__(texture_factory, size, position, **kw)
        self.texture = self._texture_factory.get_thing_texture()
        self.target = self._position
        
    def draw(self, canvas, offset_vector):
        updated_position = Vector(self._position) + offset_vector
        with canvas:
            r = Ellipse(pos=updated_position, size=self._size, texture=self.texture)
            r.tex_coords = [x * 0.2 for x in r.tex_coords]

    def move_to_touch(self, touch, offset_vector):
        self.target = Vector(touch.x, touch.y) + offset_vector

    def update(self):
        self.move_to_point(self.target, 5)
