import tkinter as tk
import math

def on_click(event):
    current_text = display.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result=eval(current_text)
            display.set(result)
        except Exception as e:
            display.set("Error")
    elif button_text == "c":
        display.set("")
    elif button_text == "√":
        try:
            result =math.sqrt(float(current_text))
            display.set(result)
        except Exception as e:
            display.set("Error")
    elif button_text == "x!":
        try:
            result=math.factorial(int(current_text))
            display.set(result)
        except Exception as e:
            display.set("Error")
    else:
        display.set(current_text+button_text)

window=tk.Tk()
window.title("CALCULATOR")
window.geometry("340x440")
window.configure(bg="black")

heading_label=tk.Label(window,text="Calculator",font=("Arial",20,"bold"),pady=10)
heading_label.pack()

display=tk.StringVar()
display.set("")
display_entry=tk.Entry(window,textvariable=display,font=("Arial",20,),bd=5,relief=tk.RIDGE,justify=tk.RIGHT)
display_entry.pack(fill=tk.BOTH,padx=10,pady=10,ipadx=5,ipady=5)

button_frame=tk.Frame(window)
button_frame.pack()

button=[
    ('7','8','9','/','√'),
    ('4','5','6','*', 'x!'),
    ('1','2','3','-', 'c'),
    ('0', '.','%','+', '=')
]
for i,row in enumerate(button):
    for j,text in enumerate(row):
        button=tk.Button(button_frame,text=text,font=("Arial",15,"bold"),padx=10,pady=10,bd=5,relief=tk.RIDGE)
        button.grid(row=i,column=j,padx=5,pady=5,sticky="nsew")
        button.bind("<Button-1>",on_click)

button_frame.columnconfigure(4,weight=1)
button_frame.rowconfigure(4,weight=1)

window.mainloop()
