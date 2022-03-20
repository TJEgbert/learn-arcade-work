""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5


class Ghost:

    def __init__(self, position_x, position_y):

        self.position_x = position_x
        self.position_y = position_y

    def draw(self):

        # Ghost body
        arcade.draw_rectangle_filled(self.position_x,
                                     self.position_y,
                                     width=102,
                                     height=100,
                                     color=arcade.color.WHITE)
        # Ghost head
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y + 55,
                                  radius=51,
                                  color=arcade.color.WHITE)
        # Draws left eye
        arcade.draw_circle_filled(self.position_x - 20,
                                  self.position_y + 45,
                                  radius=10,
                                  color=arcade.color.BLACK)
        # Draws right eye
        arcade.draw_circle_filled(self.position_x + 20,
                                  self.position_y + 45,
                                  radius=10,
                                  color=arcade.color.BLACK)

        # Draws mouth
        arcade.draw_line(self.position_x - 25,
                         self.position_y,
                         self.position_x + 25,
                         self.position_y,
                         color=arcade.color.BLACK,
                         line_width=4)


class GirlGhost:

    def __init__(self, position_x, position_y, change_x, change_y, width, height, radius):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.radius = radius

    def update(self):

        # Updates the location of GirlGhost class
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.width - 50:
            self.position_x = self.width - 50

        if self.position_x > SCREEN_WIDTH - self.width + 24:
            self.position_x = SCREEN_WIDTH - self.width + 24

        if self.position_y < self.height:
            self.position_y = self.height

        if self.position_y > SCREEN_HEIGHT - self.height - 40:
            self.position_y = SCREEN_HEIGHT - self.height - 40

    def draw(self):

        # Draw body
        arcade.draw_rectangle_filled(self.position_x,
                                     self.position_y,
                                     self.width,
                                     self.height,
                                     color=arcade.color.WHITE)
        # Draw head
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y + 55,
                                  self.radius,
                                  color=arcade.color.WHITE)
        # Draws left eye
        arcade.draw_circle_filled(self.position_x - 20,
                                  self.position_y + 45,
                                  radius=10,
                                  color=arcade.color.BLACK)
        # Draws right eye
        arcade.draw_circle_filled(self.position_x + 20,
                                  self.position_y + 45,
                                  radius=10,
                                  color=arcade.color.BLACK)

        # Draws mouth
        arcade.draw_line(self.position_x - 25,
                         self.position_y,
                         self.position_x + 25,
                         self.position_y,
                         color=arcade.color.BLACK,
                         line_width=4)

        # Draws round part of bow
        arcade.draw_circle_filled(self.position_x + 30,
                                  self.position_y + 90,
                                  radius=10,
                                  color=arcade.color.DARK_PINK)

        # Draw left part of bow
        arcade.draw_triangle_filled(self.position_x + 30,
                                    self.position_y + 90,
                                    self.position_x + 30 - 50,
                                    self.position_y + 90 + 25,
                                    self.position_x + 30 - 25,
                                    self.position_y + 90 + 50,
                                    arcade.color.DARK_PINK)

        # Draws right part of bow
        arcade.draw_triangle_filled(self.position_x + 30,
                                    self.position_y + 90,
                                    self.position_x + 30 + 50,
                                    self.position_y + 90 - 25,
                                    self.position_x + 30 + 25,
                                    self.position_y + 90 - 50,
                                    arcade.color.DARK_PINK)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # set color of background
        arcade.set_background_color(arcade.color.BLUE)

        # remove mouse pointer
        self.set_mouse_visible(False)

        # Creates children classes from parent classes
        self.ghost = Ghost(300, 300)
        self.girl_ghost = GirlGhost(400, 400, 0, 0, 102, 100, 51)

        # Import sounds

        self.click_sound = arcade.load_sound("082- Earthbound - Going Down!.mp3")
        self.click_sound_player = None
        self.bump_sound = arcade.load_sound("083- Earthbound - Rough Landing.mp3")
        self.bump_sound_player = None

    def on_draw(self):

        arcade.start_render()

        # Draw children class
        self.ghost.draw()
        self.girl_ghost.draw()

        # Draw backgrounds

        def draw_bigger_gravestone(x, y):
            """Draw a bigger version of a gravestone"""
            arcade.draw_arc_filled(center_x=x,
                                   center_y=y,
                                   width=150,
                                   height=200,
                                   color=arcade.csscolor.GRAY,
                                   start_angle=0,
                                   end_angle=180,
                                   tilt_angle=0,
                                   num_segments=20)

            # Bottom of gravestone
            arcade.draw_rectangle_filled(center_x=x,
                                         center_y=y - 50,
                                         width=150,
                                         height=115,
                                         color=arcade.csscolor.GRAY)

        arcade.draw_rectangle_filled(400, 0, 800, 250, arcade.color.DARK_GREEN)
        draw_bigger_gravestone(100, 200)
        draw_bigger_gravestone(400, 200)
        draw_bigger_gravestone(700, 200)

    # Mouse movement for ghost child class
    def on_mouse_motion(self, x, y, dx, dy):

        self.ghost.position_x = x
        self.ghost.position_y = y
        self.ghost.direction_x = x + dx
        self.ghost.direction_y = y + dy

    # plays sound when left mouse button pressed
    def on_mouse_press(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.click_sound)

    # Updates movement information for the girl_ghost child class
    def update(self, delta_time):
        self.girl_ghost.update()

        # Checks for collision on top of screen and play sound effect if not already playing
        if self.girl_ghost.position_y + 140 == SCREEN_HEIGHT:
            if not self.bump_sound_player or not self.bump_sound_player.playing:
                self.bump_sound_player = arcade.play_sound(self.bump_sound)

        # Checks for collision on bottom of screen and play sound effect if not already playing
        elif self.girl_ghost.position_y - 100 == 0:
            if not self.bump_sound_player or not self.bump_sound_player.playing:
                self.bump_sound_player = arcade.play_sound(self.bump_sound)

        # Checks for collision on right of screen and play sound effect if not already playing
        elif self.girl_ghost.position_x + 78 == SCREEN_WIDTH:
            if not self.bump_sound_player or not self.bump_sound_player.playing:
                self.bump_sound_player = arcade.play_sound(self.bump_sound)

        # Checks for collision on left of screen and play sound effect if not already playing
        elif self.girl_ghost.position_x - 55 == 0:
            if not self.bump_sound_player or not self.bump_sound_player.playing:
                self.bump_sound_player = arcade.play_sound(self.bump_sound)

    # Increases of decreases by MOVEMENT_SPEED when key is pressed for the girl_ghost child class
    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.girl_ghost.change_x = - MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.girl_ghost.change_x = + MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.girl_ghost.change_y = + MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.girl_ghost.change_y = - MOVEMENT_SPEED

    # When key is released sets the change modifier back to zero
    def on_key_release(self, key, modifiers):

        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.girl_ghost.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.girl_ghost.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()