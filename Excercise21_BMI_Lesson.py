from tkinter import *

def leftClickButton(event):
    Weight = int(textboxWeight.get())
    Height = int(textboxHeight.get())
    result = (Weight/((Height/100)**2))
    return BMIresult(result)

def BMIresult(level):
    if level >= 30:
        labelResult.configure(text="อ้วนเกินไป")
    elif level >= 25 <=29.0:
        labelResult.configure(text="อ้วน")
    elif level >= 23 <=24.9:
        labelResult.configure(text="น้ำหนักเกิน")
    elif level >= 18.6 <=22.9:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif level <= 18.5:
        labelResult.configure(text="ผอมเกินไป")
    else:
        labelResult.configure(text="Error")

mainWindow = Tk()
labelHeight = Label(mainWindow,text="ส่วนสูง (ซม.)")
labelHeight.grid(row=0,column=0)
textboxHeight = Entry(mainWindow)
textboxHeight.grid(row=0,column=1)

labelWeight = Label(mainWindow,text="น้ำหนัก (กก.)")
labelWeight.grid(row=1,column=0)
textboxWeight = Entry(mainWindow)
textboxWeight.grid(row=1,column=1)

labelResult = Label(mainWindow,text="BMI : ")
labelResult.grid(row=2,column=1)

CalculateButton = Button(mainWindow,text = "Calcurate")
CalculateButton.bind('<Button-1>',leftClickButton)
CalculateButton.grid(row=2)

mainWindow.mainloop()