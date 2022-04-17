""" Snowball Home"""
"""By Trevor Egbert"""
""" I would like to thank 
    Kenny.nl for the sprite used in this project,
    incompetech.com for the music
    and freesound.org for some of the sound effects"""

import arcade

# --- Constants ---

MOVEMENT_SPEED = 17

WIDTH = 1050
HEIGHT = 1050

LIVES = 3

PLAYER_STARTING_X = 110
PLAYER_STARTING_Y = 110


class Player(arcade.Sprite):
    """sets up player for movement"""
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class MenuView(arcade.View):
    """Sets up the MenuView on Game Start"""

    def __init__(self):
        super().__init__()

        # Sets up background image
        self.menu_background = arcade.load_texture("menu_screen.png")

    def on_draw(self):

        # clears window
        self.window.clear()
        # displays background image
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.menu_background)

    def on_key_press(self, key, modifiers):
        """Sets up buttons: Enter to start game, Escape to close game"""

        if key == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        elif key == arcade.key.ESCAPE:
            arcade.close_window()


class WinScreen(arcade.View):
    """Sets up WinScreen"""

    def __init__(self):
        super().__init__()

        # Sound effect came from freesound.org and sets up sound to play
        self.victory_fanfare = arcade.load_sound("victory-fanfare.wav")
        self.victory_fanfare_player = self.victory_fanfare.play(volume=.4)

        # sets up background image
        self.win_background = arcade.load_texture("win_screen.png")

    def setup(self):

        # Players victory sound effect
        self.victory_fanfare.play()

    def on_draw(self):

        # Clears Window
        self.window.clear()
        # Displays background image
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.win_background)

    def on_key_press(self, key, modifiers):
        """Sets up buttons: R to restart game and Escape to close game"""

        if key == arcade.key.R:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        elif key == arcade.key.ESCAPE:
            arcade.close_window()


class GameOver(arcade.View):

    def __init__(self):
        super().__init__()

        # Sound effect came from freesound.org and sets up sound to play
        self.game_over = arcade.load_sound("game-over.wav")
        self.game_over_player = self.game_over.play(volume=.8)

        # Sets up background image
        self.game_over_background = arcade.load_texture("game_over.png")

    def setup(self):

        # Play game over sound effect
        self.game_over_player.play()

    def on_draw(self):

        # Clears window
        self.window.clear()
        # Displays background image
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.game_over_background)

    def on_key_press(self, key, modifiers):
        """Sets up buttons: R to restart game and Escape to close game"""
        if key == arcade.key.R:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        elif key == arcade.key.ESCAPE:
            arcade.close_window()


