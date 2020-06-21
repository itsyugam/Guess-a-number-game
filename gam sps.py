from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image,AsyncImage
from kivy.uix.filechooser import FileChooserIconView
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import json
import requests
import ssl
import urllib.parse as u
import pickle
from kivy.graphics import Color,Rectangle,Ellipse,Line

Window.clearcolor=(1,1,1,0.3)
Window.size=(1080,1920)
w,h=Window.size


#FUNCTION TO ACCESS FIREBASE
def processdata():
   ssl._create_default_https_context=ssl._create_unverified_context

   url="https://profile-fe70b.firebaseio.com"
   auth="hFqxaKpiHT90rFDrKoHWkBdZ vgDfCKc0pqV92csz"
   path=u.urlencode({"aut":auth})

   finalpath=url+"/Details/.json"+"?"+path
   return finalpath

#FUNCTION TO VERIFY  EMAIL ACCOUNT
def Email_verification(name,reciever):
   global otp
   otp=random.randint(1000,9999)
   mail_content ="Hello {},\
        \n!!!!!!!!!!!!!      Welcome to my profile        !!!!\
        \nVerification ID -{}".format(name,otp)
        
   sendr="yugamsachdeva100@gmail.com"       
   sender_pass="wevsltfhdsifjorb"
   reciever_address=reciever
   
   msg = MIMEMultipart()
   msg['From'] = sendr
   msg['To'] = reciever_address
   msg['Subject'] = "ID verification"
   
   msg.attach(MIMEText(mail_content,"plain"))
   
   smtp = smtplib.SMTP('smtp.gmail.com',587)
   smtp.starttls()
   smtp.login(sendr,sender_pass)
   smtp.sendmail(sendr, reciever_address, msg.as_string())
   smtp.close()
   
#CLASS FOR SIGNUP PAGE   
class Profile(FloatLayout):
   def __init__(self,*args,**kwargs):
      super().__init__(*args,**kwargs)
      
      self.l=Label(color=(0,0.5,1,1),text="SIGN UP\n________",font_size='30sp',size_hint=(1,0.1),pos_hint={'x':0,'y':0.85})
      self.add_widget(self.l)
      list=["userid:","Full Name:","Email:","Password:"]
      y=0.7
      for i in range(len(list)):
         self.la=Label(color=(0,0.5,1,1),text=list[i],size_hint=(0.3,0.1),pos_hint={'x':0,'y':y},font_size='20sp')
         self.add_widget(self.la)
         y=y-0.15
      
      self.t0=TextInput(size_hint=(0.7,0.1),pos_hint={'x':0.3,'y':0.7})
      self.add_widget(self.t0)
                
      self.t1=TextInput(size_hint=(0.7,0.1),pos_hint={'x':0.3,'y':0.55})
      self.add_widget(self.t1)
         
      self.t2=TextInput(size_hint=(0.7,0.1),pos_hint={'x':0.3,'y':0.40})
      self.add_widget(self.t2)
      global email
      email=self.t2.text
         
      self.t3=TextInput(size_hint=(0.7,0.1),pos_hint={'x':0.3,'y':0.25},password=True)
      self.add_widget(self.t3)
         
            
      self.b=Button(text="create", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.4,'y':0.15})
      self.add_widget(self.b)
      self.b.bind(on_press=self.verify)
      
      self.lab=Label(color=(0,0.5,1,1),text="Already have account:",size_hint=(1,0.05),pos_hint={'x':0,'y':0.1},font_size='10sp')
      self.add_widget(self.lab)
      
      self.b2=Button(text="log in", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.4,'y':0.05})
      self.add_widget(self.b2)
      self.b2.bind(on_press=self.login)
      
      
   def login(self,*args):
      s.current="3"
      
   def verify(self,*args):
      global name
      global detail
      global filename
      global email
      
      finalpath=processdata()
      list=requests.get(finalpath).json()
      
      mail=[]  
      for k,v in list.items():
         mail.append(v['mail'])
      
      if self.t0.text in list:
         self.l7=Label(color=(0,0.5,1,1),text="User id not available!",size_hint=(0.9,0.05),pos_hint={'x':0,'y':0.65})
         self.add_widget(self.l7)
         
      elif self.t2.text in mail:
            self.l7=Label(color=(0,0.5,1,1),text="Email I'd is already registered",size_hint=(1,0.05),pos_hint={'x':0,'y':0.35})
            self.add_widget(self.l7)
      else:
            user=self.t1.text
            email=self.t2.text
            detail={self.t0.text:{'name':self.t1.text,'mail':self.t2.text,'pass':self.t3.text,'college':'college','profession':'profession','skills':'skills','achievements':'achievements','token':'token',"headline":"student","country":"India","region":"city,state","summary":"summary"}}
         
         
            if len(self.t0.text)==0 or len(self.t1.text)==0 or len(self.t2.text)==0 or len(self.t3.text)==0:
               self.l=Label(color=(0,0.5,1,1),text="All the details are mandatory!",size_hint=(1,0.5),pos_hint={'x':0,'y':-0.03},font_size='15sp')
               self.add_widget(self.l)
               Profile()
            else:
                Email_verification(self.t1.text,email)
                s.current="2"       
                self.t0.text=self.t1.text=self.t2.text=self.t3.text=""
 
