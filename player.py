from pgzero.actor import Actor
from pygame import Rect

class Player:
    def __init__(self):
        self.actor = Actor('cat-idle-0', (300, 175))
        #movement
        self.x_velocity = 0
        self.y_velocity = 0
        self.gravity = 1
        self.jumping = False
        self.jumped = False
        self.allow_x = True
        self.timer = []

        #make collision rectangle smaller and anchored to the feet
        self.collision_rect = Rect(0, 0, self.actor.width - 4, self.actor.height // 2)
        self.collision_rect.midbottom = self.actor.midbottom

        #animation frames
        self.idle_frames = [f'cat-idle-{i}' for i in range(4)]
        self.run_right_frames = [f'cat-run-right-{i}' for i in range(4)]
        self.run_left_frames = [f'cat-run-left-{i}' for i in range(4)]
        self.jump_right_frames = [f'cat-jump-right-{i}' for i in range(4)]
        self.jump_left_frames = [f'cat-jump-left-{i}' for i in range(4)]

        #animation state
        self.current_animation = self.idle_frames
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_speed = 5
