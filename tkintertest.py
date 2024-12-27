import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("200x200")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

options = ["Apple", "Orange", "Grape"]
selected_option = tk.StringVar()
selected_option.set(options[0])

dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack()

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup")
    popup.geometry("100x100")
    label = tk.Label(popup, text="😊")
    label.pack()

button = tk.Button(root, text="Go", command=show_popup)
button.pack()

root.mainloop()
