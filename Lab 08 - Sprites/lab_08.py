"""Lab 8 Trevor Egbert"""

import arcade
import random

# Global variables
CHARACTER_SPRITE_SIZE = 0.5
GOOD_SPRITE_SIZE = 0.7
BAD_SPRITE_SIZE = 0.4

DIAMOND_COUNT = 50
SAW_COUNT = 40

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Diamond class set up
class Diamond(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


# Saw class setup
class Saw(arcade.Sprite):

    def update(self):
        self.center_x += 1
        self.angle += 2

        if self.right > SCREEN_WIDTH:
            self.left = 0

        if self.angle > 359:
            self.angle -= 360


class MyGame(arcade.Window):
    """Set up game """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        # set up sprite lists
        self.player_list = None
        self.diamond_list = None
        self.saw_list = None

        # score
        self.player_sprite = None
        self.player_score = 0

        self.set_mouse_visible(False)

        self.diamond_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.saw_sound = arcade.load_sound(":resources:sounds/lose5.wav")

        arcade.set_background_color(arcade.color.CYBER_GRAPE)

    def setup(self):

        # sprite list
        self.player_list = arcade.SpriteList()
        self.diamond_list = arcade.SpriteList()
        self.saw_list = arcade.SpriteList()

        self.score = 0

        # player set up
        self.player_sprite = arcade.Sprite("platformChar_happy.png", CHARACTER_SPRITE_SIZE)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Creates diamond sprites
        for i in range(DIAMOND_COUNT):

            diamond = Diamond("platformPack_item007.png", GOOD_SPRITE_SIZE)

            diamond.center_x = random.randrange(SCREEN_WIDTH)
            diamond.center_y = random.randrange(SCREEN_HEIGHT)
            diamond.change_x = random.randrange(-2, 2)
            diamond.change_y = random.randrange(-2, 2)

            self.diamond_list.append(diamond)

        # Creates saw sprites
        for i in range(SAW_COUNT):
            saw = Saw("platformPack_tile023.png", BAD_SPRITE_SIZE)

            saw.center_x = random.randrange(SCREEN_WIDTH)
            saw.center_y = random.randrange(SCREEN_HEIGHT)

            self.saw_list.append(saw)

    def on_draw(self):

        # draw everything
        arcade.start_render()
        self.diamond_list.draw()
        self.player_sprite.draw()
        self.saw_list.draw()

        output = f"Score: {self.player_score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 15)
        if len(self.diamond_list) == 0:
            arcade.draw_text("Game Over!", 200, 300, arcade.color.BLACK, 50, SCREEN_WIDTH)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Character movement with mouse"""

        if len(self.diamond_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):

        # Checks if there's any diamonds in the list if so it moves them if not freezes everything
        if len(self.diamond_list) > 0:
            self.diamond_list.update()
            self.saw_list.update()

        # Check collisions with the player against the sprite list
        diamond_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.diamond_list)
        saw_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.saw_list)

        # adds one to points when player collides
        for diamond in diamond_hit_list:
            diamond.remove_from_sprite_lists()
            self.player_score += 1
            arcade.play_sound(self.diamond_sound)

        # minus a point when collides
        for saw in saw_hit_list:
            saw.remove_from_sprite_lists()
            self.player_score -= 1
            arcade.play_sound(self.saw_sound)


def main():

    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()