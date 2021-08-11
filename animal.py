import os
import random
import game_config as gc
from pygame import image , transform

animals_count = dict((a,0) for a in gc.ASSET_FILES)#intilaize all to 0

def available_animals():
    return[a for a,c in animals_count.items() if c<2 ]# to iterate over animal items and it give key as value and if <2 then it'll be elemnt and list will return


class Animal:
    def __init__(self , index):
        self.index = index# for 4 row and 4 coloum
        self.row = index // gc.NUM_TILES_SIDE  # 4 in this case row
        self.col = index % gc.NUM_TILES_SIDE # if row is 1 coloum is 0 and so on
        self.name = random.choice(available_animals())
        animals_count[self.name]+= 1

        self.image_path = os.path.join(gc.ASSET_DIR , self.name)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image , (gc.IMAGE_SIZE - 2*gc.MARGIN , gc.IMAGE_SIZE - 2*gc.MARGIN ))
        self.box = self.image.copy()
        self.box.fill((200,200,200))
        self.skip=False # if animals are matched then skip printing
