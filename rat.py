from pgzero.actor import Actor
import random
import pygame

class Rat:
    def __init__(self):
        self.rat_x = [570, 70, 510, 90, 450, 150, 390, 210, 300]
        self.rat_y = [35, 35, 85, 85, 135, 135, 185, 185, 235]

        r_xy = random.randint(0, 8)
        self.current_index = r_xy

        self.actor = Actor('rat-idle-0', (self.rat_x[r_xy], self.rat_y[r_xy]))


        self.idle_frames = []
        for i in range(3):
            surf = pygame.image.load(f"images/rat-idle-{i}.png").convert_alpha()
            surf = pygame.transform.scale(surf, (64, 64))
            self.idle_frames.append(surf)

        self.current_frame = 0
        self.frame_timer = 0
        self.frame_speed = 10

        self.actor._surf = self.idle_frames[self.current_frame]

    def respawn(self):
        old_index = self.current_index
        self.current_index = random.randint(0, 8)
        while self.current_index == old_index:
            self.current_index = random.randint(0, 8)

        self.actor.x = self.rat_x[self.current_index]
        self.actor.y = self.rat_y[self.current_index]

        self.current_frame = 0
        self.frame_timer = 0
        self.actor._surf = self.idle_frames[self.current_frame]

    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= self.frame_speed:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
            self.actor._surf = self.idle_frames[self.current_frame]
