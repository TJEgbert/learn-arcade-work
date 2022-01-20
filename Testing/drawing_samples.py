"""
this is a sample a test for the drawing functions

three double-quote marks
"""

# single lines use number sign.
# importing arcade
import arcade

# sets the dimensions of (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Start drawing function
arcade.start_render()

# (this is where the drawing code will go

# Drawing a rectangle
# Left of 0, right of 599
# top of 300 bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Drawing tree truck
# center of 100, 320
# Width of 20
# Height of 60
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and ellipse for top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and arc for top
# Arc is centered at (300, 340) with a width of 60 and height 100
# The starting angle is 0, and ending angle is 180
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Tree with trunk and triangle for top
# Triangle is made of these three points:
# (400, 400), (370, 320), (430,320)
arcade.draw_triangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)



# finish drawing
arcade.finish_render()

# keeps window open until someone closes it
arcade.run()