#CLASS FOR OTP VERIFICATION PAGE     
class verification(FloatLayout):
   def __init__(self,*args,**kwargs):
      super().__init__(*args)
      self.l=Label(color=(0,0.5,1,1),text="VERIFICATION\n_______________",font_size='30sp',size_hint=(1,0.1),pos_hint={'x':0,'y':0.85})
      self.add_widget(self.l)
      self.l1=Label(color=(0,0.5,1,1),text="Enter OTP:",font_size='20sp',size_hint=(0.9,0.1),pos_hint={'x':0,'y':0.7})
      self.add_widget(self.l1)
      
      self.ttt=TextInput(size_hint=(0.4,0.05),pos_hint={'x':0.34,'y':0.67})
      self.add_widget(self.ttt)
      
      self.b1=Button(text="Verify",size_hint=(0.2,0.05),pos_hint={'x':0.4,'y':0.57}, background_color=(0,0.5,1,1))
      self.add_widget(self.b1)
      self.b1.bind(on_press=self.done)
      
      self.bb=Button(text="log in",size_hint=(0.2,0.05),pos_hint={'x':0.4,'y':0.50}, background_color=(0,0.5,1,1))
      self.add_widget(self.bb)
      self.bb.bind(on_press=self.page)
      
   def page(self,*args):
      s.current="3"
         
   def done(self,*args,**kwargs):
      global user
      global otp
      otptext=int(self.ttt.text)
      if otptext==otp:
         global detail
         global email
         
         finalpath=processdata()

         store=json.dumps(detail)
         requests.patch(finalpath,store)
         
         self.l8=Label(color=(0,0.5,1,1),text="profile created!",size_hint=(1,0.05),pos_hint={'x':0,'y':0.63})
         self.add_widget(self.l8)
      else:
         self.l9=Label(color=(0,0.5,1,1),text="wrong otp!",size_hint=(1,0.05),pos_hint={'x':0,'y':0.63})
         self.add_widget(self.l9)
         
