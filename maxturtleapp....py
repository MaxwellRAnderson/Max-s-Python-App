import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
import os
import turtle

def close_all_windows():
    root.quit()





def open_log_out_window():
    logout_window = tk.Toplevel(root)
    logout_window.title("Logout Window")
    tk.Label(logout_window, text="Username").pack(pady=5)
    logout_username_entry = tk.Entry(logout_window)
    logout_username_entry.pack(pady=5)
    tk.Label(logout_window, text="Password").pack(pady=5)
    logout_password_entry = tk.Entry(logout_window, show="*")
    logout_password_entry.pack(pady=5)
    tk.Button(logout_window, text="Log Out", command=close_all_windows).pack(pady=20)

def open_notebook():
    notebook_window = tk.Toplevel(root)
    notebook_window.title("Notebook")

    text_area = tk.Text(notebook_window, wrap='word')
    text_area.pack(expand='yes', fill='both')

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))

    def open_file():
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())

    open_button = tk.Button(notebook_window, text="Open", command=open_file)
    open_button.pack(pady=10)

    save_button = tk.Button(notebook_window, text="Save", command=save_file)
    save_button.pack(pady=10)

    close_button = tk.Button(notebook_window, text="Close", command=notebook_window.destroy)
    close_button.pack(pady=10)

def open_drawing_window():
    drawing_window = tk.Toplevel(root)
    drawing_window.title("Drawing App")
    
    canvas = tk.Canvas(drawing_window, width=500, height=500, bg="white")
    canvas.pack()

    def choose_color():
        color = colorchooser.askcolor()[1]
        if color:
            canvas.color = color

    def draw_on_canvas(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        canvas.create_oval(x1, y1, x2, y2, fill=canvas.color, outline=canvas.color)

    def save_drawing():
        file_path = filedialog.asksaveasfilename(defaultextension=".ps", filetypes=[("PostScript Files", "*.ps")])
        if file_path:
            canvas.postscript(file=file_path)

    canvas.color = "black"  # Default color
    canvas.bind("<B1-Motion>", draw_on_canvas)

    color_button = tk.Button(drawing_window, text="Choose Color", command=choose_color)
    color_button.pack(pady=10)

    save_button = tk.Button(drawing_window, text="Save", command=save_drawing)
    save_button.pack(pady=10)

    close_button = tk.Button(drawing_window, text="Close", command=drawing_window.destroy)
    close_button.pack(pady=10)

def open_os_options_window():
    os_window = tk.Toplevel(root)
    os_window.title("OS Options")

    tk.Button(os_window, text="Shut Down", command=lambda: os.system("shutdown /s /f /t 0")).pack(pady=5)
    tk.Button(os_window, text="Sleep", command=lambda: os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")).pack(pady=5)
    tk.Button(os_window, text="Restart", command=lambda: os.system("shutdown /r /f /t 0")).pack(pady=5)
    tk.Button(os_window, text="Lock", command=lambda: os.system("shutdown /l")).pack(pady=5)
    tk.Button(os_window, text="Close", command=os_window.destroy).pack(pady=10)

def open_maxwell_account():
    maxwell_window = tk.Toplevel(root)
    maxwell_window.title("Maxwell's Account")
    tk.Label(maxwell_window, text="Welcome to your account, Maxwell!").pack(pady=20)
    tk.Button(maxwell_window, text="Notebook", command=open_notebook).pack(pady=10)
    tk.Button(maxwell_window, text="Drawing App", command=open_drawing_window).pack(pady=10)
    tk.Button(maxwell_window, text="OS", command=open_os_options_window).pack(pady=10)
    tk.Button(maxwell_window, text="OS", command=open_kechup_man).pack(pady=10)
    tk.Button(maxwell_window, text="Log Out", command=open_log_out_window).pack(pady=10)
    tk.Button(maxwell_window, text="Close", command=maxwell_window.destroy).pack(pady=10)

def open_rcsd_account():
    rcsd_window = tk.Toplevel(root)
    rcsd_window.title("RCSD Account")
    tk.Label(rcsd_window, text="Welcome to your account, RCSD!").pack(pady=20)
    tk.Button(rcsd_window, text="Notebook", command=open_notebook).pack(pady=10)
    tk.Button(rcsd_window, text="Drawing App", command=open_drawing_window).pack(pady=10)
    tk.Button(rcsd_window, text="OS", command=open_os_options_window).pack(pady=10)
    tk.Button(rcsd_window, text="Log Out", command=open_log_out_window).pack(pady=10)
    tk.Button(rcsd_window, text="Close", command=rcsd_window.destroy).pack(pady=10)


    

def open_kechup_man





def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check credentials
    if username == "maxwell.r.anderson" and password == "2015":
        messagebox.showinfo("Login", "Login successful!")
        open_maxwell_account()
    elif username == "max.anderson@rcsd.ca" and password == "2015":
        messagebox.showinfo("Login", "Login successful!")
        open_rcsd_account()
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login App")

# Create and place labels and entries for username and password
tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Run the application
root.mainloop()
