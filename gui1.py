from Tkinter import *
import pymysql
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
global e1,e2,e3,e4,e5,e6,e7,e8,x,z1,z2,z3,z4,z5,z6,z7,z8,r1,k2,k3,window1,window2,window3,window4,window5
def password(c,d):
   
    for i in range(1):
         a=random.randint(11001,99999)
    phone="9119225518"
    passwd="onelastride"
    mob=d
    msg= "You are verified by your College and now your password for application meri pahachaan is"+" "+str(c)+str(a)
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
    verification()
    connect=pymysql.connect(host="localhost",user="akshat",passwd="Super_10",db="Identity")
    cur=connect.cursor()
    sql_command="update Studentinfo set password='%s' where Username='%s'"
    cur.execute(sql_command,(a,c))
    connect.commit()
    connect.close()


def verify(a,b,c,d,e,f,g,h,i):
      global window1,window2,window3,window4,window5
      window6 = Tk()
      window6.title("Meri pahachaan")
      A=Label(window6, text=a)
      B=Label(window6, text=b)
      C=Label(window6, text=c)
      D=Label(window6, text=d)
      E=Label(window6, text=e)
      F=Label(window6, text=f)
      G=Label(window6, text=g)

      A.grid(row=0,column=0)
      B.grid(row=1,column=0)
      C.grid(row=2,column=0)
      D.grid(row=3,column=0)
      E.grid(row=4,column=0)
      F.grid(row=5,column=0)
      G.grid(row=6,column=0)
    
      W=Button(window6,text="Verify",fg="Red",command=lambda:(password(h,i)))
      W.grid(row=7, column=0)
      c=Button(window6,text="Not Verify",fg="Red",command=window6.destroy)
      c.grid(row=8, column=0)
      window5.destroy()
      window6.mainloop()
def Requests():
  connect=pymysql.connect(host="localhost",user="akshat",passwd="Super_10",db="Identity")
  cur=connect.cursor()
  sql_command="select Name,Username,College_name,Date_of_birth,Branch,City,Phoneno from Studentinfo where College_name='BKBIET'"
  cur.execute(sql_command)
  data=cur.fetchall()
  data1=list(data)
  data2=list(data1[0])
  connect.commit()
  connect.close()
  for j in range(len(data1)):
   for i in data1:
      a="Name"+"->"+" "+i[0]
      b="Username"+"->"+" "+i[1]
      c="College_name"+"->"+" "+i[2]
      d="Date_of_birth"+"->"+" "+i[3]
      e="Branch"+"->"+" "+i[4]
      f="City"+"->"+" "+i[5]
      g="Phoneno"+"->"+" "+str(i[6])
      verify(a,b,c,d,e,f,g,i[1],int(i[6])) 
          
  
def login1(f1,h1,m1,n1,k1,b1,t1,l1,j2,k3):
  global k2,window1,window2,window3,window4,window5
  connect=pymysql.connect(host="localhost",user="akshat",passwd="Super_10",db="Identity")
  cur=connect.cursor()
  if k2=="Name":
      sql_command="select"+" "+f1+","+h1+","+m1+","+n1+","+k1+","+b1+","+t1+","+l1+" "+"from Studentinfo where password=%s and Username=%s"
  elif k2=="College_admin":
       sql_command="select"+" "+f1+","+h1+","+m1+","+n1+","+k1+","+b1+","+t1+","+l1+" "+"from Facultyinfo where password=%s and Username=%s"
  else:
       sql_command="select"+" "+f1+","+h1+","+m1+","+n1+","+k1+","+b1+","+t1+","+l1+" "+"from Companyinfo where password=%s and Username=%s"
  cur.execute(sql_command,(j2,k3))
  data=cur.fetchall()
  data1=list(data)
  data2=list(data1[0])
  connect.commit()
  connect.close()

  a=f1+"->"+" "+data2[0]
  b=h1+"->"+" "+data2[1]
  c=m1+"->"+" "+data2[2]
  d=n1+"->"+" "+data2[3]
  e=k1+"->"+" "+data2[4]
  f=b1+"->"+" "+data2[5]
  g=t1+"->"+" "+data2[6]
  h=l1+"->"+" "+str(data2[7])
  

  window5 = Tk()
  window5.title("Meri pahachaan")
  A=Label(window5, text=a)
  B=Label(window5, text=b)
  C=Label(window5, text=c)
  D=Label(window5, text=d)
  E=Label(window5, text=e)
  F=Label(window5, text=f)
  G=Label(window5, text=g)
  H=Label(window5, text=h)

  A.grid(row=0,column=0)
  B.grid(row=1,column=0)
  C.grid(row=2,column=0)
  D.grid(row=3,column=0)
  E.grid(row=4,column=0)
  F.grid(row=5,column=0)
  G.grid(row=6,column=0)
  H.grid(row=7,column=0)

  Q=Button(window5,text="Quit",fg="Blue",command=window5.destroy)
  if k2=="Name":
     W=Button(window5,text="Add project",fg="Red")
     W.grid(row=8, column=0)
  elif k2=="College_admin":
     W=Button(window5,text="Requests",fg="Red",command=Requests)
     W.grid(row=8, column=0)
  elif k2== "Company_admin":
     W=Button(window5,text="Rankings",fg="Red")
     W.grid(row=8, column=0)
    
  Q.grid(row=8,column=2)
 
  window5.mainloop()
  


