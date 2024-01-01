from tkinter import *


def salaryCal():
    Divi_Var = selectedDayDivVar.get()

    salary_input = textBoxSalary.get()
    textBox1pow_input = textBox1pow.get() if textBox1pow.get() else 0
    textBox2pow_input = textBox2pow.get() if textBox2pow.get() else 0
    textBox3pow_input = textBox3pow.get() if textBox3pow.get() else 0

    if salary_input:
        try:
            SalaryPerDay = float(salary_input) / (float(Divi_Var) * 8)
            Result1pow = float(SalaryPerDay) * 1.5 * float(textBox1pow_input)
            Result2pow = float(SalaryPerDay) * 2 * float(textBox2pow_input)
            Result3pow = float(SalaryPerDay) * 3 * float(textBox3pow_input)
            TotalIncome = float(Result3pow + Result2pow + Result1pow)
            labelResult.configure(text='%.2f' % TotalIncome)
            label1powTotal.configure(text='%.2f' % Result1pow)
            label2powTotal.configure(text='%.2f' % Result2pow)
            label3powTotal.configure(text='%.2f' % Result3pow)
        except ValueError:
            labelResult.configure(text="กรุณากรอกข้อมูลที่ถูกต้อง")
    else:
        labelResult.configure(text="โปรดกรอกเงินเดือน")




mainWindow = Tk()

labelTitle = Label(mainWindow, text="Overtime Calculation", font=30, anchor=E)
labelTitle.grid(row=0, column=0)

labelSalary = Label(mainWindow, text="เงินเดือน", font=18)
labelSalary.grid(row=1, column=0)

textBoxSalary = Entry(mainWindow, font=18, justify='center')
textBoxSalary.grid(row=1, column=1)

label1pow = Label(mainWindow, text="1.5 แรง (ชม.)", font=18)
label1pow.grid(row=2, column=0)
textBox1pow = Entry(mainWindow, font=18, justify='center')
textBox1pow.grid(row=2, column=1)

label2pow = Label(mainWindow, text="2 แรง (ชม.)", font=18)
label2pow.grid(row=3, column=0)
textBox2pow = Entry(mainWindow, font=18, justify='center')
textBox2pow.grid(row=3, column=1)

label3pow = Label(mainWindow, text="3 แรง (ชม.)", font=18)
label3pow.grid(row=4, column=0)
textBox3pow = Entry(mainWindow, font=18, justify='center')
textBox3pow.grid(row=4, column=1)

# ใช้ IntVar เพื่อเก็บค่าของ Radiobutton
selectedDayDivVar = IntVar()

labelResult = Label(mainWindow, text="จำนวน วันหาร OT", font=18)
labelResult.grid(row=5)
DayDivind22 = Radiobutton(mainWindow, text="22 วัน", font=18, variable=selectedDayDivVar, value=22)
DayDivind22.grid(row=5, column=1)
DayDivind22.select()

DayDivind30 = Radiobutton(mainWindow, text="30 วัน", font=18, variable=selectedDayDivVar, value=30)
DayDivind30.grid(row=6, column=1)

labelResult = Label(mainWindow, text="รายรับค่าล่วงเวลาทั้งหมด", font=18)
labelResult.grid(row=7, column=1)
label1powTotal = Label(mainWindow, text=" ", font=18)
label1powTotal.grid(row=2, column=2)
label2powTotal = Label(mainWindow, text=" ", font=18)
label2powTotal.grid(row=3, column=2)
label3powTotal = Label(mainWindow, text=" ", font=18)
label3powTotal.grid(row=4, column=2)

CalButton = Button(mainWindow, text="คำนวณ", font=18, command=salaryCal)
CalButton.grid(row=7, column=0)

mainWindow.mainloop()
