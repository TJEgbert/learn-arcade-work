""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # set color of background
        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()

        def draw_ghost(x, y):
            arcade.draw_rectangle_filled(center_x=x,
                                         center_y=y,
                                         width=102,
                                         height=100,
                                         color=arcade.color.WHITE)
            arcade.draw_circle_filled(center_x=x,
                                      center_y=y + 55,
                                      radius=51,
                                      color=arcade.color.WHITE)
            # draws left eye
            arcade.draw_circle_filled(center_x=x - 20,
                                      center_y=y + 45,
                                      radius=5,
                                      color=arcade.color.BLACK)
            # draws right eye
            arcade.draw_circle_filled(center_x=x + 20,
                                      center_y=y + 45,
                                      radius=5,
                                      color=arcade.color.BLACK)

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
        draw_bigger_gravestone(200, 200)
        draw_ghost(200, 200)


def main():
    window = MyGame()
    arcade.run()


main()