def db(r1):
          
  global e1,e2,e3,e4,e5,e6,e7,e8,x,z1,z2,z3,z4,z5,z6,z7,z8,k2
  
  z1=e1.get()
  z2=e2.get()
  z3=e3.get()
  z4=e4.get()
  z5=e5.get()
  z6=e6.get()
  z7=e7.get()
  z8=int(e8.get())

  
  connect=pymysql.connect(host="localhost",user="akshat",passwd="Super_10",db="Identity")
  cur=connect.cursor()
  if r1==x:
    
    if k2=="Name":
      sql_command="insert into Studentinfo(Name,Username,College_name,Date_of_birth,Branch,City,Email,Phone_number) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    elif k2=="College_admin":
      sql_command="insert into Facultyinfo(Faculty_admin,Username,College_name,College_id,College_type,City,College_Email,Emergency_no) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    else:
      sql_command="insert into Companyinfo(Company_admin,Username,Company_name,Company_id,Company_type,City,Company_Email,Emergency_no) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    data=(z1,z2,z3,z4,z5,z6,z7,int(z8))
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


def verification():

    global window1,window2,window3,window4,window5
    window4 = Tk()
    window4.title("Verification")
    A=Label(window4,text="Verification code",fg="Blue") 
    B=Button(window4,text="Resend OTP",fg="Red")
    C=Button(window4,text="Save",fg="Green",command=lambda:([db(int(w1.get()))],[window4.destroy]))
    A.grid(row=0, column=0)
    w1=Entry(window4)
    w1.grid(row=0,column=1)
    B.grid(row=1,column=1)
    C.grid(row=1,column=2)
    window3.destroy()
    window4.mainloop()

           
def final(y):
    global x        # Sending OTP on phone
    for i in range(1):
         a=random.randint(11001,99999)
    x=a
    phone="9119225518"
    passwd="onelastride"
    mob=int(y)
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
    verification()        


        
          



def signup(p1,p2,p3,p4,p5,p6,p7,p8):
     global e1,e2,e3,e4,e5,e6,e7,e8,r1,x,z1,z2,z3,z4,z5,z6,z7,z8,k2,window1,window2,window3,window4,window5
     window3 = Tk()
     window3.title("Registration form")
     k2=p1
     A=Label(window3, text=p1)
     B=Label(window3, text=p2)
     C=Label(window3, text=p3)
     D=Label(window3, text=p4)
     E=Label(window3, text=p5)
     F=Label(window3, text=p6)
     G=Label(window3, text=p7)
     H=Label(window3, text=p8)

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
     W=Button(window3,text="Save",fg="Red",command=lambda:final(int(e8.get())))
 
     W.grid(row=8, column=0)
     Q.grid(row=8,column=2)
     window2.destroy()
     window3.mainloop()
    
def Login(x,f1,h1,m1,n1,k1,b1,t1,l1):
     global k2,window1,window2,window3,window4,window5
   #Student login window  
     k2=f1
     window2 = Tk()
     window2.title("Login")
     G=Label(window2, text=x)
     H=Label(window2, text="Password")
     G.grid(row=0,column=0)
     H.grid(row=1,column=0)
     q1=Entry(window2)
     q2=Entry(window2,show="*")
     q1.grid(row=0,column=1)
     q2.grid(row=1,column=1)
     I=Button(window2,text="Login",fg="Blue",command=lambda:login1(f1,h1,m1,n1,k1,b1,t1,l1,q2.get(),q1.get())) 
     J=Button(window2,text="Quit",fg="Red",command=window2.destroy)
     I.grid(row=2, column=0)
     J.grid(row=2,column=2)
     window1.destroy()
     window2.mainloop()
    
          

         
          
    


# Student window
def choice(q1,w1,e1,d1,f1,h1,m1,n1,k1,b1,t1,l1):
  global window1,window2,window3,window4,window5
  window1 = Tk()
  window1.title(q1)
  E=Button(window1, text=w1,command=lambda:Login(d1,f1,h1,m1,n1,k1,b1,t1,l1))
  F=Button(window1, text=e1,command=lambda:signup(f1,h1,m1,n1,k1,b1,t1,l1))
  E.grid(row=0,column=0)
  F.grid(row=0,column=4)
  window.destroy()
  window1.mainloop()


#Main window

window = Tk()
window.title("Meri Pahachaan")
A=Button(window,text="Student",fg="Blue",command= lambda:choice("Student","Login","Sighup","Username","Name","Username","College_name","Date_of_birth","Branch","City","Email","Phoneno"))
B=Button(window,text="Faculty",fg="Red",command= lambda:choice("Faculty","Login","Sighup","Username","College_admin","Username","College_name","College_id","College_type","City","College_Email","Emergency_no"))
C=Button(window,text="Comapany",fg="Green",command= lambda:choice("Company","Login","Sighup","Username","Company_admin","Username","Company_name","Company_id","Company_type","City","Company_email","Emergency_no"))
A.grid(row=0, column=0)
B.grid(row=0,column=1)
C.grid(row=0,column=2)
window.mainloop()