#CLASS FOR LOGIN PAGE
class Login(FloatLayout):
   def __init__(self,*args):
      super().__init__(*args)
      self.l=Label(text="LOG IN\n_______",font_size='30sp',size_hint=(1,0.1),pos_hint={'x':0,'y':0.85},color=(0,0.5,1,1))
      self.add_widget(self.l)
      
      self.ll2=Label(color=(0,0.5,1,1),text="User Id:  ",size_hint=(0.6,0.5),font_size="25sp",pos_hint={'x':0,'y':0.50})
      self.add_widget(self.ll2)
      
      self.ll3=Label(color=(0,0.5,1,1),text="  Password:",size_hint=(0.6,0.5),font_size="25sp",pos_hint={'x':0,'y':0.305})
      self.add_widget(self.ll3)
      
      self.et=TextInput(size_hint=(0.7,0.1),pos_hint={'x':0.18,'y':0.63})
      self.add_widget(self.et)
      
      
      self.pt=TextInput(password=True,size_hint=(0.7,0.1),pos_hint={'x':0.18,'y':0.43})
      self.add_widget(self.pt)    
                  
      self.bu=Button(text="log in", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.4,'y':0.30})
      self.add_widget(self.bu)
      self.bu.bind(on_press=self.mainp)
      
      self.bu3=Button(text="forgot", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.4,'y':0.23})
      self.add_widget(self.bu3)
      self.bu3.bind(on_press=self.recovery)       
      
      self.lab=Label(color=(0,0.5,1,1),text="create account:",size_hint=(1,0.05),pos_hint={'x':0,'y':0.15},font_size='10sp')
      self.add_widget(self.lab)
      
      self.bu2=Button(text="sign up", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.4,'y':0.10})
      self.add_widget(self.bu2)
      self.bu2.bind(on_press=self.firstpage)
    
   def recovery(self,*args):
      s.current="5"
        
   def firstpage(self,*args):
         s.current="1"
         
   def mainp(self,*args):
         finalpath=processdata()
         list=requests.get(finalpath).json()
         
         if len(self.et.text)==0 or len(self.pt.text)==0:
            self.lll0=Label(color=(0,0.5,1,1),text="fill the detail to login!",size_hint=(1,0.05),pos_hint={'x':0,'y':0.35})
            self.add_widget(self.lll0)
         else:  
            if self.et.text not in list:
               self.lll=Label(color=(0,0.5,1,1),text="User id is wrong!          ",size_hint=(0.7,0.05),pos_hint={'x':0,'y':0.58})
               self.add_widget(self.lll)
            elif self.pt.text!=list[self.et.text]["pass"]:
               self.lll1=Label(color=(0,0.5,1,1),text="wrong password!",size_hint=(0.63,0.05),pos_hint={'x':0,'y':0.38})
               self.add_widget(self.lll1)
            else:
               global uid
               global pop1
               uid=self.et.text
               self.et.text=""
               self.pt.text=""
               f1=FloatLayout()
               f1.bbt1=Button(color=(0,0.5,1,1),text="Yes",size_hint=(0.3,0.2),pos_hint={'x':0.1,'y':0.1})
               f1.add_widget(f1.bbt1)
               f1.bbt1.bind(on_press=self.yes)
               
               f1.bbt2=Button(color=(0,0.5,1,1),text="No",size_hint=(0.3,0.2),pos_hint={'x':0.6,'y':0.1})
               f1.add_widget(f1.bbt2)
               f1.bbt2.bind(on_press=self.no)
               
               pop1=Popup(title="Keep me log in!",content=f1,size_hint=(0.5,0.2))
               pop1.open()

   def yes(self,*args):
      f=open("save.txt","wb")
      detail={"user":uid}
      pickle.dump(detail,f)
      f.close()
      pop1.dismiss()
      s.current="4"
      
   def no(self,*args):
      pop1.dismiss()
      s.current="4"
               
               
               
class Recovery(FloatLayout):
   global id
   def __init__(self,*args,**kwargs):
      super().__init__(*args,**kwargs)
      
      self.l=Label(text="Recovery\n_________",font_size='30sp',size_hint=(1,0.1),pos_hint={'x':0,'y':0.85},color=[0,0.5,1,1])
      self.add_widget(self.l)
      
      self.ll2=Label(color=(0,0.5,1,1),text="User Id:   ",size_hint=(0.6,0.5),font_size="25sp",pos_hint={'x':0,'y':0.50})
      self.add_widget(self.ll2)
      
      self.ett1=TextInput(size_hint=(0.7,0.1),pos_hint={'x':0.18,'y':0.63})
      self.add_widget(self.ett1)
      
      self.but1=Button(text="submit", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.40,'y':0.52})
      self.add_widget(self.but1)
      self.but1.bind(on_press=self.veri)
      
      self.butt=Button(text="sign up", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.40,'y':0.45})
      self.add_widget(self.butt)
      self.butt.bind(on_press=self.first)
         
   def first(self,*args):
      s.current="1"  
       
   def veri(self,*args):
      global id
      finalpath=processdata()
      list=requests.get(finalpath).json()
      id=self.ett1.text
      
         
      if id in list:
            Email_verification(list[self.ett1.text]["name"],list[self.ett1.text]["mail"])
            self.et1=TextInput(hint_text="Enter otp",size_hint=(0.7,0.05),pos_hint={'x':0.18,'y':0.30})
            self.add_widget(self.et1)
            
            self.but2=Button(text="verify", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.40,'y':0.19})
            self.add_widget(self.but2)
            self.but2.bind(on_press=self.newpass)             
      else:
            self.ll3=Label(color=(0,0.5,1,1),text="User Id not registered!",size_hint=(0.73,0.05),font_size="15sp",pos_hint={'x':0,'y':0.58})
            self.add_widget(self.ll3)
      
   def newpass(self,*args):
         if self.et1.text==str(otp):
            s.current="6"
         else:
            self.ll4=Label(color=(0,0.5,1,1),text="wrong otp!",size_hint=(0.55,0.05),font_size="15sp",pos_hint={'x':0,'y':0.26})
            self.add_widget(self.ll4)
            
