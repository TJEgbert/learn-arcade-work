"""
This program will draw a spooky castle!
"""

# import arcade
import arcade

# Open and set window size (width and height)
arcade.open_window(900, 1000, "Spooky Castle")

# background color
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

# Connecting arm
arcade.draw_rectangle_filled(center_x=250,
                             center_y=600,
                             width=40,
                             height=225,
                             color=(0, 0, 0),
                             tilt_angle=100)

# connecting joint
arcade.draw_rectangle_filled(center_x=152,
                             center_y=678,
                             width=40,
                             height=150,
                             color=(0, 0, 0))

# building part of tower
arcade.draw_rectangle_filled(center_x=152,
                             center_y=800,
                             width=175,
                             height=150,
                             color=(0, 0, 0))

# roof of tower
arcade.draw_triangle_filled(x1=65,
                            y1=875,
                            x2=237,
                            y2=875,
                            x3=150,
                            y3=950,
                            color=(10, 10, 10))
# Window
arcade.draw_rectangle_filled(center_x=152,
                             center_y=790,
                             width=50,
                             height=70,
                             color=(208, 242, 14))
# Top of window
arcade.draw_circle_filled(center_x=152,
                          center_y=820,
                          radius=25,
                          color=(208, 242, 14))

# ----- Right Tower ---------

# Connecting arm
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

# roof of tower
arcade.draw_triangle_filled(x1=635,
                            y1=900,
                            x2=840,
                            y2=900,
                            x3=736,
                            y3=970,
                            color=(250, 10, 10))

arcade.draw_ellipse_filled(center_x=736,
                           center_y=800,
                           width=80,
                           height=100,
                           color=(208, 242, 14),
                           tilt_angle=0,
                           num_segments=30,)

# ----- Drawing Castle -----

# Main part of Castle
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

# ------ Clock -------------

arcade.draw_circle_filled(center_x=450,
                          center_y=850,
                          radius=75,
                          color=arcade.csscolor.WHITE)

# -------- Hour lines-----

# 12
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=450,
                 end_y=1000,
                 color=(0, 0, 0),
                 line_width=5)
# 1
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=530,
                 end_y=1000,
                 color=(0, 0, 0),
                 line_width=5)
# 2
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=700,
                 end_y=1000,
                 color=(0, 0, 0),
                 line_width=5)
# 3
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=800,
                 end_y=850,
                 color=(0, 0, 0),
                 line_width=5)
# 4
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=800,
                 end_y=650,
                 color=(0, 0, 0),
                 line_width=5)
# 5
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=600,
                 end_y=600,
                 color=(0, 0, 0),
                 line_width=5)
# 6
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=450,
                 end_y=450,
                 color=(0, 0, 0),
                 line_width=5)
# 7
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=80,
                 end_y=200,
                 color=(0, 0, 0),
                 line_width=5)
# 8
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=150,
                 end_y=670,
                 color=(0, 0, 0),
                 line_width=5)
# 9
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=300,
                 end_y=850,
                 color=(0, 0, 0),
                 line_width=5)
# 10
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=200,
                 end_y=1000,
                 color=(0, 0, 0),
                 line_width=5)
# 11
arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=373,
                 end_y=1000,
                 color=(0, 0, 0),
                 line_width=5)

arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=450,
                 end_y=1000,
                 color=(0, 0, 0),
                 line_width=5)

arcade.draw_line(start_x=450,
                 start_y=850,
                 end_x=450,
                 end_y=1000,
                 color=(0, 0, 0),
                 line_width=5)

# Window top left
arcade.draw_rectangle_filled(center_x=350,
                             center_y=600,
                             width=50,
                             height=100,
                             color=(208, 242, 14))

# Window middle right
arcade.draw_rectangle_filled(center_x=550,
                             center_y=550,
                             width=50,
                             height=100,
                             color=(208, 242, 14))

# Window bottom left
arcade.draw_rectangle_filled(center_x=360,
                             center_y=450,
                             width=50,
                             height=100,
                             color=(208, 242, 14))

# Door
arcade.draw_rectangle_filled(center_x=450,
                             center_y=383,
                             width=80,
                             height=115,
                             color=(32, 22, 6))

arcade.draw_circle_filled(center_x=450,
                          center_y=436,
                          radius=40,
                          color=(32, 22, 6))
# finish drawing
arcade.finish_render()

# Keep window open
arcade.run()
