from pygame import Rect

class PlatformManager:
    def __init__(self):
        self.floor = Rect ((0, 380), (600, 20))
        self.platform1 = Rect((270, 300),(60, 5))
        self.platform2 = Rect((180, 250),(60, 5))
        self.platform3 = Rect((360, 250),(60, 5))
        self.platform4 = Rect((120, 200),(60, 5))
        self.platform5 = Rect((420, 200),(60, 5))
        self.platform6 = Rect((60, 150),(60, 5))
        self.plat61_x = 40
        self.plat62_x = 490
        self.platform61 = Rect((self.plat61_x, 150),(60, 5))
        self.platform62 = Rect((self.plat62_x, 150),(60, 5))
        self.platform7 = Rect((480, 150),(60, 5))
        self.platform8 = Rect((0, 100),(60, 5))
        self.platform9 = Rect((540, 100),(60, 5))
        self.platforms = [self.floor, self.platform1, self.platform2, self.platform3, self.platform4, self.platform5,
                          self.platform6, self.platform7, self.platform8, self.platform9, self.platform61, self.platform62]
        self.plat61_left = True
        self.plat62_left = False
