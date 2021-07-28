import pygame

# 視窗大小
WIN_width = 1024
WIN_height = 600
# 設定楨數
FPS = 60

class Image:    # 設定背景圖像
    def __init__(self):
        self.BG = pygame.image.load('images/Map.png')
        self.pause = pygame.image.load('images/pause.png')
        self.conti = pygame.image.load('images/continue.png')
        self.sound = pygame.image.load('images/sound.png')
        self.muse = pygame.image.load('images/muse.png')
        self.hp = pygame.image.load('images/hp.png')
        self.hpgray = pygame.image.load('images/hp_gray.png')
class Color:    # 設定顏色
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.purple = (147, 0, 147)
# 設定敵人路徑
path_enemy_1 = [(22, 308), (52, 283), (84, 283), (110, 305), (116, 341), (115, 375), (112, 405), (116, 433),
          (135, 455), (159, 475), (188, 480), (217, 481), (243, 474), (267, 463), (291, 454), (315, 441),
          (334, 423), (343, 398), (339, 368), (328, 345), (305, 331), (282, 322), (264, 303), (255, 283),
          (259, 259), (274, 239), (294, 225), (318, 214), (347, 212), (373, 217), (394, 230), (410, 250),
          (429, 266), (446, 282), (465, 295), (483, 310), (502, 321), (523, 309), (535, 282), (535, 254),
          (533, 230), (532, 190)]
path_enemy_2 = [(576, 595), (603, 531), (658, 489), (737, 501), (836, 496), (891, 454), (830, 394), (771, 348),
                (833, 262), (829, 201), (718, 213), (597, 289), (526, 297), (525, 218)]

