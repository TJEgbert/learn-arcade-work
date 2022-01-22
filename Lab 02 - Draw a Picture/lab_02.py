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

arcade.draw_circle_filled(center_x=152,
                          center_y=820,
                          radius=25,
                          color=(208, 242, 14))

# ----- Right Tower ---------


# ----- Drawing Castle -----

# Main part of Castle
arcade.draw_rectangle_filled(center_x=450,
                             center_y=500,
                             width=350,
                             height=350,
                             color=arcade.csscolor.BLACK)

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
