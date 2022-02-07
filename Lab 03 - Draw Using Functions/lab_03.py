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


def draw_arch_window(x_location, y_location):
    """Draws an arch window"""
    arcade.draw_rectangle_filled(center_x=x_location,
                                 center_y=y_location,
                                 width=50,
                                 height=70,
                                 color=(189, 219, 21))
    # Top of window
    arcade.draw_circle_filled(center_x=x_location,
                              center_y=y_location + 30,
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


def draw_oval_window(x_location, y_location):
    """Draws an oval that you can place"""
    arcade.draw_ellipse_filled(center_x=x_location,
                               center_y=y_location,
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


def draw_rectangle_window(x_location, y_location):
    """Draws rectangle window that can be placed"""
    arcade.draw_rectangle_filled(center_x=x_location,
                                 center_y=y_location,
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


def draw_circle_window(location_x, location_y, horizontal_x_start, horizontal_y_start, horizontal_x_end,
                       horizontal_y_end, vertical_x_start, vertical_y_start, vertical_x_end, vertical_y_end):
    """Draws a window with cross design"""
    # Round part
    arcade.draw_circle_filled(center_x=location_x,
                              center_y=location_y,
                              radius=75,
                              color=(189, 219, 21))

    # Right Line
    arcade.draw_line(start_x=horizontal_x_start,
                     start_y=horizontal_y_start,
                     end_x=horizontal_x_end,
                     end_y=horizontal_y_end,
                     color=(0, 0, 0),
                     line_width=5)

    # Top Line
    arcade.draw_line(start_x=vertical_x_start,
                     start_y=vertical_y_start,
                     end_x=vertical_x_end,
                     end_y=vertical_y_end,
                     color=(0, 0, 0),
                     line_width=5)


def draw_bigger_gravestone(x_location, y_location):
    """Draw a bigger version of a gravestone"""
    arcade.draw_arc_filled(center_x=x_location,
                           center_y=y_location,
                           width=150,
                           height=200,
                           color=arcade.csscolor.GRAY,
                           start_angle=0,
                           end_angle=180,
                           tilt_angle=0,
                           num_segments=20)

    # Bottom of gravestone
    arcade.draw_rectangle_filled(center_x=x_location,
                                 center_y=y_location - 50,
                                 width=150,
                                 height=115,
                                 color=arcade.csscolor.GRAY)


def draw_smaller_gravestone(x_location, y_location):
    """Draw a smaller version of a gravestone"""

    # Top of Grave
    arcade.draw_arc_filled(center_x=x_location,
                           center_y=y_location,
                           width=113,
                           height=150,
                           color=arcade.csscolor.GRAY,
                           start_angle=0,
                           end_angle=180,
                           tilt_angle=0,
                           num_segments=20,
                           )

    # Bottom of gravestone
    arcade.draw_rectangle_filled(center_x=x_location,
                                 center_y=y_location - 45,
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
    draw_arch_window(x_location=152,
                     y_location=790)

    """Drawing right tower"""
    draw_right_joints()
    draw_big_tower()
    draw_oval_window(x_location=736,
                     y_location=800)

    """Drawing main building with decorations"""
    draw_main_building()
    draw_rectangle_window(x_location=350,
                          y_location=550)
    draw_rectangle_window(x_location=550,
                          y_location=600)
    draw_rectangle_window(x_location=550,
                          y_location=450)
    draw_door()
    draw_circle_window(location_x=450,
                       location_y=850,
                       horizontal_x_start=525,
                       horizontal_y_start=850,
                       horizontal_x_end=375,
                       horizontal_y_end=850,
                       vertical_x_start=450,
                       vertical_y_start=775,
                       vertical_x_end=450,
                       vertical_y_end=925)

    """Drawing gravestones in the yard"""
    draw_bigger_gravestone(x_location=200,
                           y_location=200)
    # Text On Grave
    arcade.draw_text(text="RIP",
                     start_x=170,
                     start_y=200,
                     color=arcade.csscolor.BLACK,
                     font_size=30)
    draw_smaller_gravestone(x_location=100,
                            y_location=370)

    # Text On Grave
    arcade.draw_text(text="RIP",
                     start_x=65,
                     start_y=350,
                     color=arcade.csscolor.BLACK,
                     font_name=("Old English Text MT", "arial"),
                     font_size=25)

    draw_smaller_gravestone(x_location=800,
                            y_location=300)

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
