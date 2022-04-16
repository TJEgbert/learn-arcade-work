""" Sprite Sample Program """

import arcade

# --- Constants ---

MOVEMENT_SPEED = 20

WIDTH = 1050
HEIGHT = 1050

LIVES = 3

PLAYER_STARTING_X = 120
PLAYER_STARTING_Y = 120

class Player(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y


class MenuView(arcade.View):

    def __init__(self):
        super().__init__()

    def on_show(self):

        arcade.set_background_color(arcade.color.BLUEBERRY)

    def on_draw(self):
        self.window.clear()
        arcade.draw_text("Menu Screen", WIDTH / 2, HEIGHT / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press enter to start", WIDTH / 2, HEIGHT / 2 - 75, arcade.color.WHITE, font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)


class WinScreen(arcade.View):

    def __init__(self):
        super().__init__()

    def on_show(self):

        arcade.set_background_color(arcade.color.BLUEBERRY)

    def on_draw(self):
        self.window.clear()
        arcade.draw_text("You Win! Thanks for playing!", WIDTH / 2, HEIGHT / 2, arcade.color.WHITE, font_size=50,
                         anchor_x="center")
        arcade.draw_text("Press escape to quit or R to play again", WIDTH / 2, HEIGHT / 2 - 75, arcade.color.WHITE,
                         font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        elif key == arcade.key.ESCAPE:
            arcade.close_window()


class GameView(arcade.View):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """

        super().__init__()

        self.level = 1
        self.movement_block = None
        self.current_level = None
        self.movement_block_list = None
        self.tile_map = None
        self.scene = None
        self.lives = None

        self.movement = False
        self.collision_with_wall = False
        self.physics_engine = None
        self.key_pressed = False
        self.goal_hit = False

        # Sound effect came from freesound.org
        self.goal_sound = arcade.load_sound("goal.wav")

        self.collision_sound = arcade.load_sound(":resources:sounds/hurt2.wav")
        self.life_lost_sound = arcade.load_sound(":resources:sounds/lose5.wav")

    def setup(self):

        map_name = f"snow_level_{self.level}.json"
        self.tile_map = arcade.load_tilemap(map_name)

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.movement_block_list = arcade.SpriteList()
        self.movement_block = Player("snowBall.png", scale=1.7)
        self.movement_block.center_x = PLAYER_STARTING_X
        self.movement_block.center_y = PLAYER_STARTING_Y
        self.movement_block_list.append(self.movement_block)
        self.lives = LIVES

        self.physics_engine = arcade.PhysicsEngineSimple(self.movement_block, self.scene["reset"])


    def on_draw(self):

        self.window.clear()
        self.movement_block_list.draw()
        self.scene.draw()
        output_lives = f"lives:{self.lives}"
        arcade.draw_text(output_lives, 50, 50, arcade.color.BLACK, 12)

    def on_update(self, delta_time):

        self.movement_block_list.update()

        reset_hit_list = arcade.check_for_collision_with_list(self.movement_block, self.scene["reset"])
        goal_hit_list = arcade.check_for_collision_with_list(self.movement_block, self.scene["goal"])
        live_lost_list = arcade.check_for_collision_with_list(self.movement_block, self.scene["wall"])

        if goal_hit_list:
            if self.level == 5:
                self.level += 1
                arcade.play_sound(self.goal_sound)
                self.setup()
                self.key_pressed = False
            else:
                win_screen = WinScreen()
                self.window.show_view(win_screen)

        if reset_hit_list:
            if not self.collision_with_wall:
                self.collision_with_wall = True
                self.key_pressed = False
                self.movement_block.change_y = 0
                self.movement_block.change_x = 0

        if live_lost_list:
            self.movement_block.change_x = 0
            self.movement_block.change_y = 0

            self.movement_block.center_x = PLAYER_STARTING_X
            self.movement_block.center_y = PLAYER_STARTING_Y

            self.key_pressed = False
            self.collision_with_wall = False
            arcade.play_sound(self.life_lost_sound)

            self.lives -= 1
            return LIVES

        if self.lives == 0:
            print("game over")

        if self.level > 5:
            win_screen = WinScreen()
            self.window.show_view(win_screen)

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
                self.movement_block.center_x = PLAYER_STARTING_X
                self.movement_block.center_y = PLAYER_STARTING_Y
            elif key == arcade.key.S:
                self.level += 1
                self.setup()

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.collision_with_wall = False
        elif key == arcade.key.DOWN:
            self.collision_with_wall = False
        elif key == arcade.key.LEFT:
            self.collision_with_wall = False
        elif key == arcade.key.RIGHT:
            self.collision_with_wall = False



def main():
    """ Main method """

window = arcade.Window(WIDTH, HEIGHT, "Block Game")
menu_view = MenuView()
window.show_view(menu_view)
arcade.run()


if __name__ == "__main__":
    main()