class setnewpass(FloatLayout):
   global id
   def __init__(self,*args):
      super().__init__(*args)
      
      self.l=Label(text="Set Password\n________________",font_size='30sp',size_hint=(1,0.1),pos_hint={'x':0,'y':0.85},color=(0,0.5,1,1))
      self.add_widget(self.l)
      
      self.pass1=TextInput(hint_text="Enter new password", password=True,size_hint=(0.7,0.05),pos_hint={'x':0.18,'y':0.7})
      self.add_widget(self.pass1)
      
      self.pass2=TextInput(hint_text="confirm password", password=True,size_hint=(0.7,0.05),pos_hint={'x':0.18,'y':0.6})
      self.add_widget(self.pass2)
      
      self.but3=Button(text="verify", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.40,'y':0.5})
      self.add_widget(self.but3)
      self.but3.bind(on_press=self.setpass)
      
      self.but4=Button(text="Log in", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.40,'y':0.43})
      self.add_widget(self.but4)
      self.but4.bind(on_press=self.pagelog)
 
   def pagelog(self,*args):
      s.current="3"
      
   def setpass(self,*args):
       global id
       if self.pass1.text==self.pass2.text:
          new=self.pass1.text
          finalpath=processdata()
          list=requests.get(finalpath).json()
          list[id]["pass"]=new
          store=json.dumps(list)
          requests.put(finalpath,store)
          
          self.ll4=Label(color=(0,0.5,1,1),text="password changed!",size_hint=(0.70,0.05),font_size="15sp",pos_hint={'x':0,'y':0.55})
          self.add_widget(self.ll4) 
       else:
          self.ll4=Label(color=(0,0.5,1,1),text="password is not same!",size_hint=(0.73,0.05),font_size="15sp",pos_hint={'x':0,'y':0.66})
          self.add_widget(self.ll4)    
                              
         
