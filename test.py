import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
import os

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

def open_joke_app():
    joke_app_window = tk.Toplevel(root)
    joke_app_window.title("Joke App")

    def display_message():
        age = int(age_entry.get())
    
        if age <= 7:
            message = ("Are you a bit too young to be on the laptop?\n"
                       "And on coding?\n"
                       "I hope your parents are watching you!")
        elif age == 8:
            message = "What do you call a fish with no eyes? A fsh."
        elif age == 9:    
            message = "What do you say when you lose a Wii game? I want a Wii-match."
        elif age == 10:
            message = "Why was the snowman at the grocery store? He was picking his nose."
        elif age == 11:
            message = "How do you get a cat to code? You scratch it."
        elif age == 12:
            message = "What did mama cow say to baby cow? It's pasture bedtime."
        elif age == 13:
            message = "What did the fisherman say to the magician? Pick a cod, any cod."
        elif age == 14:
            message = "What did the janitor say when he jumped out of the closet? Supplies."
        elif age == 15:
            message = "Why are robots never afraid? They have nerves of steel."
        elif age == 16:
            message = "How do you make a tissue dance? Put a little boogie in it."
        elif age == 17:
            message = "How do pickles enjoy a day out? They relish it."
        elif age == 18:
            message = "If athletes get athlete's foot, what do astronauts get? Missile toe."
        elif age >= 19 and age <= 24:
            message = ("You're too old for normal jokes!\n"
                       "So you get knock knock jokes! Age 19 to 24\n"
                       "Knock knock\n"
                       "Who's there?\n")
            if age == 19:
                message += "Pilipe\nPilipe who?\nPilipe the car, we're out of gas!"
            elif age == 20:
                message += "Cookie\nCookie who?\nCookie quit now and I have to make all the food!"
            elif age == 21:
                message += "Dee\nDee who?\nDee-licious!"
            elif age == 22:
                message += "Anna\nAnna who?\nAnna one, Anna two, Anna three!"
            elif age == 23:
                message += "Harry\nHarry who?\nHarry up and answer the door!"
            elif age == 24:
                message += "Cow\nCow who?\nCow much longer are you going to put up with all his knocking?"
        elif age >= 25 and age <= 30:
            message = ("You're too old for jokes!\n"
                       "So you get riddles! Age 25 to 30\n")
            if age == 25:
                message += "What has keys but can't open locks?\nA piano."
            elif age == 26:
                message += "I have no blood pumping through me but I have 4 fingers and 1 thumb. What am I?\nA glove."
            elif age == 27:
                message += "What is as big as an elephant but weighs nothing?\nAn elephant's shadow."
            elif age == 28:
                message += "I have wings and a tail. Across the sky is where I sail. Yet I have no eyes, ears, or mouth. What am I?\nA kite."   
            elif age == 29:
                message += "What has a neck but no head, two arms but no hands?\nA shirt."
            elif age == 30:
                message += "Make the number 1 disappear.\nAdd the letter G and it's gone."
        elif age >= 31 and age <= 39:
            message = ("You're too old for jokes and riddles!\n"
                       "So you get tongue twisters! Age 31 to 39\n")
            if age == 31:
                message += "She sells seashells by the seashore."
            elif age == 32:
                message += "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
            elif age == 33:
                message += "Two to two Toulouse."
            elif age == 34:
                message += "Peter Piper picked a peck of pickled peppers."
            elif age == 35:
                message += "How can a clam cram in a clean cream can?"
            elif age == 36:
                message += "If practice makes perfect and perfect needs practice, I'm perfectly practiced and practically perfect."
            elif age == 37:
                message += "Tim, the thin twin tinsmith."
            elif age == 38:
                message += "Tim the thin twin tinsmith's twin brother."
            elif age == 39:
                message += "Did Doug dig David's garden or did David dig Doug's garden?"
        elif age >= 40 and age <= 60:      
            num1 = int(input("Pick any number: "))
            num2 = int(input("Pick another number: "))
            answer = int(input(f"What is {num1} + {num2}? "))
            correct_answer = num1 + num2
            if answer == correct_answer:
                message = "Correct!"
            else:
                message = f"Wrong! The correct answer is {correct_answer}"
        elif age >= 61 and age <= 100:
            message = ("You're too old for jokes, riddles, tongue twisters, and math problems.\n"
                       "So you get a story! Age 61 to 100\n"
                       "Once upon a time in a small village, there lived an old man.\n"
                       "He was known for his wisdom and kindness. Every day, he would sit under a large oak tree and share stories with the children of the village.\n"
                       "One day, a young boy asked him, 'What is the secret to a happy life?'\n"
                       "The old man smiled and said, 'The secret to a happy life is to always be kind, to always be curious, and to always find joy in the little things.'\n"
                       "The boy thought about this for a moment and then asked, 'But how do I do that?'\n"
                       "The old man replied, 'By treating others with respect, by always asking questions and seeking knowledge, and by appreciating the beauty of the world around you.'\n"
                       "The boy nodded and thanked the old man for his wisdom. From that day on, he tried to live by the old man's advice, and he found that his life was indeed much happier.\n"
                       "The end.\nI hope you enjoyed the story!")
        else:
            message = (f"Are you too old to be alive?\n"
                       f"You are {age} years old.\n"
                       "I hope you are not dead!\n"
                       "If you are, I am sorry for your loss.\n"
                       "Plus then you are a ghost!\n"
                       "Ah! A ghost!")
    
        messagebox.showinfo("Message", message)

# Create the main window
root = tk.Tk()
root.title("Age-based Messages")

# Create and place label and entry for age
tk.Label(root, text="Enter your age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

# Create and place the button to display message
show_message_button = tk.Button(root, text="Show Message", command=display_message)
show_message_button.pack(pady=20)

# Run the application
root.mainloop()
