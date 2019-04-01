from Tkinter import *
import pymysql
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
def Faculty():
    window5 = Tk()
    window5.title("Faculty")
    E=Button(window5, text="Login")
    F=Button(window5, text="Signup")
    E.grid(row=0,column=0)
    F.grid(row=0,column=4)
    window.destroy()
    window5.mainloop()

def Student():
 def Login():
   #Student login window  

     window2 = Tk()
     window2.title("Login")
     G=Label(window2, text="Username")
     H=Label(window2, text="Password")
     G.grid(row=0,column=0)
     H.grid(row=1,column=0)
     e1=Entry(window2)
     e2=Entry(window2,show="*")
     e1.grid(row=0,column=1)
     e2.grid(row=1,column=1)
     I=Button(window2,text="Login",fg="Blue") 
     J=Button(window2,text="Quit",fg="Red",command=window2.destroy)
     I.grid(row=2, column=0)
     J.grid(row=2,column=2)
     window1.destroy()
     window2.mainloop()
 def Signup():
     #Student signup window
     global x
     
     def OTP():
          def save():
            global x
            u=int(w1.get())
            print u
            print x
            if u==x:
              z=e1.get()
              x=e2.get()
              m=e3.get()
              n=e4.get()
              l=e5.get()
              k=e6.get()
              p=e7.get()
              f=int(e8.get())
              connect=pymysql.connect(host="localhost",user="akshat",passwd="Super_10",db="Identity")
              cur=connect.cursor()
              sql_command="insert into Studentinfo(Name,Username,College_name,DOB,Branch,City,Email,Phone_number) values(%s,%s,%s,%s,%s,%s,%s,%s)"
              data=(z,x,m,n,l,k,p,int(f))
              cur.execute(sql_command,data)
              connect.commit()
              connect.close()
              e1.delete(0, END)
              e2.delete(0, END)
              e3.delete(0, END)
              e4.delete(0, END)
              e5.delete(0, END)
              e6.delete(0, END)
              e7.delete(0, END)
              e8.delete(0, END) 
              print "All done correctly"
            else:
                print "OTP Entered is incorrect"

           
          def final():
            # Sending OTP on phone
            global x
            x=int
            for i in range(1):
               a=random.randint(11001,99999)
            x=a
            phone="9119225518"
            passwd="onelastride"
            mob=f
            print type(mob)
            msg= "Your OTP for Meri Pahachaan application is"+" "+str(a)
            browser=webdriver.Chrome(executable_path="/home/akshat/chromedriver")
            url="http://www.way2sms.com/"
            sleep(2)
            browser.get(url)
            sleep(4)
            p=browser.find_element_by_id("mobileNo") 
            p.send_keys(phone)
            k=browser.find_element_by_id("password")
            k.send_keys(passwd)
            sleep(5)  
            l=browser.find_element_by_xpath("//button[@class='btn-theme-sm btn-ls text-uppercase']")
            l.click()
            sleep(4)
            m=browser.find_element_by_id("mobile")
            m.send_keys(mob)
            n=browser.find_element_by_id("message")
            n.send_keys(msg)
            sleep(1)
            o=browser.find_element_by_id("sendButton")
            o.click()
            print "message send successfully"
            
  
          f=int(e8.get())

          final()
          window4 = Tk()
          window4.title("Verification")
          A=Label(window4,text="Verification code",fg="Blue") 
          B=Button(window4,text="Resend OTP",fg="Red",command=OTP)
          C=Button(window4,text="Save",fg="Green",command=save)
          A.grid(row=0, column=0)
          w1=Entry(window4)
          w1.grid(row=0,column=1)
          B.grid(row=1,column=1)
          C.grid(row=1,column=2)
          window4.mainloop()

        
          


         
          
     window3 = Tk()
     window3.title("Registration form")
     A=Label(window3, text="Name")
     B=Label(window3, text="Username")
     C=Label(window3, text="College_name")
     D=Label(window3, text="Date of birth")
     E=Label(window3, text="Branch")
     F=Label(window3, text="City")
     G=Label(window3, text="Email")
     H=Label(window3, text="Phone_no.")

     A.grid(row=0,column=0)
     B.grid(row=1,column=0)
     C.grid(row=2,column=0)
     D.grid(row=3,column=0)
     E.grid(row=4,column=0)
     F.grid(row=5,column=0)
     G.grid(row=6,column=0)
     H.grid(row=7,column=0)

     
     e1=Entry(window3)
     e2=Entry(window3)
     e3=Entry(window3)
     e4=Entry(window3)
     e5=Entry(window3)
     e6=Entry(window3)
     e7=Entry(window3)
     e8=Entry(window3)
     
     e1.grid(row=0,column=1)
     e2.grid(row=1,column=1)
     e3.grid(row=2,column=1)
     e4.grid(row=3,column=1)
     e5.grid(row=4,column=1)
     e6.grid(row=5,column=1)
     e7.grid(row=6,column=1)
     e8.grid(row=7,column=1)

     
     Q=Button(window3,text="Quit",fg="Blue",command=window3.destroy) 
     W=Button(window3,text="Save",fg="Red",command= OTP)
 
     W.grid(row=8, column=0)
     Q.grid(row=8,column=2)
     window3.mainloop()
     


# Student window
    
 window1 = Tk()
 window1.title("Student")
 E=Button(window1, text="Login",command=Login)
 F=Button(window1, text="Signup",command=Signup)
 E.grid(row=0,column=0)
 F.grid(row=0,column=4)
 window.destroy()
 window1.mainloop()


#Main window

window = Tk()
window.title("Meri Pahachaan")
A=Button(window,text="Student",fg="Blue",command=Student) 
B=Button(window,text="Faculty",fg="Red",command=Faculty)
C=Button(window,text="Comapany",fg="Green")
A.grid(row=0, column=0)
B.grid(row=0,column=1)
C.grid(row=0,column=2)
window.mainloop()