class GameView(arcade.View):
    """GameView window"""

    def __init__(self):
        """ Initializer """

        super().__init__()

        # sets up level parameters
        self.level = 1
        self.tile_map = None
        self.scene = None
        self.current_level = None
        self.lives = None
        self.background_music_playing = False

        # Set up player
        self.movement_block = None
        self.movement_block_list = None

        # Sets up mechanics
        self.movement = False
        self.collision_with_wall = False
        self.physics_engine = None
        self.key_pressed = False
        self.goal_hit = False

        # Sound effect came from freesound.org
        self.goal_sound = arcade.load_sound("goal.wav")

        # Sets up sound effects and music
        """background music from incompetech.com
        "Mana Two - Part 2" Kevin MacLeod (incompetech.com)
    Licensed under Creative Commons: By Attribution 4.0 License
            http://creativecommons.org/licenses/by/4.0/"""

        self.background_music = arcade.load_sound("Mana Two - Part 2.mp3", True)

        self.collision_sound = arcade.load_sound(":resources:sounds/hurt2.wav")
        self.life_lost_sound = arcade.load_sound(":resources:sounds/lose5.wav")

        self.background_player = self.background_music.play(volume=.5, loop=True)

    def setup(self):

        # Plays background music if its already not playing
        if not self.background_music_playing:
            self.background_player.play()

        # Load the tile maps from the files
        map_name = f"snow_level_{self.level}.json"
        self.tile_map = arcade.load_tilemap(map_name)

        # Put the tile maps as a scene
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Movement block list and sets up movement block in level
        self.movement_block_list = arcade.SpriteList()
        # All sprite's came from kenney.nl
        self.movement_block = Player("snowBall.png", scale=1.7)
        self.movement_block.center_x = PLAYER_STARTING_X
        self.movement_block.center_y = PLAYER_STARTING_Y
        self.movement_block_list.append(self.movement_block)

        # Load lives
        self.lives = LIVES

    def on_show(self):

        # Sets up background color
        arcade.set_background_color(arcade.color.BLUEBERRY)

    def on_draw(self):

        # Clears window
        self.window.clear()

        # Draws movement block
        self.movement_block_list.draw()

        # Draws the window
        self.scene.draw()

        # Draws where "Lives" are and then draws lives
        arcade.draw_rectangle_filled(center_x=99, center_y=30, color=arcade.color.BLACK, width=182, height=57)
        arcade.draw_rectangle_filled(center_x=100, center_y=30, color=arcade.color.WHITE, width=175, height=50)
        output_lives = f"Lives:{self.lives}"
        arcade.draw_text(output_lives, 15, 18, arcade.color.BLACK, 30, font_name="Rockwell Extra Bold")

    def on_update(self, delta_time):

        # Updates movement block for movement
        self.movement_block_list.update()

        # Sets up collision with the scene layer reset
        reset_hit_list = arcade.check_for_collision_with_list(self.movement_block, self.scene["reset"])
        # Sets up collision with the scene layer goal
        goal_hit_list = arcade.check_for_collision_with_list(self.movement_block, self.scene["goal"])
        # Sets up collision with the scene layer wall
        live_lost_list = arcade.check_for_collision_with_list(self.movement_block, self.scene["wall"])

        # checks level to see if level == 11 to display win screen
        if self.level == 11:
            win_screen = WinScreen()
            self.window.show_view(win_screen)
            arcade.stop_sound(self.background_player)
        # Checks goal_hit_list: increases level by one and plays victory sound and reset key_pressed False
        elif goal_hit_list:
            self.level += 1
            arcade.play_sound(self.goal_sound)
            self.setup()
            self.key_pressed = False

        # Checks reset_hit_list: and if it False
        if reset_hit_list:
            # Sets player movement to 0. Sets collision to True. key_pressed to False and player sound effect
            if not self.collision_with_wall:
                self.collision_with_wall = True
                self.key_pressed = False
                self.movement_block.change_y = 0
                self.movement_block.change_x = 0
                arcade.play_sound(self.collision_sound)

        # If live_lost_list: player movement to 0
        if live_lost_list:
            self.movement_block.change_x = 0
            self.movement_block.change_y = 0

            # Sets player back to starting position
            self.movement_block.center_x = PLAYER_STARTING_X
            self.movement_block.center_y = PLAYER_STARTING_Y

            # sets key_pressed and collision to False
            self.key_pressed = False
            self.collision_with_wall = False
            # Plays sound effect
            arcade.play_sound(self.life_lost_sound)
            # Minus one to Lives
            self.lives -= 1

        # If lives == 0 the loads GameOver()view
        if self.lives == 0:
            game_over_screen = GameOver()
            self.window.show_view(game_over_screen)
            arcade.stop_sound(self.background_player)

    def on_key_press(self, key, modifiers):

        # If key pressed False allows movement
        if not self.key_pressed:

            # Sets up player Key movements and sets key_pressed True
            if key == arcade.key.UP or key == arcade.key.W:
                self.movement_block.change_y = MOVEMENT_SPEED
                self.key_pressed = True
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.movement_block.change_y = - MOVEMENT_SPEED
                self.key_pressed = True
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.movement_block.change_x = MOVEMENT_SPEED
                self.key_pressed = True
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.movement_block.change_x = - MOVEMENT_SPEED
                self.key_pressed = True
            elif key == arcade.key.R:
                self.movement_block.center_x = PLAYER_STARTING_X
                self.movement_block.center_y = PLAYER_STARTING_Y
            elif key == arcade.key.T:
                # Lets you skip level
                self.level += 1
                self.setup()
            elif key == arcade.key.ESCAPE:
                # Close Window
                arcade.close_window()

    def on_key_release(self, key, modifiers):

        # On release set collision_with_wall False
        if key == arcade.key.UP or key == arcade.key.W:
            self.collision_with_wall = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.collision_with_wall = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.collision_with_wall = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.collision_with_wall = False


def main():

    window = arcade.Window(WIDTH, HEIGHT, "Block Game")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()