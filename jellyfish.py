from pgzero.actor import Actor
from pygame import Rect
import random

class Jellyfish:
    def __init__(self):
        self.positions = [
            (540, 340), (60, 340), (480, 290), (120, 290),
            (420, 240), (180, 240), (360, 190), (240, 190), (300, 140)
        ]

        #animation frames
        self.idle_frames = [f'jellyfish-idle-{i}' for i in range(11)]

        pos = random.choice(self.positions)
        self.actor = Actor(self.idle_frames[0], pos)

        self.collision_rect = Rect(0, 0, self.actor.width, self.actor.height)
        self.collision_rect.center = self.actor.pos

        self.current_frame = 0
        self.frame_timer = 0
        self.frame_speed = 10

    def respawn(self):
        old = self.actor.pos
        pos = random.choice([p for p in self.positions if p != old])
        self.actor.pos = pos
        self.current_frame = 0
        self.frame_timer = 0
        self.actor.image = self.idle_frames[0]

    def update(self):
        #animate jellyfish
        self.frame_timer += 1
        if self.frame_timer >= self.frame_speed:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
            self.actor.image = self.idle_frames[self.current_frame]

        #keep collision rect aligned (full size)
        self.collision_rect.center = self.actor.pos
