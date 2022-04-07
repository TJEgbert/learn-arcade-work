""" Sprite Sample Program """

import arcade

# --- Constants ---

MOVEMENT_SPEED = 5

ROW_COUNT = 15
COLUMN_COUNT = 15

WIDTH = 54
HEIGHT = 54

MARGIN = 5

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

class Player(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

class Block(arcade.Sprite):

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

        self.block = None

        self.movement_block_list = None
        self.wall_list = None
        self.test_list = None

        self.movement = False
        self.collision_with_wall = False
        self.physics_engine = None
        self.key_pressed = False

        self.left_pressed = False
        self.right_pressed = False
        self.down_pressed = False
        self.up_pressed = False

        self.block_list = None

    def setup(self):

        self.movement_block_list = arcade.SpriteList()
        self.movement_block = Player("tile_0024.png", scale=3)

        block = arcade.Sprite("platformPack_tile016.png", scale=1)
        block.center_x = 300
        block.center_y = 300
        block.boundary_left = 0
        block.boundary_top = 0

        self.movement_block.center_x = 400
        self.movement_block.center_y = 250
        self.movement_block_list.append(self.movement_block)

        self.block.center_x = 300
        self.block.center_y = 300
        self.block_list.append(self.block)


        self.wall_list = arcade.SpriteList()
        self.test_list = arcade.SpriteList()
        self.movement = False

        for x in range(0, 1080, 54):
            wall = arcade.Sprite("tile_0018.png", scale=3)
            wall.center_x = x
            wall.center_y = 800
            self.wall_list.append(wall)

        for x in range(0, 1080, 54):
            wall = arcade.Sprite("tile_0018.png", scale=3)
            wall.center_x = x
            wall.center_y = 30
            self.wall_list.append(wall)

        for y in range(0, 1080, 54):
            wall = arcade.Sprite("tile_0018.png", scale=3)
            wall.center_x = 50
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 1080, 54):
            wall = arcade.Sprite("tile_0018.png", scale=3)
            wall.center_x = 950
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 1080, 54):
            test = arcade.Sprite("platformPack_tile016.png", scale=1)
            test.center_x = 950
            test.center_y = y
            self.test_list.append(test)

        self.physics_engine = arcade.PhysicsEnginePlatformer(player_sprite=self.movement_block,
                                                             platforms=self.block_list,
                                                             walls=self.wall_list,
                                                             gravity_constant=0)

    def on_draw(self):
        arcade.start_render()
        self.movement_block_list.draw()

        self.wall_list.draw()

        self.test_list.draw()

        self.block_list.draw()

    def on_update(self, delta_time):

        self.movement_block_list.update()

        self.wall_list.update()

        self.physics_engine.update()

        test_hit_list = arcade.check_for_collision(self.movement_block, self.block)

        if test_hit_list:
            self.

    def update_player_speed(self):

        self.movement_block.change_x = 0
        self.movement_block.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.movement_block.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.movement_block.change_y = - MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.movement_block.change_x = MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.movement_block.change_x = - MOVEMENT_SPEED

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()