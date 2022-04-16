""" Sprite Sample Program """

import arcade

# --- Constants ---

MOVEMENT_SPEED = 7

ROW_COUNT = 15
COLUMN_COUNT = 15

WIDTH = 1050
HEIGHT = 1050

MARGIN = 5

LIVES = 3

LEVEL_1_X = 400
LEVEL_1_Y = 250


class Player(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y


class MenuView(arcade.View):

    def __init__(self):
        super().__init__()

    def on_show(self):

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

    def on_draw(self):
        self.window.clear()
        arcade.draw_rectangle_filled(center_x=500, center_y=500, width=250, height=250,color=arcade.color.DARK_SLATE_BLUE)
        arcade.set_background_color(arcade.color.BLUEBERRY)
        arcade.draw_text("Menu Screen", WIDTH / 2, HEIGHT / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press enter to start", WIDTH / 2, HEIGHT / 2 - 75, arcade.color.WHITE, font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)


class GameView(arcade.View):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        self.movement_block = None
        self.wall = None
        self.test = None
        self.goal = None

        self.movement_block_list = None
        self.wall_list = None
        self.test_list = None
        self.death_list = None
        self.goal_list = None

        self.movement = False
        self.collision_with_wall = False
        self.physics_engine = None
        self.key_pressed = False
        self.lives = None

    def setup(self):

        self.lives = LIVES
        self.movement_block_list = arcade.SpriteList()
        self.movement_block = Player("tile_0024.png", scale=3)

        self.movement_block.center_x = LEVEL_1_X
        self.movement_block.center_y = LEVEL_1_Y
        self.movement_block_list.append(self.movement_block)

        self.death_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.test_list = arcade.SpriteList()
        self.goal_list = arcade.SpriteList()
        self.movement = False

        wall_points = [(800, 250), (750, 800), (150, 740), (204, 500)]

        for x, y in wall_points:
            self.test = arcade.Sprite("iceBlock.png")
            self.test.center_x = x
            self.test.center_y = y
            self.test_list.append(self.test)

        for x, y in wall_points:
            self.wall = arcade.Sprite("tile_0018.png", scale=.9)
            self.wall.center_x = x
            self.wall.center_y = y
            self.wall_list.append(self.wall)

        self.goal = arcade.Sprite("tile_0024.png")
        self.goal.center_x = 900
        self.goal.center_y = 558
        self.goal_list.append(self.goal)

        for x in range(0, 1080, 54):
            death = arcade.Sprite("iceBlock.png", scale=1)
            death.center_x = x
            death.center_y = 1023
            self.death_list.append(death)

        for x in range(0, 1080, 54):
            death = arcade.Sprite("iceBlock.png", scale=1)
            death.center_x = x
            death.center_y = 50
            self.death_list.append(death)

        for y in range(0, 1080, 54):
            death = arcade.Sprite("iceBlock.png", scale=1)
            death.center_x = 27
            death.center_y = y
            self.death_list.append(death)

        for y in range(0, 1080, 54):
            death = arcade.Sprite("iceBlock.png", scale=1)
            death.center_x = 1023
            death.center_y = y
            self.death_list.append(death)

        self.physics_engine = arcade.PhysicsEngineSimple(self.movement_block, self.wall_list)

    def on_show(self):

        arcade.set_background_color(arcade.color.BLUEBERRY)

    def on_draw(self):

        arcade.start_render()

        self.movement_block_list.draw()
        self.wall_list.draw()
        self.test_list.draw()
        self.death_list.draw()
        output = f"lives:{self.lives}"
        arcade.draw_text(output, 50, 50, arcade.color.BLACK, 12,)
        self.goal_list.draw()

    def on_update(self, delta_time):

        self.movement_block_list.update()

        self.wall_list.update()

        self.physics_engine.update()

        test_hit_list = arcade.check_for_collision_with_list(self.movement_block, self.test_list)
        death_hit = arcade.check_for_collision_with_list(self.movement_block, self.death_list)
        goal_hit = arcade.check_for_collision_with_list(self.movement_block, self.goal_list)

        if death_hit:
            self.movement_block.center_y = 250
            self.movement_block.center_x = 400
            self.movement_block.change_x = 0
            self.movement_block.change_y = 0
            self.key_pressed = False
            self.collision_with_wall = True
            self.lives -= 1

        if test_hit_list:
            if not self.collision_with_wall:
                self.collision_with_wall = True
                #self.movement = False
                self.key_pressed = False
                self.movement_block.change_y = 0
                self.movement_block.change_x = 0
                print(MOVEMENT_SPEED)

        if goal_hit:
            print("win!")
            game_view = Level2()
            game_view.setup()
            self.window.show_view(game_view)

        if self.lives == 0:
            print("game over")
            game_view = Level2()
            game_view.setup()
            self.window.show_view(game_view)

        #print(self.movement_block.center_x, self.movement_block.center_y)
    def on_key_press(self, key, modifiers):

        if not self.key_pressed:

            if key == arcade.key.UP:
                self.movement_block.change_y = MOVEMENT_SPEED
                self.key_pressed = True
            elif key == arcade.key.DOWN:
                self.movement_block.change_y = - MOVEMENT_SPEED
                self.key_pressed = True
            elif key == arcade.key.RIGHT:
                self.movement_block.change_x = MOVEMENT_SPEED
                self.key_pressed = True
            elif key == arcade.key.LEFT:
                self.movement_block.change_x = - MOVEMENT_SPEED
                self.key_pressed = True
            elif key == arcade.key.R:
                self.movement_block.center_x = LEVEL_1_X
                self.movement_block.center_y = LEVEL_1_Y

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            #self.movement = True
            self.collision_with_wall = False
        elif key == arcade.key.DOWN:
            #self.movement = True
            self.collision_with_wall = False
        elif key == arcade.key.LEFT:
            #self.movement = True
            self.collision_with_wall = False
        elif key == arcade.key.RIGHT:
            #self.movement = True
            self.collision_with_wall = False


class Level2(arcade.View):

    def __init__(self):
        super().__init__()

        self.goal_list = None
        self.reset_list = None
        self.tile_map = None

    def setup(self):
        self.goal_list = arcade.SpriteList()
        self.reset_list = arcade.SpriteList()


    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

    def on_draw(self):
        self.window.clear()
        arcade.draw_rectangle_filled(center_x=500, center_y=500, width=250, height=250,color=arcade.color.DARK_SLATE_BLUE)
        arcade.set_background_color(arcade.color.BLUEBERRY)
        arcade.draw_text("Menu Screen", WIDTH / 2, HEIGHT / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press enter to start", WIDTH / 2, HEIGHT / 2 - 75, arcade.color.WHITE, font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

    def setup(self):

        self.window.clear()

def main():
    """ Main method """
    window = arcade.Window(WIDTH, HEIGHT, "HEy")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()