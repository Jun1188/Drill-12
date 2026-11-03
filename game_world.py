#객체로 구성된 게임월드
from pico2d import *
from boy import Boy
from grass import Grass

world = [[], [], []] # layers for game objects, 이중 리스트 [깊이], [객체]

def add_object(o, depth=1): 
    if depth == 2:
        o.y += 10
    world[depth].append(o)

def add_objects(ol, depth=1):
    
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return #계산을 줄이기 위함

    raise Exception("Object not found")


#게임 로직
def update():
    for layer in world:
        for o in layer:
            o.update()

#게임 렌더링
def render():
    for layer in world:
        for o in layer:
            o.draw()






