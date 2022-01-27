"""
This program will draw a spooky building!
"""

# Import arcade
import arcade

# Open and set window size (width and height)
arcade.open_window(900, 1000, "Spooky Building")

# Background color
arcade.set_background_color((6, 8, 28))

# Starting drawing code
arcade.start_render()

# -------- Set up background ---------

# Drawing ground
arcade.draw_rectangle_filled(center_x=450,
                             center_y=0,
                             width=900,
                             height=750,
                             color=(3, 73, 16))
# Drawing moon
arcade.draw_circle_filled(center_x=850,
                          center_y=900,
                          radius=150,
                          color=arcade.csscolor.YELLOW)


# ------left Tower-------

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

# Building part of tower
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
# Window
arcade.draw_rectangle_filled(center_x=152,
                             center_y=790,
                             width=50,
                             height=70,
                             color=(189, 219, 21))
# Top of window
arcade.draw_circle_filled(center_x=152,
                          center_y=820,
                          radius=25,
                          color=(189, 219, 21))

# ----- Right Tower ---------

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

# Window
arcade.draw_ellipse_filled(center_x=736,
                           center_y=800,
                           width=80,
                           height=100,
                           color=(189, 219, 21),
                           tilt_angle=0,
                           num_segments=30,)

# ----- Drawing building -----

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

# Window top left
arcade.draw_rectangle_filled(center_x=350,
                             center_y=600,
                             width=50,
                             height=100,
                             color=(189, 219, 21))

# Window middle right
arcade.draw_rectangle_filled(center_x=550,
                             center_y=550,
                             width=50,
                             height=100,
                             color=(189, 219, 21))

# Window bottom left
arcade.draw_rectangle_filled(center_x=360,
                             center_y=450,
                             width=50,
                             height=100,
                             color=(189, 219, 21))

# Door
arcade.draw_rectangle_filled(center_x=450,
                             center_y=383,
                             width=80,
                             height=115,
                             color=(32, 22, 6))

# ------ Window on Third Floor -------------

# Round part
arcade.draw_circle_filled(center_x=450,
                          center_y=850,
                          radius=75,
                          color=(189, 219, 21))

# Top Line
arcade.draw_line(start_x=450,
                 start_y=775,
                 end_x=450,
                 end_y=925,
                 color=(0, 0, 0),
                 line_width=5)

# Right Line
arcade.draw_line(start_x=525,
                 start_y=850,
                 end_x=375,
                 end_y=850,
                 color=(0, 0, 0),
                 line_width=5)

# ----------- Grave Stones ---------------

# ------Front Grave ---------
# Top
arcade.draw_arc_filled(center_x=200,
                       center_y=200,
                       width=150,
                       height=200,
                       color=arcade.csscolor.GRAY,
                       start_angle=0,
                       end_angle=180,
                       tilt_angle=0,
                       num_segments=20,
                       )

# Bottom of gravestone
arcade.draw_rectangle_filled(center_x=200,
                             center_y=150,
                             width=150,
                             height=115,
                             color=arcade.csscolor.GRAY)

# Text On Grave
arcade.draw_text(text="RIP",
                 start_x=170,
                 start_y=200,
                 color=arcade.csscolor.BLACK,
                 font_size=30)

# ------ Back left gravestone ------

# Top of Grave
arcade.draw_arc_filled(center_x=100,
                       center_y=370,
                       width=113,
                       height=150,
                       color=arcade.csscolor.GRAY,
                       start_angle=0,
                       end_angle=180,
                       tilt_angle=0,
                       num_segments=20,
                       )

# Bottom of gravestone
arcade.draw_rectangle_filled(center_x=100,
                             center_y=325,
                             width=112,
                             height=100,
                             color=arcade.csscolor.GRAY)

# Text On Grave
arcade.draw_text(text="RIP",
                 start_x=65,
                 start_y=350,
                 color=arcade.csscolor.BLACK,
                 font_name=("Old English Text MT", "arial"),
                 font_size=25)

# -------- Right gravestone ------

# Top of Grave
arcade.draw_arc_filled(center_x=800,
                       center_y=300,
                       width=113,
                       height=150,
                       color=arcade.csscolor.GRAY,
                       start_angle=0,
                       end_angle=180,
                       tilt_angle=0,
                       num_segments=20,
                       )

# Bottom of gravestone
arcade.draw_rectangle_filled(center_x=800,
                             center_y=250,
                             width=112,
                             height=100,
                             color=arcade.csscolor.GRAY)

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
