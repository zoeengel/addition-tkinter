from tkinter import *

def answer_button():
   number1=int(no1_field.get())
   number2=int(no2_field.get())
   answer=number1+number2
   answer_field.configure(text=answer)

page1= Tk()
page1.title("Addition Calculator")
page1.geometry("400x500")
page1.config(background="linen")


no1_label=Label(page1, text="First Number", relief="solid", font="Sans-Serif")
no1_label.pack()
no1_field=Entry(page1, width=30)
no1_field.pack()

no2_label=Label(page1, text="Second Number", relief="solid", font="Sans-Serif")
no2_label.pack()
no2_field=Entry(page1, width=30)
no2_field.pack()

answer_label=Label(page1, text="Result", relief="solid", font="Sans-Serif")
answer_label.pack()
answer_field=Label(page1, width=30)
answer_field.pack()

no1 = Entry(page1)
no2 = Entry(page1)



my_button=Button(page1, text="Answer",   command=answer_button)
my_button.pack()

def endProgam():
    raise SystemExit
    sys.exit()

B =Button(page1, text = "Clear", command = endProgam)
B.pack()


page1.mainloop()
