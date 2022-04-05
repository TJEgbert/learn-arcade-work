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
SCREEN_HEIGHT = 800

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
        self.wall_list = None

        self.movement = False
        self.collision_with_wall = False
        self.physics_engine = None

    def setup(self):

        self.movement_block_list = arcade.SpriteList()
        self.movement_block = Player("tile_0024.png", scale=3)

        self.movement_block.center_x = 500
        self.movement_block.center_y = 500
        self.movement_block_list.append(self.movement_block)

        self.wall_list = arcade.SpriteList()
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

        self.physics_engine = arcade.PhysicsEngineSimple(self.movement_block, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.movement_block_list.draw()

        self.wall_list.draw()

    def on_update(self, delta_time):

        self.movement_block_list.update()

        self.wall_list.update()

        self.physics_engine.update()

        wall_hit = arcade.check_for_collision_with_list(self.movement_block, self.wall_list)
        if wall_hit:
            print("hi")

    def on_key_press(self, key, modifiers):

        if not self.movement:

            if key == arcade.key.UP:
                self.movement_block.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.movement_block.change_y = - MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.movement_block.change_x = MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.movement_block.change_x = - MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.movement = True
        elif key == arcade.key.DOWN:
            self.movement = True
        elif key == arcade.key.LEFT:
            self.movement = True
        elif key == arcade.key.RIGHT:
            self.movement = True


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()