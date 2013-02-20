import kivy
from kivy.config            import Config
from kivy.vector            import Vector
from kivy.app               import App
from kivy.uix.widget        import Widget
from kivy.graphics          import Rectangle
from kivy.graphics.texture  import Texture
from kivy.clock             import Clock
from kivy.properties        import NumericProperty, ReferenceListProperty, ListProperty

kivy.require('1.5.1')

FPS = 30
VP_H = 500
VP_W = 750
F_H = 1000
F_W = 1000


Config.set('graphics', 'height', VP_H)
Config.set('graphics', 'width',  VP_W)

class AObj(object):
    
    def __init__(self, size, position, **kw):
        super(AObj, self).__init__(**kw)
        self._size = size
        self._position = Vector(*position)
    
    def check_bounds(self, min_x, min_y, max_x, max_y):
        #print 'size: x:%d y:%d' % (self._size[0], self._size[1])
        #print ' min x: %d\n min y: %d\n max x: %d\n max y: %d\n x: %d\n y: %d' % (min_x, min_y, max_x, max_y, self._position[0], self._position[1])
        if self._position[0] > max_x or self._position[1] > max_y:
            return False
        elif self._position[0] + self._size[0] > min_x and self._position[1] + self._size[1] > min_y :
            return True
        else:
            return False
        

class Field(AObj):
    
    def __init__(self, size, position, **kw):
        super(Field, self).__init__(size, position, **kw)
        self.texture = Texture.create(size=(3, 1), colorfmt='rgb')
        color1 = 0
        color2 = 255
        buf = ''.join(map(chr, [color1, color2]))
        self.texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        
    def draw(self, canvas, offset_vector):
        updated_position = Vector(self._position) + offset_vector
        with canvas:
            Rectangle(pos=updated_position, size=self._size, texture=self.texture)

class WhatSheSawThere(Widget):
    
    def __init__(self, **kw):
        super(WhatSheSawThere, self).__init__(**kw)
        field_size = (F_W, F_H)
        self.field = Field(size=field_size, position=(0,0))
        self.objects = ()
    
            
class LookingGlass(Widget):
    
    def __init__(self, wsst, size, **kw):
        super(LookingGlass, self).__init__(size=size, *kw)
        self.x = 0
        self.y = 0
        self.world = wsst
        
    def draw(self, *largs):
        self.canvas.clear()
        min_x = self.x
        min_y = self.y
        max_x = self.x + self.size[0]
        max_y = self.y + self.size[1]
        if self.world.field.check_bounds(min_x, min_y, max_x, max_y):
            self.world.field.draw(self.canvas, -Vector(self.x, self.y))
        for element in self.world.objects:
            if element.check_bounds(min_x, min_y, max_x, max_y):
                element.draw(self.canvas, -Vector(self.x, self.y))
    
    def on_touch_down(self, touch):
        touch.ud['origin'] = (touch.x, touch.y)
        
    def on_touch_move(self, touch):
        offset_vector = Vector(touch.x, touch.y) - Vector(*touch.ud['origin'])
        (self.x, self.y) = Vector(self.x, self.y) - offset_vector
        print 'VP x: %d y: %d' % (self.x, self.y)
        touch.ud['origin'] = (touch.x, touch.y)

class JuctApp(App):
    
    def build(self):
        world = WhatSheSawThere()
        view = LookingGlass(world, size=(VP_W, VP_H))
        Clock.schedule_interval(view.draw, 1.0/FPS)
        return view
 
 
if __name__ == '__main__':
    JuctApp().run()
