import tkinter as tk
class Window():
    def __init__(self,root):
        self.root = root
        self.root.title('Hello Tkinter')
        self.root.label_text = 'Choose One'
        self.root.label = tk.Label(self, text=self.label_text)
        self.root.label.pack(fill=tk.BOLL, expand=1, padx=100, pady=30)
        
        hello_btn = tk.Button(self, text='say hello', command=self.root.say_hello)
        hello_btn.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        goodbye_button = tk.Button(self, text="Say Goodbye",
        command=self.root.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
    def say_hello(self):
        self.root.label.configure(text="Hello World!")
    def say_goodbye(self):
        self.root.label.configure(text="Goodbye! \n (Closing in 2 seconds)")
        self.root.after(2000, self.destroy)
root = tk.Tk()
window = Window(root)
root.mainloop()