from tkinter import * 
import json
import CodeSend
with open ("StudCred.json","r") as f:
    Data = json.load(f)

#windows and frames

mainwindow = Tk()
mainwindow.geometry("600x600")
mainframe = Frame(mainwindow)
teacherloginframe = Frame(mainwindow)
teacherloginframe = Frame(mainwindow)
studentloginframe = Frame(mainwindow)
studentloginframe2 = Frame(mainwindow)
printframe = Frame(mainwindow)
studentdashframe = Frame(mainwindow)
signupframe = Frame(mainwindow)
mainframe.grid_rowconfigure(10,weight=1)
mainframe.grid_columnconfigure(1,weight=1)
def show_main():
    signupframe.pack_forget()
    teacherloginframe.pack_forget()
    studentloginframe.pack_forget()
    printframe.pack_forget()
    mainframe.pack(fill="both", expand=1)
def show_student():
    signupframe.pack_forget()
    teacherloginframe.pack_forget()
    mainframe.pack_forget()
    printframe.pack_forget()
    studentloginframe.pack(fill="both", expand=1)
def show_teacher():
    signupframe.pack_forget()
    mainframe.pack_forget()
    studentloginframe.pack_forget()
    printframe.pack_forget()
    teacherloginframe.pack(fill="both", expand=1)
def show_print():
    signupframe.pack_forget()
    teacherloginframe.pack_forget()
    studentloginframe.pack_forget()
    mainframe.pack_forget()
    printframe.pack(fill="both", expand=1)
def show_sign():
    teacherloginframe.pack_forget()
    studentloginframe.pack_forget()
    mainframe.pack_forget()
    printframe.pack_forget()
    signupframe.pack(fill = "both",expand=1)
#MAINFRAME WIDGETS!
Label(mainframe,text="Welcome to JJ's Student Database",font=("times new roman",24,"bold")).pack()
Button(mainframe,text='student login frame',command=show_student).pack()
Button(mainframe,text="teacher login frame",command=show_teacher).pack()
Button(teacherloginframe,text='print frame',command=show_print).grid(column=0,row = 0)


#STUDENT LOGIN WIDGETS, frame 1, USERNAME & PASS
Label(studentloginframe,text='Student Login',font=("Arial",16,'italic')).pack()
Label(studentloginframe,text='Enter Email',font=('times new roman',10,'bold')).pack()
studentuser = Entry(studentloginframe)
studentuser.pack()
def Print():
    if studentuser.get() in Data and studentpas.get()==Data[studentuser.get()] :
        teacherloginframe.pack_forget()
        studentloginframe.pack_forget()
        printframe.pack_forget()
        mainframe.pack_forget()
        studentloginframe2.pack(fill='both',expand=1)
    else:
        Label(studentloginframe,text = 'Invalid  Username or Password',font=('arial',8),fg = 'Red').pack()

Label(studentloginframe,text='Enter Password',font=('times new roman',10,'bold')).pack()
studentpas = Entry(studentloginframe)
studentpas.pack()


        

    
Button(studentloginframe,text ='Submit',command = Print).pack()
#STUDENTLOGINWIDGET2, CODE for EMAIL
Label(studentloginframe2,text='an 8 char long code has been sent to your email').pack()
Label(studentloginframe2,text='Enter code here:').pack()
studcode = Entry(studentloginframe2)
studcode.pack()
def codesend():
    code = CodeSend.generate_secure_code(studentuser.get())
    if code == studcode.get():
        teacherloginframe.pack_forget()
        studentloginframe.pack_forget()
        printframe.pack_forget()
        mainframe.pack_forget()
        studentloginframe2.pack_forget()
        studentdashframe.pack(fill='both',expand=1)

Button(studentloginframe2,text="Sub",command=codesend).pack()
#TEACHER LOGIN WIDGETS, frame 1 & 2

#GradeFRAME


#
show_main()






mainwindow.mainloop()