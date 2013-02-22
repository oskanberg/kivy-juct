
from kivy.graphics.texture  import Texture
import random

class TextureFactory(object):
    
    def __init__(self, **kw):
        super(TextureFactory, self).__init__(**kw)
        self.texture_dictionary = {}


    def get_field_texture(self):
        if 'field' in self.texture_dictionary:
            return self.texture_dictionary['field']

        print 'generating field texture'
        texture = Texture.create(size=(128, 128), colorfmt='rgb')
        size = 128 * 128 * 3
        image_buffer = []
        for i in xrange(size):
            image_buffer.append(random.randint(0, 75))
            image_buffer.append(random.randint(50, 200))
            image_buffer.append(random.randint(0, 75))
        
        image_buffer = ''.join(map(chr, image_buffer))
        texture.wrap = 'repeat'
        texture.blit_buffer(image_buffer, colorfmt='rgb', bufferfmt='ubyte')
        self.texture_dictionary['field'] = texture
        return texture

    def get_tree_texture(self):
        if 'tree' in self.texture_dictionary:
            return self.texture_dictionary['tree']

        print 'generating tree texture'
        texture = Texture.create(size=(128, 128), colorfmt='rgb')
        size = 128 * 128 * 3
        img_data = []
        for pixel in xrange(size):
            img_data.append({
                'r' : 50,
                'g' : random.randint(75, 100),
                'b' : 0
            })
        img_buffer = []
        for pixel in img_data:
            if random.randint(0, 10) > 9: 
                pixel['r'] = 100
                pixel['g'] = 25
                pixel['b'] = 0
            img_buffer.append(pixel['r'])
            img_buffer.append(pixel['g'])
            img_buffer.append(pixel['b'])
        
        img_buffer = ''.join(map(chr, img_buffer))
        texture.wrap = 'repeat'
        texture.blit_buffer(img_buffer, colorfmt='rgb', bufferfmt='ubyte')
        self.texture_dictionary['tree'] = texture
        return texture
    
    def get_thing_texture(self):
        if 'thing' in self.texture_dictionary:
            return self.texture_dictionary['thing']

        print 'generating tree texture'
        texture = Texture.create(size=(128, 128), colorfmt='rgb')
        size = 128 * 128 * 3
        img_data = []
        for pixel in xrange(size):
            img_data.append({
                'r' : 20,
                'g' : 20,
                'b' : 20
            })
        img_buffer = []
        for pixel in img_data:
            img_buffer.append(pixel['r'])
            img_buffer.append(pixel['g'])
            img_buffer.append(pixel['b'])
        
        img_buffer = ''.join(map(chr, img_buffer))
        texture.wrap = 'repeat'
        texture.blit_buffer(img_buffer, colorfmt='rgb', bufferfmt='ubyte')
        self.texture_dictionary['thing'] = texture
        return texture

