import tkinter as tk
from tkinter import messagebox
import subprocess
import sys




# Function to open a new window with "Part 2"
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Part 2")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="CHAPTER 2", font=("Helvetica", 16))
    label.pack(pady=20)
    label = tk.Label(new_window, text="so you want to be a super hero dude", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(new_window, text="yes!", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(new_window, text="what is your super hero name dude?", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(new_window, text="my super hero name is ketchup man.", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(new_window, text="cool name dude!", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(new_window, text="whats your power dude?", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(new_window, text="my power is shooting ketchup out of my finger.", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(new_window, text="cool power dude.", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(new_window, text="can i have some?", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(new_window, text="sure dude!", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(new_window, text="you pass!", font=("Helvetica", 14))
    label.pack(pady=10)
    
    # Button to open the third window with "Part 3"
    open_third_window_button = tk.Button(new_window, text="Go to Part 3", command=open_new_window3)
    open_third_window_button.pack(pady=20)

# Function to open the third window with "Part 3"
def open_new_window3():
    third_window = tk.Toplevel(root)
    third_window.title("Part 3")
    third_window.geometry("300x200")
    label = tk.Label(third_window, text="CHAPTER 3", font=("Helvetica", 16))
    label.pack(pady=20)
    label = tk.Label(third_window, text="hey there is big news at the big news station over there!", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(third_window, text="ok?", font=("Helvetica", 14))
    label.pack(pady=10)
    open_window_button = tk.Button(third_window, text="see film", command=open_new_window_film)
    open_window_button.pack(pady=20)
    label = tk.Label(third_window, text="this is a job for ketchup boy!", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(third_window, text="hmmm?", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(third_window, text="mustard man !", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(third_window, text="ketchup man hated mustard man.", font=("Helvetica", 14))
    label.pack(pady=10)
    label = tk.Label(third_window, text="the battle is going to start!", font=("Helvetica", 14))
    label.pack(pady=10)
    open_window_button = tk.Button(third_window, text="boss", command=lambda: open_new_window_boss(third_window))
    open_window_button.pack(pady=20)

# Function to open the animation window
def open_new_window_film():
    animation_window = tk.Toplevel(root)
    animation_window.title("Animation")
    animation_window.geometry("600x600")
    canvas = tk.Canvas(animation_window, width=600, height=600, bg="red")
    canvas.pack()

    # Create character instances
    ketchup = Character(canvas, 50, 50, 100, "black ")
    mustard = Character(canvas, 150, 50, 100, "red")

    # Function to move characters
    def move_characters():
        dx, dy = 5, 0
        ketchup.move(dx, dy)
        animation_window.after(50, move_characters)

    move_characters()

class Character:
    def __init__(self, canvas, x, y, health, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health
        self.color = color
        self.rect = canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
        self.health_bar = canvas.create_rectangle(x, y - 10, x + 30, y - 5, fill='green')
    
    def move(self, dx, dy):
        self.canvas.move(self.rect, dx, dy)
        self.canvas.move(self.health_bar, dx, dy)
        self.x += dx
        self.y += dy
    
    def get_coords(self):
        return self.canvas.coords(self.rect)
    
    def update_health_bar(self):
        x1, y1, x2, y2 = self.get_coords()
        health_ratio = self.health / self.max_health
        self.canvas.coords(self.health_bar, x1, y1 - 10, x1 + 30 * health_ratio, y1 - 5)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.update_health_bar()
        if self.health == 0:
            self.canvas.create_text(300, 300, text=f"{self.color.capitalize()} Man is defeated!", fill="red")

# Set the size of the window
root = tk.Tk()
root.geometry("500x500")

# Create a label with text
label = tk.Label(root, text="CHAPTER 1", font=("Helvetica", 16))
label.pack(pady=20)
label = tk.Label(root, text="one day ketchup man was at the factory.", font=("Helvetica", 10))
label.pack(pady=20)                        
label = tk.Label(root, text="he was making ketchup, but it was special ketchup.", font=("Helvetica", 10))
label.pack(pady=20)
label = tk.Label(root, text="he tried some. it turned his blood into ketchup!", font=("Helvetica", 10))
label.pack(pady=20)
label = tk.Label(root, text="then he went to the hospital. then he got surgery.", font=("Helvetica", 10))
label.pack(pady=20)
label = tk.Label(root, text="his surgery is done!", font=("Helvetica", 10))
label.pack(pady=20)
label = tk.Label(root, text="CHAPTER 2", font=("Helvetica", 10))
label.pack(pady=20)





# Button to open a new window with "Part 2"
open_window_button = tk.Button(root, text="Go to Part 2", command=open_new_window)
open_window_button.pack(pady=20)


#open the boss window
def open_new_window_boss(new_window_boss):
    
    try:
        # Open the Python file to ensure it exists and can be read
        with open(file_path, 'r') as file:
            print(f"Opening {file_path}...\n")
        
        # Run the Python file
        result = subprocess.run([sys.executable, file_path], capture_output=True, text=True)
        print("Output:\n", result.stdout)
        print("Errors:\n", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = "kechup man game part 2.py"  # Replace with the path to your Python file
open_new_window_boss(file_path)
# Run the application
root.mainloop()
