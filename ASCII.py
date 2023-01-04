from tkinter import*
root=Tk()

root.title("ASCII")
root.geometry("500x500")
root.configure(background='green')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)


label=Label(root,text="Name in ASCII - ",bg="Orange",fg="White")

def ASCIIconvertor():
    input_word=enter_word.get()
    for i in input_word:
        lable["text"]+=str(ord(i))+""

btn=Button(root,text="ASCII value", command=ASCIIconvertor,bg="orange",fg="Black")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)




root.mainloop()