"""
This program will draw a spooky building!
Trevor Egbert
"""

# Import arcade
import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1000


def draw_ground():
    """Draws the ground"""
    arcade.draw_rectangle_filled(center_x=450,
                                 center_y=0,
                                 width=900,
                                 height=750,
                                 color=(3, 73, 16))


def draw_moon():
    """Draws the moon"""
    arcade.draw_circle_filled(center_x=850,
                              center_y=900,
                              radius=150,
                              color=arcade.csscolor.YELLOW)


def draw_left_joints():
    """Draws the connecting joints to left tower"""
    # Connecting arm to building
    arcade.draw_rectangle_filled(center_x=250,
                                 center_y=600,
                                 width=40,
                                 height=225,
                                 color=(0, 0, 0),
                                 tilt_angle=100)

    # Connecting joint
    arcade.draw_rectangle_filled(center_x=152,
                                 center_y=678,
                                 width=40,
                                 height=150,
                                 color=(0, 0, 0))


def draw_small_tower():
    """Draw a small tower with a gray roof"""
    arcade.draw_rectangle_filled(center_x=152,
                                 center_y=800,
                                 width=175,
                                 height=150,
                                 color=(0, 0, 0))

    # Roof of tower
    arcade.draw_triangle_filled(x1=65,
                                y1=875,
                                x2=237,
                                y2=875,
                                x3=150,
                                y3=950,
                                color=(42, 42, 43))


def draw_arch_window(x, y):
    """Draws an arch window"""
    arcade.draw_rectangle_filled(center_x=x,
                                 center_y=y,
                                 width=50,
                                 height=70,
                                 color=(189, 219, 21))
    # Top of window
    arcade.draw_circle_filled(center_x=x,
                              center_y=y + 30,
                              radius=25,
                              color=(189, 219, 21))


def draw_right_joints():
    """Draws connecting joints to the right tower"""
    # Connecting arm to building
    arcade.draw_rectangle_filled(center_x=670,
                                 center_y=525,
                                 width=40,
                                 height=225,
                                 color=(0, 0, 0),
                                 tilt_angle=40)

    # Connecting Joint
    arcade.draw_rectangle_filled(center_x=736,
                                 center_y=700,
                                 width=40,
                                 height=200,
                                 color=(0, 0, 0))


def draw_big_tower():
    """Draws a bigger tower with a gray roof"""
    # Building top of tower
    arcade.draw_rectangle_filled(center_x=736,
                                 center_y=800,
                                 width=200,
                                 height=200,
                                 color=(0, 0, 0))

    # Roof of tower
    arcade.draw_triangle_filled(x1=635,
                                y1=900,
                                x2=840,
                                y2=900,
                                x3=736,
                                y3=970,
                                color=(42, 42, 43))


def draw_oval_window(x, y):
    """Draws an oval that you can place"""
    arcade.draw_ellipse_filled(center_x=x,
                               center_y=y,
                               width=80,
                               height=100,
                               color=(189, 219, 21),
                               tilt_angle=0,
                               num_segments=30)


def draw_main_building():
    """This draws the main portion of the spooky building"""
    # Main part of building
    arcade.draw_rectangle_filled(center_x=450,
                                 center_y=500,
                                 width=350,
                                 height=350,
                                 color=arcade.csscolor.BLACK)

    # Second floor
    arcade.draw_rectangle_filled(center_x=450,
                                 center_y=740,
                                 width=300,
                                 height=180,
                                 color=arcade.csscolor.BLACK)

    # Third floor
    arcade.draw_rectangle_filled(center_x=450,
                                 center_y=900,
                                 width=250,
                                 height=200,
                                 color=arcade.csscolor.BLACK)


def draw_rectangle_window(x, y):
    """Draws rectangle window that can be placed"""
    arcade.draw_rectangle_filled(center_x=x,
                                 center_y=y,
                                 width=50,
                                 height=100,
                                 color=(189, 219, 21))


def draw_door():
    """Draws a wooden door"""
    arcade.draw_rectangle_filled(center_x=450,
                                 center_y=383,
                                 width=80,
                                 height=115,
                                 color=(32, 22, 6))


def draw_circle_window(x, y):
    """Draws a window with cross design"""
    # Round part
    arcade.draw_circle_filled(center_x=x,
                              center_y=y,
                              radius=75,
                              color=(189, 219, 21))


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


def draw_smaller_gravestone(x, y):
    """Draw a smaller version of a gravestone"""

    # Top of Grave
    arcade.draw_arc_filled(center_x=x,
                           center_y=y,
                           width=113,
                           height=150,
                           color=arcade.csscolor.GRAY,
                           start_angle=0,
                           end_angle=180,
                           tilt_angle=0,
                           num_segments=20,
                           )

    # Bottom of gravestone
    arcade.draw_rectangle_filled(center_x=x,
                                 center_y=y - 45,
                                 width=112,
                                 height=100,
                                 color=arcade.csscolor.GRAY)


def main():
    """Setting up the screen and background"""
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Spooky Building")
    arcade.set_background_color((6, 8, 28))
    arcade.start_render()

    """Drawing background objects"""
    draw_ground()
    draw_moon()

    """Drawing Left tower"""
    draw_left_joints()
    draw_small_tower()
    draw_arch_window(x=152,
                     y=790)

    """Drawing right tower"""
    draw_right_joints()
    draw_big_tower()
    draw_oval_window(x=736,
                     y=800)

    """Drawing main building with decorations"""
    draw_main_building()
    draw_arch_window(x=350,
                     y=550)
    draw_rectangle_window(x=550,
                          y=600)
    draw_rectangle_window(x=550,
                          y=450)
    draw_door()
    """Draw window with cross design"""
    draw_circle_window(x=450,
                       y=850)

    # Right Line
    arcade.draw_line(start_x=525,
                     start_y=850,
                     end_x=375,
                     end_y=850,
                     color=(0, 0, 0),
                     line_width=5)

    # Top Line
    arcade.draw_line(start_x=450,
                     start_y=775,
                     end_x=450,
                     end_y=925,
                     color=(0, 0, 0),
                     line_width=5)

    """Drawing gravestones in the yard"""
    draw_smaller_gravestone(x=200,
                            y=200)
    # Text On Grave
    arcade.draw_text(text="RIP",
                     start_x=170,
                     start_y=200,
                     color=arcade.csscolor.BLACK,
                     font_size=30)

    draw_smaller_gravestone(x=100,
                            y=370)
    # Text On Grave
    arcade.draw_text(text="RIP",
                     start_x=65,
                     start_y=350,
                     color=arcade.csscolor.BLACK,
                     font_name=("Old English Text MT", "arial"),
                     font_size=25)

    draw_smaller_gravestone(x=800,
                            y=300)
    # Text On Grave
    arcade.draw_text(text="RIP",
                     start_x=760,
                     start_y=280,
                     color=arcade.csscolor.DARK_RED,
                     font_name=("Chiller", "arial"),
                     font_size=50)

    # finish drawing
    arcade.finish_render()

    # Keep window open
    arcade.run()


main()
