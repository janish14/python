"""
from tkinter import *

gokul=Tk()
gokul.title("enquire form")
gokul.geometry("900x1300")
gokul.resizable(0,0)

#shape
Canvas=Canvas(gokul,height=180,width=750)
Canvas.create_rectangle(0,1,2,3,outline="#ccccff",fill="BLACK",width=3000)
Canvas.place(x=10,y=320)



#NEW PAGE
def arul():
       gokul.destroy()
       new=Tk()
       new.title("enquire  ")
       new.configure(background="white")
       new.geometry("900x1300")
       new.resizable(0,0)

       def prev():
              new.destroy()
              gokul=Tk()       
      #button
       b=Button(new,text="prev page",command=prev)
       b.place(x=550,y=600)
       
      #entry
       e1=Entry(new)
       e1.place(x=10,y=10,width=100,height=100)
       e1=Entry(new)
       e1.place(x=140,y=390,width=200)
       e1=Entry(new)
       e1.place(x=150,y=430,width=180)
       e1=Entry(new)
       e1.place(x=150,y=470,width=180)
       e1=Entry(new)
       e1.place(x=150,y=510,width=180)
       e1=Entry(new)
       e1.place(x=170,y=550,width=180)
       e1=Entry(new)
       e1.place(x=110,y=590,width=350)
       e1=Entry(new)
       e1.place(x=530,y=390,width=150)
       e1=Entry(new)
       e1.place(x=530,y=430,width=150)
       e1=Entry(new)
       e1.place(x=440,y=470,width=150)
       e1=Entry(new)
       e1.place(x=440,y=510,width=150)
       e1=Entry(new)
       e1.place(x=440,y=550,width=150)

       
      #LABEL



       l3=Label(new,text="course name:",fg="#333333",font="roman 10 bold")
       l3.place(x=10,y=390)
       l4=Label(new,text="TotalFees:",fg="#333333",font="roman 10 bold")
       l4.place(x=10,y=430)
       l5=Label(new,text="Duration:",fg="#333333",font="roman 10 bold")
       l5.place(x=450,y=390)
       l5=Label(new,text="Discound:",fg="#333333",font="roman 10 bold")
       l5.place(x=450,y=430)
       l6=Label(new,text="Admission Fees:",fg="#333333",font="roman 10 bold")
       l6.place(x=10,y=470)
       l3=Label(new,text="First Installment:",fg="#333333",font="roman 10 bold")
       l3.place(x=10,y=510)
       l4=Label(new,text="Secound Installment:",fg="#333333",font="roman 10 bold")
       l4.place(x=10,y=550)
       l5=Label(new,text="other details",fg="#333333",font="roman 10 bold")
       l5.place(x=10,y=590)
       l6=Label(new,text="Date:",fg="#333333",font="roman 10 bold")
       l6.place(x=380,y=470)
       l6=Label(new,text="Date:",fg="#333333",font="roman 10 bold")
       l6.place(x=380,y=510)
       l6=Label(new,text="Date:",fg="#333333",font="roman 10 bold")
       l6.place(x=380,y=550)



       







       
#button
b=Button(gokul,text="next page",command=arul)
b.place(x=750,y=1)


#label
l1=Label(gokul,text="SOFTLOGIC GROUP",fg="#9900cc",font="garamond 15 bold")
l1.place(x=310,y=1)
l3=Label(gokul,text="enquiry form",fg="#ffcc90",font="sabon 12 bold")
l3.place(x=370,y=30)
l3=Label(gokul,text="Student Name:",fg="#333333",font="roman 10 bold")
l3.place(x=10,y=87)
l4=Label(gokul,text="contact no:",fg="#333333",font="roman 10 bold")
l4.place(x=10,y=130)
l5=Label(gokul,text="Alternative:",fg="#333333",font="roman 10 bold")
l5.place(x=300,y=130)
l6=Label(gokul,text="Email ID:",fg="#333333",font="roman 10 bold")
l6.place(x=10,y=170)
l7=Label(gokul,text="ADDRESS:",fg="#333333",font="roman 10 bold")
l7.place(x=10,y=210)
l7=Label(gokul,text="date:",fg="#333333",font="roman 10 bold")
l7.place(x=650,y=47)
l8=Label(gokul,text="course Interested For:",fg="#333333",font="timesnewroman 11 bold")
l8.place(x=10,y=280)
l9=Label(gokul,text="Other Course:",fg="#333333",font="roman 10 bold",bg="#9999cc")
l9.place(x=20,y=460)
l10=Label(gokul,text="Academic Qualification:",fg="#333333",font= "roman 11 bold",bg="#99ccff")
l10.place(x=10,y=510)
l12=Label(gokul,text="Qualification",fg="#333333",font="roman 10 bold")
l12.place(x=10,y=550)
l13=Label(gokul,text="Collage Name",fg="#333333",font="roman 10 bold")
l13.place(x=180,y=550)
l14=Label(gokul,text="Year of passing",fg="#333333",font="roman 10 bold")
l14.place(x=350,y=550)
l15=Label(gokul,text="Percentage",fg="#333333",font="roman 10 bold")
l15.place(x=520,y=550)
l16=Label(gokul,text="Specialization",fg="#333333",font="roman 10 bold")
l16.place(x=680,y=550)
l17=Label(gokul,text="IF Employed,Company Name",fg="#333333",font="roman 10 bold",bg="#66ccff")
l17.place(x=10,y=620)
l18=Label(gokul,text="Role",fg="#333333",font="roman 10 bold",bg="#66ccff")
l18.place(x=500,y=620)
l19=Label(gokul,text="Training Type:",fg="#333333",font="roman 10 bold",bg="#66ccff")
l19.place(x=10,y=660)
l20=Label(gokul,text="How do you know about Us..?:",fg="#333333",font="roman 10 bold",bg="#ffff99")
l20.place(x=600,y=130)


#entry
e1=Entry(gokul)
e2=Entry(gokul)
e3=Entry(gokul)
e4=Entry(gokul)
e5=Entry(gokul)
e6=Entry(gokul)
e7=Entry(gokul)
e8=Entry(gokul)
e9=Entry(gokul)
e10=Entry(gokul)
e11=Entry(gokul)
e12=Entry(gokul)
e13=Entry(gokul)
e14=Entry(gokul)

e1.place(x=120,y=87)
e2.place(x=120,y=130)
e3.place(x=400,y=130)
e4.place(x=120,y=170)
e5.place(x=120,y=210,width=165,height=50)
e6.place(x=700,y=47)
e7.place(x=130,y=460,width=200)
e8.place(x=10,y=580,width=120)
e9.place(x=160,y=580,width=150)
e10.place(x=350,y=580,width=120)
e11.place(x=520,y=580,width=100)
e12.place(x=680,y=580,width=150)
e13.place(x=220,y=620,width=270)
e14.place(x=540,y=620,width=230)

#check box

c=Checkbutton(gokul,text="SQL",bg="#cccc99")
c.place(x=25,y=330)
c1=Checkbutton(gokul,text="RPA",bg="#cccc99")
c1.place(x=25,y=370)
c2=Checkbutton(gokul,text="AWS",bg="#cccc99")
c2.place(x=25,y=410)
c3=Checkbutton(gokul,text="python",bg="#cccc99")
c3.place(x=120,y=330)
c4=Checkbutton(gokul,text="DOTNET",bg="#cccc99")
c4.place(x=120,y=370)
c5=Checkbutton(gokul,text="DevOps",bg="#cccc99")
c5.place(x=120,y=410)
c6=Checkbutton(gokul,text="bigdata",bg="#cccc99")
c6.place(x=230,y=330)
c7=Checkbutton(gokul,text="Matlab",bg="#cccc99")
c7.place(x=230,y=370)
c8=Checkbutton(gokul,text="Hadoop",bg="#cccc99")
c8.place(x=230,y=410)
c9=Checkbutton(gokul,text="Data science",bg="#cccc99")
c9.place(x=340,y=330)
c10=Checkbutton(gokul,text="R program",bg="#cccc99")
c10.place(x=340,y=370)
c11=Checkbutton(gokul,text="MS Azure",bg="#cccc99")
c11.place(x=340,y=410)
c12=Checkbutton(gokul,text="Web designing",bg="#cccc99")
c12.place(x=480,y=330)
c13=Checkbutton(gokul,text="Software testing",bg="#cccc99")
c13.place(x=480,y=370)
c14=Checkbutton(gokul,text="Machine Learning",bg="#cccc99")
c14.place(x=480,y=410)
c15=Checkbutton(gokul,text="Regular",bg="#99ff90")
c15.place(x=150,y=660)
c16=Checkbutton(gokul,text="Week End",bg="#99FF90")
c16.place(x=250 ,y=660)
ca=Checkbutton(gokul,text="Fast track",bg="#99FF90")
ca.place(x=370 ,y=660)
cb=Checkbutton(gokul,text="Google",bg="#666699")
cb.place(x=600 ,y=170)
cc=Checkbutton(gokul,text="Justdial",bg="#666699")
cc.place(x=600 ,y=210)
cd=Checkbutton(gokul,text="Direct",bg="#666699")
cd.place(x=700 ,y=170)
cc=Checkbutton(gokul,text="Reference",bg="#666699")
cc.place(x=700 ,y=210)








gokul.mainloop
"""
