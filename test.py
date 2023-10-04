import math

###

#!/usr/bin/env python 
import tkinter as tk 
class Application(tk.Frame): 
    def __init__(self, master=None):
        tk.Frame.__init__(self, master) 
        self.grid() 
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit) 
        self.quitButton.grid() 

app = Application() 
app.master.title('Sample application') 
app.mainloop()

# #!/usr/bin/env python
# import tkinter as tk

# class Example(tk.Frame):
#     def __init__(self, parent):
#         tk.Frame.__init__(self, parent)

#         # create a prompt, an input box, an output label,
#         # and a button to do the computation
#         self.prompt = tk.Label(self, text="Enter a number:", anchor="w")
#         self.entry = tk.Entry(self)
#         self.submit = tk.Button(self, text="Submit", command = self.calculate)
#         self.output = tk.Label(self, text="")

#         # lay the widgets out on the screen. 
#         self.prompt.pack(side="top", fill="x")
#         self.entry.pack(side="top", fill="x", padx=20)
#         self.output.pack(side="top", fill="x", expand=True)
#         self.submit.pack(side="right")

#     def calculate(self):
#         # get the value from the input widget, convert
#         # it to an int, and do a calculation
#         try:
#             i = int(self.entry.get())
#             result = "%s*2=%s" % (i, i*2)
#         except ValueError:
#             result = "Please enter digits only"

#         # set the output widget to have our result
#         self.output.configure(text=result)

# # if this is run as a program (versus being imported),
# # create a root window and an instance of our example,
# # then start the event loop

# if __name__ == "__main__":
#     root = tk.Tk()
#     Example(root).pack(fill="both", expand=True)
#     root.mainloop()
###

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - 4*a*c

print(delta)

if delta<0:
    print("Não existem raízes reais")

else:
    print("Existem raízes reais")
    x1= (-b+math.sqrt(delta))/(2*a)*(-1)
    x2= (-b-math.sqrt(delta))/(2*a)*(-1)

    print("X1 = ",x1)
    print("X2 = ",x2)