#CLASS FOR WELCOME AFTER LOGIN
class welcome(FloatLayout):
   def __init__(self,*args,**kwargs):
      super().__init__(*args,**kwargs)
      global list
      finalpath=processdata()
      list=requests.get(finalpath).json()
      
      with self.canvas:
               Color(0,0.5,1,1)
               Rectangle(size=(1*w,0.05*h),pos=(0,0))
                  
      self.buttt1=Button(text="Log Out", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.8,'y':0.95})
      self.add_widget(self.buttt1)
      self.buttt1.bind(on_press=self.pagechng)
      
      self.buttt2=Button(text="My Profile", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0,'y':0.95})
      self.add_widget(self.buttt2)
      self.buttt2.bind(on_press=self.myprofile)
      
      self.tinput=TextInput(background_color=(1,1,1,0.2),font_size="20sp",hint_text="Search",size_hint=(0.5,0.05),pos_hint={'x':0.2,'y':0.95})
      self.add_widget(self.tinput)
      
      self.button3=Button(background_normal="search.jpeg",size_hint=(0.1,0.05),pos_hint={'x':0.7,'y':0.95})
      self.add_widget(self.button3)
      self.button3.bind(on_press=self.searchprofile)
      
      
      
   def searchprofile(self,*args):
      global pop4,fl
      suid=self.tinput.text
      
      fl=FloatLayout()
      
      fl.buttt4=Button(size_hint=(0.08,0.04),pos_hint={'x':0.92,'y':1.01}, background_normal="cross.png")
      fl.add_widget(fl.buttt4)
      fl.buttt4.bind(on_press=self.closepop4)
      
      pop4=Popup(auto_dismiss=False,title_color=(0,0.5,1,1),background="white.jpeg",content=fl,title="Search Profile",size_hint=(1,1),pos_hint={'x':0,'y':0}, background_color=(1,1,1,1))
      pop4.open() 

      if uid==suid:
         fl.llll3=Label(text=f"{suid} is your User Id!",size_hint=(1,1),pos_hint={'x':0,'y':0},color=(0,0,0,1))
         fl.add_widget(fl.llll3)
         
      elif suid in list:
         token=list[suid]["token"]
         with fl.canvas:
               Color(0,0.5,1,1)
               Line(ellipse=(w*0.35,0.93*h-w*0.55,w*0.3,w*0.3),width=3)
               Color(0,0.5,1,1)
               Rectangle(size=(0.925*w,0.23*h),pos=(0.0375*w,0.7*h),source="1.jpeg")      
               Color(1,1,1,1)
               self.profile_image2=Ellipse(size=(w*0.3,w*0.3),pos=(w*0.35,0.93*h-w*0.55),source="dp.jpg")
               
         urll="https://firebasestorage.googleapis.com/v0/b/profile-fe70b.appspot.com/o/"+suid+"%2F"+suid+".jpg?alt=media&token="+token
       
         fl.img=AsyncImage(source=urll,on_load=self.loadp)
         
         fl.llll1=Label(text=f"{list[suid]['name']}\n{list[suid]['college']}\n{list[suid]['profession']}\n\n\nSkills:\n_______\n\n{list[suid]['skills']}\n\nAchievements:\n________________\n\n{list[suid]['achievements']}",size_hint=(0.8,0.6),pos_hint={'x':-0.1,'y':0.02},color=(0,0,0,1))
         fl.add_widget(fl.llll1)
         
      
      
      else:
         fl.llll2=Label(text=f"No User found With User Id:- {suid}",size_hint=(1,1),pos_hint={'x':0,'y':0},color=(0,0,0,1))
         fl.add_widget(fl.llll2)     
      
   def loadp(self,*args):
          self.profile_image2.texture=fl.img.texture
          fl.img.reload() 
          
   def closepop4(self,*args):
      pop4.dismiss() 
         
   def editprofile(self,*args):
      global f2,uid,pop2
      f2=FloatLayout()
      
      f2.buttt4=Button(size_hint=(0.08,0.04),pos_hint={'x':0.92,'y':1.01}, background_normal="cross.png")
      f2.add_widget(f2.buttt4)
      f2.buttt4.bind(on_press=self.closepop2)
      
      
      tilist=['Name','headline','city,state','country','summary']
      
      f2.ttt=TextInput(hint_text=tilist[0],text=list[uid]['name'],size_hint=(0.8,0.05),pos_hint={'x':0.1,'y':0.90})
      f2.add_widget(f2.ttt)
         
      f2.ttt1=TextInput(hint_text=tilist[1],text=list[uid]['headline'],size_hint=(0.8,0.05),pos_hint={'x':0.1,'y':0.78})
      f2.add_widget(f2.ttt1)
         
      f2.ttt2=TextInput(hint_text=tilist[2],text=list[uid]['region'],size_hint=(0.8,0.05),pos_hint={'x':0.1,'y':0.66})
      f2.add_widget(f2.ttt2)
      
      f2.ttt3=TextInput(hint_text=tilist[3],text=list[uid]['country'],size_hint=(0.8,0.05),pos_hint={'x':0.1,'y':0.54})
      f2.add_widget(f2.ttt3)
         
      f2.ttt4=TextInput(hint_text=tilist[4],text=list[uid]['summary'],size_hint=(0.8,0.2),pos_hint={'x':0.1,'y':0.27})
      f2.add_widget(f2.ttt4)  
         
      f2.bit=Button(text="save", background_color=(0,0.5,1,1),size_hint=(0.2,0.05),pos_hint={'x':0.4,'y':0.1})
      f2.add_widget(f2.bit)
      f2.bit.bind(on_press=self.savedetail)
      
      pop2=Popup(auto_dismiss=False,title_color=(0,0.5,1,1),background="white.jpeg",content=f2,title="Edit profile",size_hint=(1,1),pos_hint={'x':0,'y':0}) 
      
      pop2.open()
      
   def closepop2(self,*args):
      pop2.dismiss()               
      
   def savedetail(self,*args):
      global f2,uid
           
      finalpath=processdata()
      list=requests.get(finalpath).json()
      list[uid]["name"]=f2.ttt.text
      list[uid]["headline"]=f2.ttt1.text
      list[uid]["region"]=f2.ttt2.text
      list[uid]["country"]=f2.ttt3.text
      list[uid]["summary"]=f2.ttt4.text
      
      store=json.dumps(list)
      requests.put(finalpath,store)
     
      f2.labe=Label(color=(0,0.5,1,1),text="Detailed updated!",size_hint=(1,0.05),pos_hint={'x':0,'y':0.15})
      f2.add_widget(f2.labe) 
      
      
        
   def myprofile(self,*args):
      global f,pop,uid,list
      f=FloatLayout()
      
      token=list[uid]["token"]
      
      with f.canvas:
               Color(0,0.5,1,1)
               Line(ellipse=(w*0.35,0.93*h-w*0.55,w*0.3,w*0.3),width=3)
               Color(0,0.5,1,1)
               Rectangle(size=(0.925*w,0.23*h),pos=(0.0375*w,0.7*h),source="1.jpeg")               
               Color(1,1,1,1)
               self.profile_image=Ellipse(size=(w*0.3,w*0.3),pos=(w*0.35,0.93*h-w*0.55),source="dp.jpg")
              
      url2="https://firebasestorage.googleapis.com/v0/b/profile-fe70b.appspot.com/o/"+uid+"%2F"+uid+".jpg?alt=media&token="+token
       
      try:
         f.img=AsyncImage(source=url2,on_load=self.load1)
      except:
         pass
      
    
      f.lll1=Label(text=f"{list[uid]['name']}\n{list[uid]['headline']}\n{list[uid]['region']},{list[uid]['country']}",size_hint=(0.7,0.2),pos_hint={'x':-0.1,'y':0.40},color=(0,0,0,1),halign="left")
      f.add_widget(f.lll1)
      
      f.button1=Button(text="Upload New Dp",size_hint=(1,0.05),pos_hint={'x':0,'y':0.6}, background_color=(255,255,255,0.1),color=(0,0.5,1,1))
      f.add_widget(f.button1)
      f.button1.bind(on_press=self.opengallary)
      
      f.buttt4=Button(size_hint=(0.08,0.04),pos_hint={'x':0.92,'y':1.01}, background_normal="cross.png")
      f.add_widget(f.buttt4)
      f.buttt4.bind(on_press=self.closepop)
      
      
      f.buttt3=Button(size_hint=(0.1,0.05),pos_hint={'x':0.9,'y':0.50}, background_normal="pencil.jpeg")
      f.add_widget(f.buttt3)
      f.buttt3.bind(on_press=self.editprofile)
      
      pop=Popup(auto_dismiss=False,title_color=(0,0.5,1,1),background="white.jpeg",content=f,title="My Profile",size_hint=(1,1),pos_hint={'x':0,'y':0}, background_color=(1,1,1,1))
      pop.open() 
      
      
   def load1(self,*args):
          self.profile_image.texture=f.img.texture
          f.img.reload() 
          
   def closepop(self,*args):
      pop.dismiss()
          

   def pagechng(self,*args):
      f=open("save.txt","wb")
      f.close()
      s.current="3"   
      
   def opengallary(self,*args):
      global pop3
      self.filechoose=FileChooserIconView(path=".")
      pop3=Popup(title="gallary",content=self.filechoose,size_hint=(1,1),pos_hint={'x':0,'y':0})
      f.add_widget(pop3)
      self.filechoose.bind(on_submit=self.pk)
      
   def pk(self,a,path,b):
               global list
               url="https://firebasestorage.googleapis.com/v0/b/profile-fe70b.appspot.com/o/"+uid+"%2F"+uid+".jpg"

               for i in [".jpg",".png","jpeg"]:
                    if path[0].endswith(i):       
                         files={"media":open(path[0],"rb")}
                         r=requests.post(url,files=files)   
                         data=r.json()
                         data=data["downloadTokens"]
                         
                         d={"token":data}
                         
                         list[uid]["token"]=data
                         store=json.dumps(list)
                         requests.put(finalpath,store)  
                         f.label=Label(color=(0,0.5,1,1),text="Changed successfully! ",size_hint=(1,0.05),pos_hint={'x':0,'y':0.57})
                         f.add_widget(f.label)
                         break   
                              
               else:
                    f2.label1=Label(color=(0,0.5,1,1),text="Select a correct image! ",size_hint=(1,0.05),pos_hint={'x':0,'y':0.57})
                    f.add_widget(f.label1)
               f.remove_widget(pop3)
  
                           
#MAIN  CLASS       
class profileapp(App):
   def build(self):
      return s
      
s=ScreenManager()

s1=Screen(name="1")
s1.add_widget(Profile())

s2=Screen(name="2")
s2.add_widget(verification())

s3=Screen(name="3")
s3.add_widget(Login())

s4=Screen(name="4")
s4.add_widget(welcome())

s5=Screen(name="5")
s5.add_widget(Recovery())

s6=Screen(name="6")
s6.add_widget(setnewpass())


s.add_widget(s1)
s.add_widget(s2)   
s.add_widget(s3)
s.add_widget(s4)
s.add_widget(s5)  
s.add_widget(s6)

try:
   f=open("save.txt","rb")
   data=pickle.load(f)
   global uid 
   uid=data["user"]  
   s.current="4"
except EOFError:
   s.current="1"
except:
   s.current="1"

profileapp().run()
