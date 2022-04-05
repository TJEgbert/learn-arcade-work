""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class Player(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.movement_block = None
        self.movement_block_list = None

        self.movement = False

    def setup(self):

        self.movement_block_list = arcade.SpriteList()
        self.movement_block = Player("tile_0024.png", scale=3)

        self.movement_block.center_x = 30
        self.movement_block.center_y = 30
        self.movement_block_list.append(self.movement_block)

    def on_draw(self):
        arcade.start_render()
        self.movement_block_list.draw()

    def on_update(self, delta_time):

        self.movement_block_list.update()

    def on_key_press(self, key, modifiers):

        movement = False
        while not movement:
            if key == arcade.key.UP:
                self.movement_block.change_y = MOVEMENT_SPEED
                movement = True
            elif key == arcade.key.DOWN:
                self.movement_block.change_y = - MOVEMENT_SPEED
                movement = True
            elif key == arcade.key.RIGHT:
                self.movement_block.change_x = MOVEMENT_SPEED
                movement = True
            elif key == arcade.key.LEFT:
                self.movement_block.change_x = - MOVEMENT_SPEED
                movement = True

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()