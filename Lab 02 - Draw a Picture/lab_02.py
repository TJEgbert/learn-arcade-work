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
                             height=900,
                             color=arcade.csscolor.DARK_GREEN)
# Drawing moon
arcade.draw_circle_filled(center_x=850,
                          center_y=900,
                          radius=150,
                          color=arcade.csscolor.YELLOW)

# ----- Drawing Castle -----

# Main Part
arcade.draw_rectangle_filled(center_x=450,
                             center_y=600,
                             width=350,
                             height=350,
                             color=arcade.csscolor.BLACK)

# finish drawing
arcade.finish_render()

# Keep window open
arcade.run()
