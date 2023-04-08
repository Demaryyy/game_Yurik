import os
import pygame as pg

confing = {
    'w': 600,
    'h': 600,
    'title': 'Yurik нуб а ты труп',
    'bg': " white",
    'fps': 60}

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, 'media')

player_img = pg.image.load(os.path.join(media_folder, '1647182674_4-abrakadabra-fun-p-el-primo-bez-fona-6.png'))

object_img = pg.image.load(os.path.join(media_folder, 'GFFF.png'))
