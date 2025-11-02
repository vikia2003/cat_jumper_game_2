import random
from pygame import Rect
from pgzero.clock import clock
from player import Player
from rat import Rat
from jellyfish import Jellyfish
from platform_manager import PlatformManager

class Game:
    def __init__(self, screen_obj, keyboard_obj, music_obj, sounds_obj):
        self.screen = screen_obj
        self.keyboard = keyboard_obj
        self.music = music_obj
        self.sounds = sounds_obj

        self.WIDTH = 600
        self.HEIGHT = 400
        self.blue = 150
        self.blueforward = True
        self.ground_color = (0, 0, 139)

        self.player = Player()
        self.rat = Rat()
        self.jellyfish = Jellyfish()
        self.platforms = PlatformManager()

        self.points = 0
        self.menu_active = True
        self.music_on = True
        self.game_over_state = False
        self.win_state = False

        self.start_button = Rect((250, 150), (100, 40))
        self.music_button = Rect((250, 200), (100, 40))
        self.exit_button = Rect((250, 250), (100, 40))
        self.play_again_button = Rect((200, 250), (100, 40))
        self.exit_button_go = Rect((320, 250), (100, 40))

        self.music.play('cat_music')
        self.music.set_volume(0.5)

    def win_screen(self):
        self.screen.fill((0, 0, 0))
        self.screen.draw.text("YOU WIN!", center=(self.WIDTH//2, self.HEIGHT//2 - 50), fontsize=60, color="yellow", shadow=(2,2))
        self.screen.draw.text("Play Again", center=self.play_again_button.center, fontsize=30)
        self.screen.draw.text("Exit", center=self.exit_button_go.center, fontsize=30)
        self.game_over_state = True

    def draw(self):
        if self.menu_active:
            self.screen.fill((50, 50, 50))
            self.screen.draw.text(
            "Eat the rats, beware of the fish! Score 5 points to win :)", center=(self.WIDTH // 2, 50), fontsize=25, color="white"
            )
            music_text = "Music On" if self.music_on else "Music Off"
            self.screen.draw.text("Start", center=self.start_button.center, fontsize=30)
            self.screen.draw.text(music_text, center=self.music_button.center, fontsize=20)
            self.screen.draw.text("Exit", center=self.exit_button.center, fontsize=30)

        elif self.game_over_state:
            self.screen.fill((0, 0, 0))
            self.screen.draw.text("GAME OVER", center=(self.WIDTH//2, self.HEIGHT//2 - 50), fontsize=60, color="red", shadow=(2,2))
            self.screen.draw.text("Play Again", center=self.play_again_button.center, fontsize=30)
            self.screen.draw.text("Exit", center=self.exit_button_go.center, fontsize=30)

        elif self.win_state:
            self.screen.fill((0, 100, 0))
            self.screen.draw.text("YOU WIN!", center=(self.WIDTH//2, self.HEIGHT//2 - 50), fontsize=60, color="yellow", shadow=(2,2))
            self.screen.draw.text("Play Again", center=self.play_again_button.center, fontsize=30)
            self.screen.draw.text("Exit", center=self.exit_button_go.center, fontsize=30)

        else:
            self.screen_game()

    def screen_game(self):
        p = self.player.actor
        self.screen.fill((173, 216, self.blue))
        self.screen.blit('skyline_600_400', (0, 0))
        self.platforms.platform61 = Rect((self.platforms.plat61_x, 100),(60, 5))
        self.platforms.platform62 = Rect((self.platforms.plat62_x, 100),(60, 5))
        self.platforms.platforms[10] = self.platforms.platform61
        self.platforms.platforms[11] = self.platforms.platform62

        for i in self.platforms.platforms:
            self.screen.draw.filled_rect(i, self.ground_color)

        p.draw()
        self.rat.actor.draw()
        self.jellyfish.actor.draw()
        self.screen.draw.text("Score:", center=(35, 30), fontsize=30, shadow=(1,1), color=(255, 255, 255))
        self.screen.draw.text(str(self.points), center=(80, 31), fontsize=30, shadow=(1,1), color=(255, 255, 255))

    def update(self):
        if self.game_over_state or self.win_state:
            return
        if not self.menu_active and not self.game_over_state:
            #win condition:
            if self.points >= 5:
                self.win_screen()
                return
            self.backgroundcolorfade()
            self.platform_mover()
            self.cat_move()
            self.rat.update()
            self.jellyfish.update()

            self.move_fish()
            if self.points >= 5:
                self.win_state = True

    def cat_move(self):
        p = self.player
        cat = p.actor

    #update collision rect to follow actor
        p.collision_rect.center = cat.pos

        moving_left = self.keyboard.left and p.allow_x
        moving_right = self.keyboard.right and p.allow_x

    #gravity & vertical movement
        if self.collide_check():
            p.gravity = 1
            cat.y -= 1
            p.allow_x = True
            p.timer = []
            p.jumping = False
        else:
            cat.y += p.gravity
            if p.gravity <= 20:
                p.gravity += 0.2
            p.timer.append(1)
            if len(p.timer) > 5 and not p.jumped:
                p.allow_x = False

    #horizontal movement
        if moving_left and cat.x > 40 and p.x_velocity > -8:
            p.x_velocity -= 2
        if moving_right and cat.x < 560 and p.x_velocity < 8:
            p.x_velocity += 2

        cat.x += p.x_velocity

    #friction
        if p.x_velocity > 0:
            p.x_velocity -= 1.7
            if p.x_velocity < 0: p.x_velocity = 0
        elif p.x_velocity < 0:
            p.x_velocity += 1
            if p.x_velocity > 0: p.x_velocity = 0

        if cat.x < 50 or cat.x > 550:
            p.x_velocity = 0

    #jump
        if self.keyboard.up and self.collide_check() and not p.jumped:
            self.sounds.meow.play()
            p.jumping = True
            p.jumped = True
            clock.schedule_unique(self.jumped_recently, 0.4)
            p.y_velocity = 95

        if p.jumping and p.y_velocity > 25:
            p.y_velocity -= (100 - p.y_velocity) / 2
            cat.y -= p.y_velocity / 3
        else:
            p.y_velocity = 0
            p.jumping = False

    #collect rats
        if cat.colliderect(self.rat.actor):
            self.points += 1
            self.sounds.gem.play()
            self.rat.respawn()

    #select correct animation
        if p.jumping:
            if moving_right:
                p.current_animation = p.jump_right_frames
            elif moving_left:
                p.current_animation = p.jump_left_frames
            else:
                p.current_animation = p.jump_right_frames
        elif moving_right:
            p.current_animation = p.run_right_frames
        elif moving_left:
            p.current_animation = p.run_left_frames
        else:
            p.current_animation = p.idle_frames

    #update frame
        p.frame_timer += 1
        if p.frame_timer >= p.frame_speed:
            p.frame_timer = 0
            p.current_frame = (p.current_frame + 1) % len(p.current_animation)
            cat.image = p.current_animation[p.current_frame]

    def move_fish(self):
    #use the player's collision_rect, not the Actor
        if self.player.collision_rect.colliderect(self.jellyfish.collision_rect):
            self.sounds.plop.play()
            self.points = max(0, self.points - 1)
            self.jellyfish.respawn()
            if self.points <= 0:
                self.game_over_state = True

    def platform_mover(self):
        plat = self.platforms
        cat = self.player.actor

        if plat.plat61_left:
            plat.plat61_x += 2
            if plat.plat61_x == 280:
                plat.plat61_left = False
            if cat.colliderect(plat.platform61):
                cat.x += 2   
        else:
            plat.plat61_x -= 2
            if plat.plat61_x == 40:
                plat.plat61_left = True
            if cat.colliderect(plat.platform61):
                cat.x -= 2     

        if plat.plat62_left:
            plat.plat62_x += 2
            if plat.plat62_x == 490:
                plat.plat62_left = False
            if cat.colliderect(plat.platform62):
                cat.x += 2 
        else:
            plat.plat62_x -= 2
            if plat.plat62_x == 250:
                plat.plat62_left = True
            if cat.colliderect(plat.platform62):
                cat.x -= 2 

    def collide_check(self):
        cat_rect = self.player.collision_rect
        for plat in self.platforms.platforms:
            if cat_rect.colliderect(plat):
                return True
        return False

    def jumped_recently(self):
        self.player.jumped = False

    def backgroundcolorfade(self):
        if self.blue < 255 and self.blueforward:
            self.blue += 1
        else:
            self.blueforward = False
        if self.blue > 130 and not self.blueforward:
            self.blue -= 1
        else:
            self.blueforward = True

    def on_mouse_down(self, pos):
        if self.menu_active:
            if self.start_button.collidepoint(pos):
                self.menu_active = False
            elif self.music_button.collidepoint(pos):
                self.music_on = not self.music_on
                if self.music_on:
                    self.music.play('cat_music')
                else:
                    self.music.stop()
            elif self.exit_button.collidepoint(pos):
                exit()
        elif self.game_over_state:
            if self.play_again_button.collidepoint(pos):
                self.reset_game()
            elif self.exit_button_go.collidepoint(pos):
                exit()
        elif self.win_state:
            if self.play_again_button.collidepoint(pos):
                self.reset_game()
            elif self.exit_button_go.collidepoint(pos):
                exit()

    def reset_game(self):
        self.win_state = False
        self.points = 0
        self.player.actor.x = 300
        self.player.actor.y = 175
        self.rat.respawn()
        self.jellyfish.respawn()
        self.game_over_state = False
