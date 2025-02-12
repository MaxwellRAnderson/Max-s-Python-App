import tkinter as tk
from tkinter import messagebox

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
        self.hit_delay = 200  # Decreased delay to 200 ms (0.2 seconds)
        self.hit_timer = None

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
            messagebox.showinfo("Game Over", f"{self.color.capitalize()} Man is defeated!")

    #find out what this does
    def start_hit_timer(self, target):
        if self.hit_timer is None:
            self.hit_timer = self.canvas.after(self.hit_delay, self.deal_damage, target)

    def deal_damage(self, target):
        target.take_damage(50)  # Increased damage to 50 per hit
        self.hit_timer = None
        if target.health > 0:
            self.start_hit_timer(target)

def move_ketchup(event, canvas):
    dx, dy = 0, 0
    if event.keysym == "Left":
        dx = -10
    elif event.keysym == "Right":
        dx = 10
    elif event.keysym == "Up":
        dy = -10
    elif event.keysym == "Down":
        dy = 10
    ketchup.move(dx, dy)
    check_collision()

def check_collision():
    ketchup_coords = ketchup.get_coords()
    mustard_coords = mustard.get_coords()
    #find out what this does
    if ketchup_coords[0] < mustard_coords[2] and ketchup_coords[2] > mustard_coords[0] and \
       ketchup_coords[1] < mustard_coords[3] and ketchup_coords[3] > mustard_coords[1]:
        canvas.create_text(300, 20, text="Phase 1: Mustard Man hits Ketchup Man!", fill="red")
        #find out what this does
        mustard.start_hit_timer(ketchup)
    else:
        if mustard.hit_timer is not None:
            canvas.after_cancel(mustard.hit_timer)
            mustard.hit_timer = None

def on_space_press(event):
    ketchup_coords = ketchup.get_coords()
    mustard_coords = mustard.get_coords()
    if ketchup_coords[0] < mustard_coords[2] and ketchup_coords[2] > mustard_coords[0] and \
       ketchup_coords[1] < mustard_coords[3] and ketchup_coords[3] > mustard_coords[1]:
        mustard.take_damage(20)

def move_mustard():
    dx, dy = 0, 0
    if mustard.x < ketchup.x:
        dx = 5
    elif mustard.x > ketchup.x:
        dx = -5
    if mustard.y < ketchup.y:
        dy = 5
    elif mustard.y > ketchup.y:
        dy = -5
    mustard.move(dx, dy)
    check_collision()
    if mustard.health > 0:
        canvas.after(50, move_mustard)

# Create the main window
root = tk.Tk()
root.title("Ketchup Man vs Mustard Man")

canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# Initialize Ketchup Man and Mustard Man
ketchup = Character(canvas, 50, 200, 100, "red")
mustard = Character(canvas, 300, 200, 200, "yellow")

root.bind("<KeyPress>", lambda event: move_ketchup(event, canvas))
root.bind("<space>", on_space_press)

move_mustard()

root.mainloop()
