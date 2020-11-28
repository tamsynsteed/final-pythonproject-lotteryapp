from tkinter import *
from tkinter import simpledialog ,messagebox

#create main window and style it. Add a title, sizing etc
window=Tk()
window.title("Lottery Entry")
window.configure(background="#e84e17", relief="solid")
window.geometry("650x650")
import random
userNumbers = set()
#we want the user to input 6 numbers as integers
def user_list():
    userNumbers = set()
    try:
        number1 = int(entry1.get())
        userNumbers.add(number1)

        number2 = int(entry2.get())
        userNumbers.add(number2)

        number3 = int(entry3.get())
        userNumbers.add(number3)

        number4 = int(entry4.get())
        userNumbers.add(number4)

        number5 = int(entry5.get())
        userNumbers.add(number5)

        number6 = int(entry6.get())
        userNumbers.add(number6)


    except ValueError: #this raises an error if the entries are not integers

        messagebox.showerror("Invalid Entries", "Please check for duplicates or empty textboxes.\n\nEnsure that all entries are numerical values.")
        userNumbers=(0)


    for i in userNumbers:
        if i > 49:
            messagebox.showerror("Invalid Entry", "Numbers cannot be greater than 49")


    else:
         label3.config(text=str("These are your chosen numbers:\n"+str(userNumbers)))


def lotto_numbers(): #generates 6 random numbers
    lot_num = set()

    for i in range(0,6):
      number1 = random.randint(1,49)

      while number1 in lot_num: #loop to ensures all numbers are unique
          number1 = random.randint(1,49)

      lot_num.add(number1)

    label4.config(text=str("The Lottery numbers are:\n"+str(lot_num)))

    counter= 0
#compares the two sets
    for number in userNumbers:
        if number in lot_num:
            counter +=1 #for each number from the userNUmbers, if the number is in the lottery list, the counter will increment by 1.
        label5.config(text=str("You guessed:" + str(counter) + " number(s) correctly."))

    if counter == 6:
        messagebox.showinfo("Congratulations! You are our WINNER!! You have won R10 000!!!")

        file=open('/home/user/Desktop/lotto.txt','a') #appends this to the txt file
        file.write("\n"+"Amount Payable: You have won R 10 000")
        file.close()

    elif counter ==5:

        messagebox.showinfo("Congrtaulations! You have won R 8,584.00")

        file=open('/home/user/Desktop/lotto.txt','a')
        file.write("\n"+"Amount Payable: You have won R 8,584.00")
        file.close()

    elif counter ==4:

        messagebox.showinfo("Congrtaulations! You have won R 2,384.00")

        file=open('/home/user/Desktop/lotto.txt','a')
        file.write("\n"+"Amount Payable: You have won R 2,384.00")
        file.close()

    elif counter ==3:

        messagebox.showinfo("Thank you for playing","You have won R 100.50")

        file=open('/home/user/Desktop/lotto.txt','a')
        file.write("\n"+"Amount Payable: You have won R100.50")
        file.close()

    elif counter ==2:

        messagebox.showinfo("Thank you for playing","You have won R 20")
        file=open('/home/user/Desktop/lotto.txt','a')
        file.write("\n"+"Amount Payable:You have won R20.")
        file.close()

    elif counter <=1:
        messagebox.showinfo("Thank you for playing","You have not won anything.")
        file=open('/home/user/Desktop/lotto.txt','a')
        file.write("\n"+"Amount Payable: You have not won anything.")

        file.close()

        label5.config(text=str("You guessed:" + str(counter) + " number(s) correctly\nThank you for playing!"))


def clear_function(): #clears the entries
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)



def close_window(): #closes the window
    sure = messagebox.askyesno(title="Alert",message="Are you sure you want to exit this app?")
    if sure==True:
        window.destroy()
    else:
        return  None


#created labels and entry boxes and buttons

labelHeading = Label(window,text="National Lottery | Play", font="arial 18 bold", bg="yellow")
labelHeading.pack()

label1=Label(window, text="Please enter 6 unique numbers between 1 - 49 below:", font="arial 14 bold")
label1.pack(pady=20)

entry1= Entry(window,bd=10,insertwidth=1,width=4)
entry1.place(x=100,y=100)
entry2= Entry(window,bd=10,insertwidth=1,width=4)
entry2.place(x=170,y=100)
entry3= Entry(window,bd=10,insertwidth=1,width=4)
entry3.place(x=240,y=100)
entry4= Entry(window,bd=10,insertwidth=1,width=4)
entry4.place(x=310,y=100)
entry5= Entry(window,bd=10,insertwidth=1,width=4)
entry5.place(x=380,y=100)
entry6= Entry(window,bd=10,insertwidth=1,width=4)
entry6.place(x=450,y=100)

btn2= Button(window, text="Enter", command=user_list)
btn2.pack(pady=65)

label3=Label(window, font="arial 14 bold", bg="#e84e17")
label3.place(x=200,y=200)

btn2= Button(window, text="Clear Entries", command=clear_function)
btn2.pack(pady=10)

label4=Label(window, font="arial 14 bold", bg="#e84e17")
label4.place(x=220, y=320)

btn2= Button(window, text="Generate Lottery Numbers", command=lotto_numbers)
btn2.pack(pady=80)

label5=Label(window, font="arial 14 bold", bg="#e84e17")
label5.place(x=190, y=450)

btn2= Button(window, text="Exit",command=close_window)
btn2.pack(pady=20)

window.mainloop()
