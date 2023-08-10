from tkinter import *
from tkinter import messagebox
import requests

def run():

    end_currency = str(entry1.get()).upper()
    #Making the abbreviation upper case due to the fact that the Franckfurt API only accepts Upper case.

    intial_currency = str(entry2.get()).upper()

    value = float(entry3.get())
    #float(input("Enter in the amount of money you would like to convert: "))

    feedback = requests.get(f"https://api.frankfurter.app/latest?amount={value}&from={intial_currency}&to={end_currency}")
    code = "Status Code: ",feedback.status_code
    result = f"{value} {intial_currency} is {feedback.json()['rates'][end_currency]} {end_currency}" #The "feedback.json" will return a json object for the request
    display = code, "\n", result
    #If it returns 200 it means all has worked well
    messagebox.showinfo(title="Conversion",message=display)

window = Tk()

label1 = Label(window,
               text="Enter the currency abbreviation for the currency you would like to convert to: ",
               font=("Arial", 20)
               )
label1.pack()

entry1 = Entry(window,
              font=("Arial",35))
entry1.pack()

label2 = Label(window,text="Enter the currency abbreviation for the currency you would like to convert from: ",
              font=("Arial",20))
label2.pack()

entry2 = Entry(window,
              font=("Arial",35))
entry2.pack()

label3 = Label(window,text="Enter in the amount of money you would like to convert: ",
              font=("Arial",20))
label3.pack()

entry3 = Entry(window,
              font=("Arial",35))
entry3.pack()
button = Button(window,
                text="CONVERT",
                command=run)
button.pack(side=BOTTOM)
window.mainloop()
