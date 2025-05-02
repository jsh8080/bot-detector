import tkinter as tk
import AiChatBotTest as ai
import comment_scraper_test as cs

class Bot_gui:


    def __init__(self):
        
        self.root = tk.Tk()
        #self.root.geometry("400x700")
        self.root.title("Bot Blaster")

        self.name = tk.Label(self.root, font = ("Arial", 16), text = "Bot Blaster")
        self.name.grid(column = 0, row = 0, columnspan = 2, padx = 100)

        self.action = tk.Button(text = "initiate", font = ("Arial",12), command = self.execute)
        self.action.grid(column = 0, row = 1, padx = 50)

        self.vid_input = tk.Entry(font = ("Arial",12))
        self.vid_input.grid(column = 1, row = 1, padx = 50)

        self.comments = tk.Text(font = ("Arial",14))
        self.comments.grid(column = 0, row = 2, columnspan = 2, padx= 50)

        self.root.mainloop()

    def execute(self):
        pass
        try:
            self.comments.delete("1.0","end")
            cs.get_comments(self.vid_input.get())
            self.comments.insert("1.0", ai.make_request())
        except:
            print("unable to execute, check for valid video id")

Bot_gui()