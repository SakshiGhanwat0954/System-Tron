import tkinter as tk
import time
import math

# Create main application window
root = tk.Tk()
root.title("Analog Clock")
root.geometry("400x400")
root.resizable(False, False)
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Clock center and radius
CENTER_X, CENTER_Y = 200, 200
RADIUS = 100

def draw_clock():
    canvas.delete("all")  # Clear canvas
    
    # Draw clock face
    canvas.create_oval(CENTER_X - RADIUS, CENTER_Y - RADIUS, 
                        CENTER_X + RADIUS, CENTER_Y + RADIUS, outline="black", width=3)
    
    # Draw hour markers
    for i in range(12):
        angle = math.radians(i * 30 - 90)  # Adjusted for correct orientation
        x1 = CENTER_X + RADIUS * 0.85 * math.cos(angle)
        y1 = CENTER_Y + RADIUS * 0.85 * math.sin(angle)
        x2 = CENTER_X + RADIUS * math.cos(angle)
        y2 = CENTER_Y + RADIUS * math.sin(angle)
        canvas.create_line(x1, y1, x2, y2, width=2)
    
    # Get current time
    t = time.localtime()
    hours = t.tm_hour % 12
    minutes = t.tm_min
    seconds = t.tm_sec
    
    # Draw hour hand
    hour_angle = math.radians((hours * 30) + (minutes * 0.5) - 90)  # Adjusted for 12 o'clock start
    hour_x = CENTER_X + (RADIUS * 0.5) * math.cos(hour_angle)
    hour_y = CENTER_Y + (RADIUS * 0.5) * math.sin(hour_angle)
    canvas.create_line(CENTER_X, CENTER_Y, hour_x, hour_y, width=6, fill='black')
    
    # Draw minute hand
    min_angle = math.radians((minutes * 6) - 90)  # Adjusted
    min_x = CENTER_X + (RADIUS * 0.7) * math.cos(min_angle)
    min_y = CENTER_Y + (RADIUS * 0.7) * math.sin(min_angle)
    canvas.create_line(CENTER_X, CENTER_Y, min_x, min_y, width=4, fill='blue')
    
    # Draw second hand
    sec_angle = math.radians((seconds * 6) - 90)  # Adjusted
    sec_x = CENTER_X + (RADIUS * 0.9) * math.cos(sec_angle)
    sec_y = CENTER_Y + (RADIUS * 0.9) * math.sin(sec_angle)
    canvas.create_line(CENTER_X, CENTER_Y, sec_x, sec_y, width=2, fill='red')
    
    # Draw clock center
    canvas.create_oval(CENTER_X - 5, CENTER_Y - 5, CENTER_X + 5, CENTER_Y + 5, fill='black')
    
    # Update the clock every second
    root.after(1000, draw_clock)

# Start the clock
draw_clock()
root.mainloop()
