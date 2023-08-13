from tkinter import *

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do-list Application")
        self.root.geometry("650x410+300+150")

        self.label = Label(self.root, text="ToDo-List",font="Comic, 25  bold", width=8, bd=5, bg="light blue", fg="black" )
        self.label.pack(side="left", fill=BOTH)

        self.label2 = Label(self.root, text="Add Tasks",font="comic, 18 bold", width=10, bd=5, bg="white", fg="black" )
        self.label2.place(x=200, y=54)

        self.label3 = Label(self.root, text="Tasks",font="comic, 18 bold", width=10, bd=5, bg="white", fg="black" )
        self.label3.place(x=470, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="arial, 20 bold")
        self.main_text.place(x=400, y=100)

        self.text = Text(self.root, bd=5, height=2, width=20, font="arial, 12 bold")

        self.text.place(x=190, y=120)

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open("data.txt", "a") as file:

                
                file.write(content)
                file.seek(0)

                file.close()
            self.text.delete(1.0, END)
        
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open("data.txt", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open("data.txt", "r") as file:

            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        
        self.button = Button(self.root, text="Add", font="comic, 18 ", width=10, bd=5, bg="sky blue", fg="black", command=add)
        self.button.place(x=200, y=200)

        self.button2 = Button(self.root, text="Delete", font="comic, 18 ", width=10, bd=5, bg="sky blue", fg="black", command=delete)
        self.button2.place(x=200, y=290)

        
def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
        

    