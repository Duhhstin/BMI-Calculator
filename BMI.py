from tkinter import *
#Formula:
#BMI = weight * 703/(height * height)

#Calculate button
def calc_button():
    try:
        global popUpLabel
        weight_number = entryBoxWeight.get()
        height_number = entryBoxHeight.get()

        BMI_CONSTANT = 703
        weight = float(weight_number)
        height = float(height_number)
        bmi = weight * BMI_CONSTANT/(height * height)

        entryBoxBMI.delete(0, END)
        entryBoxBMI.insert(0, float(format(bmi, ",.2f")))

        #If statement used to control labels
        if bmi >= 18.5 and bmi <= 25.0:
            popUpLabel = Label(root, text="Your BMI is OPTIMAL!")
            popUpLabel.grid(row=4, column=1, columnspan=1)
        elif bmi < 18.5:
            popUpLabel = Label(root, text="You are UNDERWEIGHT!")
            popUpLabel.grid(row=4, column=1, columnspan=1)
        else:
            popUpLabel = Label(root, text="Your are OVERWEIGHT!")
            popUpLabel.grid(row=4, column=1, columnspan=1)

        button_calc["state"] = DISABLED
        button_clear["state"] = NORMAL

    except:
        print("User must enter values.")

#Clear button
def clear_button():
    entryBoxWeight.delete(0, END)
    entryBoxHeight.delete(0, END)
    entryBoxBMI.delete(0, END)
    popUpLabel.grid_forget()
    button_calc["state"] = NORMAL
    button_clear["state"] = DISABLED

root = Tk()
root.title("BMI Calculator")

#Labels
titleLabel = Label(text="BMI Calculator")
titleLabel.grid(row=0, column=1, columnspan=2)

firstLabel = Label(text="Weight: ")
secondLabel = Label(text="Height(inches): ")
thirdLabel = Label(text="BMI: ")

#Pop up placeholder
popUpLabel = Label(root, text="")
popUpLabel.grid(row=4, column=1, columnspan=3)

#Place Labels
firstLabel.grid(row=1, column=0)
secondLabel.grid(row=2, column=0)
thirdLabel.grid(row=3, column=0)

#Entry box
entryBoxWeight = Entry(root, width=30, borderwidth=5)
entryBoxWeight.grid(row=1, column=1, columnspan=3)

entryBoxHeight = Entry(root, width=30, borderwidth=5)
entryBoxHeight.grid(row=2, column=1, columnspan=3)

entryBoxBMI = Entry(root, width=30, borderwidth=5)
entryBoxBMI.grid(row=3, column=1, columnspan=5)

#Buttons
button_calc = Button(root, text="Calculate", padx=20, pady=20, command=calc_button)
button_clear = Button(root, text="Clear", padx=35, pady=20, command=clear_button)
button_clear["state"] = DISABLED

#Place Buttons
button_calc.grid(row=5, column=0)
button_clear.grid(row=5, column=3)

root.mainloop()