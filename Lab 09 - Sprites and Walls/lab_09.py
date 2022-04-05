"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 9"

GEM_COUNT = 50
# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 50

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.gem_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.score = None

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        # Load sounds
        self.gem_sound = arcade.load_sound(":resources:sounds/coin2.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("platformChar_walk1.png",
                                           scale=0.5)
        self.player_sprite.center_x = 60
        self.player_sprite.center_y = 60
        self.player_list.append(self.player_sprite)

        self.score = 0

        """Outer walls"""
        # Bottom wall
        for x in range(0, 1000, 32):
            wall = arcade.Sprite("platformPack_tile004.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        # Top wall
        for x in range(0, 1000, 31):
            wall = arcade.Sprite("platformPack_tile004.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1000
            self.wall_list.append(wall)

        # Left wall
        for y in range(0, 1000, 32):
            wall = arcade.Sprite("platformPack_tile004.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        # Right wall
        for y in range(0, 1000, 32):
            wall = arcade.Sprite("platformPack_tile004.png", SPRITE_SCALING)
            wall.center_x = 1000
            wall.center_y = y
            self.wall_list.append(wall)

        """Row one walls"""
        # Part 1
        for x in range(75, 450, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)

        # Part 2
        for x in range(550, 925, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)

        """Row two walls"""
        # Part 1
        for x in range(75, 250, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)

        # Part 2
        for x in range(325, 925, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)

        """Row three walls"""
        # Part 1
        for x in range(75, 600, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)

        # Part 2
        for x in range(675, 900, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)

        """Row four walls"""
        # Part 1
        for x in range(75, 400, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 400
            self.wall_list.append(wall)

        # Part 2
        for x in range(475, 925, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 400
            self.wall_list.append(wall)

        """Row five wall"""
        for x in range(75, 850, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)

        """Row six wall"""
        # Part 1
        for x in range(75, 325, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 600
            self.wall_list.append(wall)

        # Part 2
        for x in range(650, 925, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 600
            self.wall_list.append(wall)

        """Row seven walls"""
        # Part 1
        for x in range(75, 325, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 700
            self.wall_list.append(wall)

        # Part 2
        for x in range(650, 925, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 700
            self.wall_list.append(wall)

        """Row eight walls"""
        # Part 1
        for x in range(75, 650, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 800
            self.wall_list.append(wall)

        # Part 2
        for x in range(700, 925, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 800
            self.wall_list.append(wall)

        """Row Nine walls"""
        # Part 1
        for x in range(75, 450, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 900
            self.wall_list.append(wall)

        # Part 2
        for x in range(525, 925, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 900
            self.wall_list.append(wall)

        """Column one walls"""
        # Part 1
        for y in range(100, 410, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = 75
            wall.center_y = y
            self.wall_list.append(wall)

        # Part 2
        for y in range(500, 900, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = 75
            wall.center_y = y
            self.wall_list.append(wall)

        """Column two Wall"""
        for y in range(100, 800, 32):
            wall = arcade.Sprite("platformPack_tile016.png", SPRITE_SCALING)
            wall.center_x = 925
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.BLUE)

        for i in range(GEM_COUNT):

            gem = arcade.Sprite("platformPack_item010.png", 1)

            gem_placed_successfully = False

            while not gem_placed_successfully:
                gem.center_x = random.randrange(0, 1000)
                gem.center_y = random.randrange(0, 1000)
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)

                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:

                    gem_placed_successfully = True

            self.gem_list.append(gem)

    def on_draw(self):
        """ Render the screen. """
        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.gem_list.draw()

        # Select the (unscrolled) camera for our GUI

        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Score: {self.score}"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        self.gem_list.update()

        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)

        for gem in gem_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.gem_sound)

        self.physics_engine.update()

        self.scroll_to_player()

    def scroll_to_player(self):

        position = Vec2(self.player_sprite.center_x - self.width / 2,

                        self.player_sprite.center_y - self.height / 2)

        self.camera_sprites.move_to(position, CAMERA_SPEED)


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()