
import random

from Player import Player
from confing import *
from Object import Object


pg.init()

screen = pg.display.set_mode((confing['w'], confing['h']))
pg.display.set_caption(confing['title'])
clock = pg.time.Clock()

all_sprite = pg.sprite.Group()
object_group=pg.sprite.Group()
player = Player()

def new_mobs():
    object_bottom = Object(confing['w'],random.randint(-100 , 100))
    object_top = Object(confing['w'],random.randint(500,confing['h']))
    object_group.add(object_top,object_bottom)
    all_sprite.add(object_group)

SPAWN_SPRITE = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_SPRITE,1500)

pg.time.set_timer(pg.USEREVENT,50)



object = Object(600, 500)
all_sprite.add(object)

all_sprite.add(player)
run = True
while run:
    clock.tick(confing['fps'])
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == SPAWN_SPRITE:
            new_mobs()

    all_sprite.update()
    screen.fill('white')
    all_sprite.draw(screen)
    pg.display.flip()

    if pg.sprite.spritecollide(player,object_group,False,pg.sprite.collide_circle):
        run=False

pg.init
