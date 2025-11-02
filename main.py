from game import Game

WIDTH = 600
HEIGHT = 400

game = None #placeholder

def init():
    global game
    if game is None:
        game = Game(screen, keyboard, music, sounds)

def draw():
    init()
    game.draw()

def update():
    init()
    game.update()

def on_mouse_down(pos):
    init()
    game.on_mouse_down(pos)
