from kivy.uix.widget        import Widget
from kivy.vector            import Vector
from kivy.graphics          import Rectangle, Ellipse
import random

class AObj(object):
    
    def __init__(self, texture_factory, size, position, **kw):
        super(AObj, self).__init__(**kw)
        self._size = size
        self._position = Vector(*position)
        self._texture_factory = texture_factory
    
    def check_bounds(self, min_x, min_y, max_x, max_y):
        #print 'size: x:%d y:%d' % (self._size[0], self._size[1])
        #print ' min x: %d\n min y: %d\n max x: %d\n max y: %d\n x: %d\n y: %d' % (min_x, min_y, max_x, max_y, self._position[0], self._position[1])
        if self._position[0] > max_x or self._position[1] > max_y:
            return False
        elif self._position[0] + self._size[0] > min_x and self._position[1] + self._size[1] > min_y :
            return True
        else:
            return False

    def update(self, *largs):
        pass

    def move_to_point(self, point, speed):
        distance = Vector(point).distance(self._position)
        movement_vector = point - self._position
        self._position += movement_vector / (1 + distance * 0.1)


class Field(AObj):
    
    def __init__(self, texture_factory, size, position, **kw):
        super(Field, self).__init__(texture_factory, size, position, **kw)
        self.texture = self._texture_factory.get_field_texture()
        
    def draw(self, canvas, offset_vector):
        updated_position = Vector(self._position) + offset_vector
        with canvas:
            r = Rectangle(pos=updated_position, size=self._size, texture=self.texture)
            r.tex_coords = [x * 32 for x in r.tex_coords] 


class Tree(AObj):
    
    def __init__(self, texture_factory, size, position, **kw):
        super(Tree, self).__init__(texture_factory, size, position, **kw)
        self.texture = self._texture_factory.get_tree_texture()
        
    def draw(self, canvas, offset_vector):
        updated_position = Vector(self._position) + offset_vector
        with canvas:
            r = Ellipse(pos=updated_position, size=self._size, texture=self.texture)
            r.tex_coords = [x * 0.2 for x in r.tex_coords]

    def update(self):
        #self._position += Vector(random.randint(-2, 2), random.randint(-2, 2))
        pass
