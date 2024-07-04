from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    from tkinter import ttk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Student Placement Prediction System")
    root.configure(background="deeppink4")
    
    gender = tk.IntVar()
    Yearpassing = tk.IntVar()
    Experience = tk.IntVar()
    Branch = tk.StringVar()
    GradeID = tk.IntVar()
    Topic = tk.IntVar()
    Semester = tk.IntVar()
    ten  = tk.DoubleVar()
    twelve= tk.DoubleVar()
    Diploma= tk.StringVar()
    BE = tk.StringVar()
    NoCourses  = tk.IntVar()
    Internships = tk.IntVar()
    YearGap = tk.IntVar()
    
   
    
    #===================================================================================================================
    def Detect():
        e1= gender.get()
        print(e1)
        e2=Yearpassing.get()
        print(e2)
        e3= Experience.get()
        print(e3)
        e4=Branch.get()
        if e4=="Computer":
            e4=0
        elif e4=="E&TC":
            e4=1
        elif e4=="Mechanical":
            e4=2
        else: 
            e4=3
        print(e4)
        e5=ten.get()
        print(e5)
        e6=twelve.get()
        print(e6)
        e7=Diploma.get()
        if e7=="NA":
            e7=0
        elif e7=="Above 60":
            e7=1
        else: 
            e7=2
        print(e7)
        e8=BE.get()
        if e8=="Above 60":
            e8=1
        else: 
            e8=2
        print(e8)
        e9=NoCourses.get()
        print(e9)
        e10=Internships.get()
        print(e10)
        e11=YearGap.get()
        print(e11)
        
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('SVM_model1.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9,e10, e11]])
        print(v)
        if v[0]==0:
            print("Low")
            no = tk.Label(root, text="Student performant is Low \n Student is Not Applicable For Job", background="red", foreground="white",font=('times', 20, ' bold '),width=25,height=2)
            no.place(x=600, y=500)
            
                     
        elif v[0]==1:
            print("Medium")
            no = tk.Label(root, text="Student performant is Medium \n Need More Improvement ", background="green", foreground="white",font=('times', 20, ' bold '),width=25,height=2)
            no.place(x=600, y=500)
            
            
        else:
            print("High")
            yes = tk.Label(root,text="Student performant is Good \n Student Applicable For Job ",background="green",foreground="white",font=('times', 20, ' bold '),width=25,height=2)
            yes.place(x=600,y=500)
            


    l1=tk.Label(root,text="Gender",background="olive",font=('times', 20, ' bold '),width=15)
    l1.place(x=5,y=5)
    tk.Radiobutton(root, text="Male", padx=5, width=3, bg="snow", font=("bold", 15), variable=YearGap, value=1).place(x=280,
                                                                                                                    y=1)
    tk.Radiobutton(root, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=YearGap, value=2).place(
        x=360, y=1)

    l2=tk.Label(root,text="Passing Year",background="olive",font=('times', 20, ' bold '),width=15)
    l2.place(x=5,y=50)
    Nationlity=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Yearpassing)
    Nationlity.place(x=300,y=50)

    l3=tk.Label(root,text="Experience",background="olive",font=('times', 20, ' bold '),width=15)
    l3.place(x=5,y=100)
    PlaceofBirth=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Experience)
    PlaceofBirth.place(x=300,y=100)
    
    l4=tk.Label(root,text="Branch",background="olive",font=('times', 20, ' bold '),width=15)
    l4.place(x=5,y=150)
    monthchoosen= ttk.Combobox(root, width = 23, textvariable = Branch)
    # Adding combobox drop down list
    monthchoosen['values'] = (' Computer',
    						' E&TC',
    						' Mechanical',
                            'Civil')
                            
    monthchoosen.place(x=300,y=150)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

    # l5=tk.Label(root,text="GradeID",background="olive",font=('times', 20, ' bold '),width=15)
    # l5.place(x=5,y=200)
    # GradeID=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=GradeID)
    # GradeID.place(x=300,y=200)

    # l6=tk.Label(root,text="Topic",background="olive",font=('times', 20, ' bold '),width=15)
    # l6.place(x=5,y=250)
    # Topic=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Topic)
    # Topic.place(x=300,y=250)

    # l7=tk.Label(root,text="Semester",background="olive",font=('times', 20, ' bold '),width=15)
    # l7.place(x=5,y=300)
    # Semester=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Semester)
    # Semester.place(x=300,y=300)

    l8=tk.Label(root,text="10th Marks",background="olive",font=('times', 20, ' bold '),width=15)
    l8.place(x=5,y=200)
    ten=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=ten)
    ten.place(x=300,y=200)

    l9=tk.Label(root,text="12th Marks",background="olive",font=('times', 20, ' bold '),width=15)
    l9.place(x=5,y=250)
    twelve=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=twelve)
    twelve.place(x=300,y=250)

    l10=tk.Label(root,text="Diploma",background="olive",font=('times', 20, ' bold '),width=15)
    l10.place(x=500,y=5)
    monthchoosen= ttk.Combobox(root, width = 27, textvariable = Diploma)
    # Adding combobox drop down list
    monthchoosen['values'] = (' NA',
    						' Above 60',
    						' Below 60')
                            
    monthchoosen.place(x=800,y=1)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

    l11=tk.Label(root,text="BE",background="olive",font=('times', 20, ' bold '),width=15)
    l11.place(x=500,y=50)
    monthchoosen= ttk.Combobox(root, width = 27, textvariable = BE)
    # Adding combobox drop down list
    monthchoosen['values'] = (' Above 60',
    						' Below 60')
                            
    monthchoosen.place(x=800,y=50)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

    l12=tk.Label(root,text="No Of Courses Done",background="olive",font=('times', 20, ' bold '),width=16)
    l12.place(x=500,y=100)
    NoCourses=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=NoCourses)
    NoCourses.place(x=800,y=100)

    l13=tk.Label(root,text="Internships",background="olive",font=('times', 20, ' bold '),width=15)
    l13.place(x=500,y=150)
    Internships=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Internships)
    Internships.place(x=800,y=150)
    
    l14=tk.Label(root,text="YearGap",background="olive",font=('times', 20, ' bold '),width=15)
    l14.place(x=500,y=200)
    tk.Radiobutton(root, text="Yes", padx=5, width=5, bg="snow", font=("bold", 15), variable=YearGap, value=1).place(x=800,
                                                                                                                    y=200)
    tk.Radiobutton(root, text="No", padx=20, width=4, bg="snow", font=("bold", 15), variable=YearGap, value=2).place(
        x=900, y=200)


    
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=800,y=250)


    root.mainloop()

Train()