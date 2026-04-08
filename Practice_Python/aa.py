# # from turtle import *
# # from colorsys import *
# # setpos(0, 80)       # Move the turtle to starting position
# # speed(0)             # Fastest drawing speed
# # bgcolor('black')     # Black background
# # pensize(2)           # Pen thickness
# # h = 0.71             # Initial hue for colors
# # for i in range(150):
# #     c = hsv_to_rgb(h, 1, 1)  # Convert HSV to RGB
# #     color(c)                  # Set current drawing color
# #     h += 0.004                # Slightly change hue for next iteration

# #     circle(140 - 1, 90)       # Draw a circle arc
# #     lt(90)                    # Turn left 90 degrees
# #     lt(20)                    # Additional turn left
# #     circle(140 - 1, 90)       # Draw another circle arc
# #     lt(18)                    # Turn left slightly for spiral effect
# # hideturtle()  # Hide the turtle cursor

# from turtle import *
# from colorsys import hsv_to_rgb
# import math

# # Setup
# bgcolor('black')
# speed(0)
# pensize(2)
# h = 0.0  # initial hue
# n = 200  # number of steps

# # Function to draw a fancy spiral
# def fancy_spiral():
#     global h
#     for i in range(n):
#         # Dynamic color
#         c = hsv_to_rgb(h, 1, 1)
#         pencolor(c)
#         h += 0.005
#         if h > 1:
#             h = 0
        
#         # Dynamic radius for pulsating effect
#         radius = 100 + 50 * math.sin(i * 0.1)
#         circle(radius, 90)
#         left(91)  # slight rotation
#         forward(2)

# # Position turtle
# penup()
# setpos(0, -50)
# pendown()

# # Draw multiple spirals with rotation
# for j in range(6):
#     fancy_spiral()
#     right(60)

# hideturtle()
# done()

# from turtle import *
# from colorsys import hsv_to_rgb
# import math
# import time

# # Setup
# bgcolor('black')
# speed(0)
# pensize(2)
# tracer(0)  # Turn off automatic drawing for smooth animation

# hue = 0.0
# n = 150  # steps per spiral
# layers = 5  # number of overlapping spirals

# # Function to draw one spiral
# def draw_spiral(offset_angle=0):
#     global hue
#     penup()
#     setpos(0, 0)
#     setheading(offset_angle)
#     pendown()
    
#     for i in range(n):
#         # Smooth rainbow color
#         c = hsv_to_rgb(hue, 1, 1)
#         pencolor(c)
#         hue += 0.003
#         if hue > 1:
#             hue = 0
        
#         # Dynamic radius for pulsating spiral
#         radius = 100 + 50 * math.sin(i * 0.1)
#         circle(radius, 60)
#         left(59)  # slight rotation
#         forward(1)

# # Main loop for animation
# while True:
#     clear()  # Clear previous drawing
#     for l in range(layers):
#         draw_spiral(offset_angle=l * (360 / layers))
#     update()  # Render drawing
#     time.sleep(0.02)  # control animation speeds