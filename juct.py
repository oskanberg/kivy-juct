import kivy
from kivy.config            import Config
from kivy.vector            import Vector
from kivy.app               import App
from kivy.uix.widget        import Widget
from kivy.clock             import Clock
from kivy.properties        import NumericProperty, ReferenceListProperty, ListProperty

import random
import nonagents
import agents
import textures
kivy.require('1.5.1')

FPS = 30
UPS = 30
VP_H = 500
VP_W = 750
F_H = 2048
F_W = 2048


Config.set('graphics', 'height', VP_H)
Config.set('graphics', 'width',  VP_W)


class WhatSheSawThere(Widget):
    
    def __init__(self, **kw):
        super(WhatSheSawThere, self).__init__(**kw)
        field_size = (F_W, F_H)
        self.texture_factory = textures.TextureFactory()
        self.field = nonagents.Field(self.texture_factory, size=field_size, position=(0,0))
        self.thing = agents.Thing(self.texture_factory, size=(10, 10), position=(0,0))
        self.objects = []
        self.add_trees(100)
        
    def add_trees(self, n):
        for tree in xrange(n):
            self.objects.append(nonagents.Tree(self.texture_factory, size=(30, 30), position=(random.randint(0, F_W), random.randint(0, F_H))))
    
    def update(self, *largs):
        self.thing.update()
        for element in self.objects:
            element.update()
    
    def touched(self, touch, offset_vector):
        self.thing.move_to_touch(touch, offset_vector)


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
        if self.world.thing.check_bounds(min_x, min_y, max_x, max_y):
            self.world.thing.draw(self.canvas, -Vector(self.x, self.y))
        for element in self.world.objects:
            if element.check_bounds(min_x, min_y, max_x, max_y):
                element.draw(self.canvas, -Vector(self.x, self.y))
    
    def on_touch_down(self, touch):
        #touch.ud['origin'] = (touch.x, touch.y)
        self.world.touched(touch, -Vector(self.x, self.y))
        
    def on_touch_move(self, touch):
        self.world.touched(touch, -Vector(self.x, self.y))
        #offset_vector = Vector(touch.x, touch.y) - Vector(*touch.ud['origin'])
        #(self.x, self.y) = Vector(self.x, self.y) - offset_vector
        #print 'VP x: %d y: %d' % (self.x, self.y)
        #touch.ud['origin'] = (touch.x, touch.y)

class JuctApp(App):
    
    def build(self):
        world = WhatSheSawThere()
        view = LookingGlass(world, size=(VP_W, VP_H))
        Clock.schedule_interval(world.update, 1.0/UPS)
        Clock.schedule_interval(view.draw, 1.0/FPS)
        return view
 
 
if __name__ == '__main__':
    JuctApp().run()
