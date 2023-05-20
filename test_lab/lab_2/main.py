from tkinter import *
from functools import partial
from CalcPresenter import CalcPres


def main_calc():
    root = Tk()
    root.title('Calculator')
    root.geometry("600x250+450+230")

    label_result = Label(font=("Arial", 14))
    label_result.pack(anchor=NW, padx=6, pady=6)
    label_result.place(x=120, y=155)
    calc = CalcPres(label_result)
    label_result["text"] = 'Ответ: '

    entry = Entry(width=23, font=("Arial", 14))
    entry.pack(anchor=NW, padx=6, pady=6)
    entry.place(x=35, y=30)
    entry2 = Entry(width=23, font=("Arial", 14))
    entry2.pack(anchor=NW, padx=6, pady=6)
    entry2.place(x=320, y=30)

    btn = Button(text="+", font=("Arial", 12), command=partial(calc.onPlusClicked, entry, entry2), width=7)
    btn.pack(anchor=NW, padx=7, pady=7)
    btn.place(x=35, y=80)

    btn1 = Button(text="-", font=("Arial", 12), command=partial(calc.onMinusClicked, entry, entry2), width=7)
    btn1.pack(anchor=NW, padx=7, pady=7)
    btn1.place(x=185, y=80)

    btn2 = Button(text='x', font=("Arial", 12), command=partial(calc.onMultiplyClicked, entry, entry2), width=7)
    btn2.pack(anchor=NW, padx=7, pady=7)
    btn2.place(x=335, y=80)

    btn3 = Button(text='/', font=("Arial", 12), command=partial(calc.onDivideClicked, entry, entry2), width=7)
    btn3.pack(anchor=NW, padx=7, pady=7)
    btn3.place(x=485, y=80)

    root.mainloop()


main_calc()
