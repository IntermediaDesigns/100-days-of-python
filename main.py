import os
import tkinter as tk

from PIL import Image, ImageTk


class VisualNovel:

    def __init__(self, master):
        self.master = master
        self.master.title("The forgotten Locket")
        self.master.geometry("800x800")

        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.image_label = tk.Label(self.frame)
        self.image_label.pack()

        self.text_label = tk.Label(self.frame,
                                   wraplength=700,
                                   font=("Arial", 12))
        self.text_label.pack(pady=20)

        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack()

        self.load_images()
        self.intro()

    def load_images(self):
        image_folder = "story"

        self.images = {
            "intro":
            ImageTk.PhotoImage(
                Image.open(os.path.join(image_folder, "intro.jpg"))),
            "scene1":
            ImageTk.PhotoImage(
                Image.open(os.path.join(image_folder, "scene1.jpg"))),
            "locket":
            ImageTk.PhotoImage(
                Image.open(os.path.join(image_folder, "locket.jpg"))),
            "alone":
            ImageTk.PhotoImage(
                Image.open(os.path.join(image_folder, "alone.jpg"))),
            "love":
            ImageTk.PhotoImage(
                Image.open(os.path.join(image_folder, "love.jpg"))),
            "choice":
            ImageTk.PhotoImage(
                Image.open(os.path.join(image_folder, "choice.jpg"))),
            "oldLife":
            ImageTk.PhotoImage(
                Image.open(os.path.join(image_folder, "oldLife.jpg"))),
            "newLife":
            ImageTk.PhotoImage(
                Image.open(os.path.join(image_folder, "newLife.jpg"))),
            "tree":
            ImageTk.PhotoImage(
                Image.open(os.path.join(image_folder, "tree.jpg"))),
        }

        global image_files
        image_files = {
            "intro": "intro.jpg",
            "start": "scene1.jpg",
            "locket": "locket.jpg",
            "alone": "alone.jpg",
            "love": "love.jpg",
            "choice": "choice.jpg",
            "oldLife": "oldLife.jpg",
            "newLife": "newLife.jpg",
            "tree": "tree.jpg",
        }
        for key, filename in image_files.items():
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            image = image.resize((700, 500), Image.Resampling.LANCZOS)
            self.images[key] = ImageTk.PhotoImage(image)

    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def intro(self):
        self.image_label.config(image=self.images["intro"])
        self.text_label.config(
            text=
            "Welcome to The forgotten Locket, a visual novel that begins in a quaint town of Willowbrook, nestled among ancient oak trees, where lies a mysterious legend.\n\n It is said that hidden deep within the forest, there exists an enchanted locket—a relic of forgotten love.\n\n The townspeople speak of its magical powers: whoever wears it will be granted a single wish, but at a great cost.\n\n Are you ready to begin?"
        )
        self.clear_buttons()
        tk.Button(self.button_frame, text="Start",
                  command=self.start_page).pack()

    def start_page(self):
        self.image_label.config(image=self.images["start"])
        self.text_label.config(
            text=
            "Evelyn Hart, a young artist struggling to find inspiration. She stumbles upon the legend during a late-night walk through the moonlit woods. Drawn by curiosity, she discovers the locket half-buried in the damp earth."
        )
        self.clear_buttons()
        tk.Button(self.button_frame,
                  text="Put on locket.",
                  command=self.pickup_path).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame,
                  text="Leave it there.",
                  command=self.oldLife_path).pack(side=tk.LEFT, padx=10)

    def pickup_path(self):
        self.image_label.config(image=self.images["locket"])
        self.text_label.config(
            text=
            "Evelyn’s life takes an unexpected turn when she puts on the locket. Her wish—to become a renowned painter—comes true, but her memories start fading. She forgets her childhood, her family, and even her dearest friend, Lucas, who lives next door."
        )
        self.clear_buttons()
        tk.Button(self.button_frame,
                  text="Go for fame",
                  command=self.newLife_path).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame,
                  text="Take off locket",
                  command=self.oldLife_path).pack(side=tk.LEFT, padx=10)

    def newLife_path(self):
        self.image_label.config(image=self.images["newLife"])
        self.text_label.config(
            text=
            "As Evelyn’s fame grows, so does her loneliness. She paints masterpieces but feels an emptiness inside. Lucas, worried about her sudden transformation, investigates the locket’s origins. He uncovers a tragic love story from centuries ago—the tale of Isabella and Gabriel."
        )
        self.clear_buttons()
        tk.Button(self.button_frame,
                  text="Life continues",
                  command=self.lifeContinues_path).pack(side=tk.LEFT, padx=10)

    def oldLife_path(self):
        self.image_label.config(image=self.images["oldLife"])
        self.text_label.config(
            text=
            "Evelyn’s life continues making memories and becomming more aquainted with Lucas. She continues to look for inspiration and creating masterpieces but something inside keeps thinking about the locket."
        )
        self.clear_buttons()
        tk.Button(self.button_frame,
                  text="Return to forest",
                  command=self.backToForest_path).pack(side=tk.LEFT, padx=10)

    def backToForest_path(self):
        self.image_label.config(image=self.images["start"])
        self.text_label.config(
            text="Evelyn returns to the forest and picks up the locket...")
        self.clear_buttons()
        tk.Button(self.button_frame,
                  text="Put on locket.",
                  command=self.pickup_path).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame,
                  text="Leave it there.",
                  command=self.oldLife_path).pack(side=tk.LEFT, padx=10)

    def lifeContinues_path(self):
        self.image_label.config(image=self.images["tree"])
        self.text_label.config(
            text=
            "Lucas asks Evelyn to meet in the forest to discuss the locket’s origins. She agrees and they head to the forest together. Evelyn and Lucas embark on a quest to reverse the locket’s effects. They follow cryptic clues, retracing Isabella and Gabriel’s steps.\n\n Along the way, they fall in love themselves, but the locket threatens to erase their memories too.\n\n They find themselves at a tree with carvings of Isabella and Gabriel's initials.\n\n The locket is inscribed with the words: 'I am the locket, and I am the key to your destiny..."
        )
        self.clear_buttons()
        tk.Button(self.button_frame,
                  text="Your destiny...",
                  command=self.which_end).pack(side=tk.LEFT, padx=10)

    def which_end(self):
        self.image_label.config(image=self.images["choice"])
        self.text_label.config(
            text=
            "In a moonlit clearing, Evelyn faces a choice: keep her newfound talent and forget Lucas, or break the curse and lose her artistry.\n\n What will she choose?"
        )
        self.clear_buttons()
        tk.Button(self.button_frame, text="Keep Fame",
                  command=self.bad_ending).pack(side=tk.LEFT, padx=10)

        tk.Button(self.button_frame,
                  text="Break Curse",
                  command=self.good_ending).pack(side=tk.LEFT, padx=10)

    def good_ending(self):
        self.image_label.config(image=self.images["love"])
        self.text_label.config(
            text=
            "She decides to honor Isabella’s sacrifice.\n\n As the locket dissolves, memories flood back—the pain, the joy, and her love for Lucas. Evelyn’s life becomes a story of resilience, friendship, and the power of love."
        )
        self.clear_buttons()
        tk.Button(self.button_frame,
                  text="Start Again",
                  command=self.start_page).pack()

    def bad_ending(self):
        self.image_label.config(image=self.images["alone"])
        self.text_label.config(
            text=
            "She decides to keep the fame, the locket dissolves and her love for Lucas is lost forever.\n\n Evelyn’s life is lonely and unfulfilled, but she knows that her talent will always be remembered."
        )
        self.clear_buttons()
        tk.Button(self.button_frame,
                  text="Start Again",
                  command=self.start_page).pack()


root = tk.Tk()
game = VisualNovel(root)
root.mainloop()
