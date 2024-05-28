from os import system
from tkinter import *
from os import sys

class morseCode:
    
    def __init__(self):
          self.win=Tk()                   
          self.win.title("Morse Code")   
          self.win.geometry("1362x768")  
          self.win.configure(bg='#EFF2C0') 
          self.message=""
          self.text=""
          self.output=""
          self.result=""
          self.output2=""
          self.result2=""
         

    def MORSE_CODE_DICT(self):

        MORSE_CODE_DICT={'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ',':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-'}

        return MORSE_CODE_DICT
    
    
    def to_morse_code(self):

        
        self.runtime+=1
        if self.runtime>1:  
            self.destroyf2()

        MORSE_CODE_DICT = self.MORSE_CODE_DICT()
        self.msg_label=Label(self.win,text="Masukkan Kalimat :",font="Ariel 15 normal",bg='#EFF2C0',fg="black")
        self.msg_label.place(x=200,y=300)
        
        self.msg_field=Entry(self.win,width=30,font="Ariel 15 bold",bg='#A4BAB7',fg='#A52422')
        self.msg_field.place(x=380,y=300)
        
        
        def conv():
            self.text=self.msg_field.get()
            
            if len(self.text)>=1:      
               
                self.op_active=1  
                morse_code=""
                
                for letter in self.text:
                    if letter==' ':
                        morse_code+=' '
                        continue
                    morse_code+=MORSE_CODE_DICT[letter.upper()]+' '
    
                self.output=Label(self.win,text="Output:-",font="times 25 bold",bg='#EFF2C0',fg="black")
                self.output.place(x=100,y=400)
                
                self.result=Text(self.win,height=4,width=45,font="Ariel 35 normal",bg='#A52422',fg="black")
                self.result.insert("0.0",morse_code)
                self.result.place(x=100,y=450)
        
        self.convert=Button(self.win,text="Convert",font="Ariel 15 bold",bg='#A4BAB7',fg='black',command=conv,cursor="hand2",borderwidth=5)
        self.convert.place(x=750,y=290)


        def reset_field():
            if len(self.text)>0:            
                self.msg_field.delete(0,END)
                
            if self.op_active==1:             
                self.output.destroy()
                self.result.destroy()

        self.reset=Button(self.win,text="Reset",font="Ariel 15 bold",bg='#A4BAB7',fg='black',command=reset_field,cursor="hand2",borderwidth=5)
        self.reset.place(x=880,y=290)

    
    def to_text(self):
        
        
        self.runtime+=1    
        if self.runtime>1:
            self.destroyf1()

        MORSE_CODE_DICT = self.MORSE_CODE_DICT()

        self.msg_label2=Label(self.win,text="Masukkan Sandi Morse :",font="Ariel 15 normal",bg='#EFF2C0',fg="black")
        self.msg_label2.place(x=200,y=300)
        
        self.msg_field2=Entry(self.win,width=30,font="Ariel 15 bold",bg='#A4BAB7',fg='#A52422')
        self.msg_field2.place(x=420,y=300)

        
        def conv():
            self.message=self.msg_field2.get()
            
            if len(self.message)>=1:     
                
                self.op_active=1   
                self.message += ' '
                decipher = '' 
                citext = '' 
                for letter in self.message: 
                    if (letter != ' '): 
                        i = 0
                        citext += letter 
                    else: 
                        i += 1
                        if i == 2 : 
                            decipher += ' '
                        else: 
                            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                            citext = ''
    
                self.output2=Label(self.win,text="Output:-",font="times 25 bold",bg='#EFF2C0',fg="black")
                self.output2.place(x=100,y=400)
                
                self.result2=Text(self.win,height=7,width=80,font="Ariel 20 normal",bg='#A52422',fg="black")
                self.result2.insert("0.0",decipher)
                self.result2.place(x=100,y=450) 

        self.convert2=Button(self.win,text="Convert",font="Ariel 15 bold",bg='#A4BAB7',fg='black',command=conv,cursor="hand2",borderwidth=5)
        self.convert2.place(x=780,y=290)
        

        def reset_field():
            if len(self.message)>0:         
                self.msg_field2.delete(0,END)
                
            if self.op_active==1:           
                self.output2.destroy()
                self.result2.destroy()

        self.reset2=Button(self.win,text="Reset",font="Ariel 15 bold",bg='#A4BAB7',fg='black',command=reset_field,cursor="hand2",borderwidth=5)
        self.reset2.place(x=920,y=290)
    

    
    def destroyf1(self):
        self.msg_field.delete(0,END)
        self.reset.destroy()
        self.msg_label.destroy()
        self.msg_field.destroy()
        self.convert.destroy()
        
        
        if self.op_active==1:
            self.output.destroy()
            self.result.destroy()
    
    def destroyf2(self):
        self.msg_field2.delete(0,END)
        self.reset2.destroy()
        self.msg_label2.destroy()
        self.msg_field2.destroy()
        self.convert2.destroy()
        
        if self.op_active==1:
            self.output2.destroy()
            self.result2.destroy()


    def main(self):
        self.runtime=0  
        self.op_active=0  


        self.heading=Label(self.win,text="Morse Code Conversion",bg='#EFF2C0',fg='BLACK',font="helvetica 35 bold")
        self.heading.place(x=20,y=20)         
        
        
        self.opt1=Button(self.win,text="From Text to Morse Code",font="Ariel 15 bold",bg='#A4BAB7',fg='black',command=self.to_morse_code,cursor="hand2")
        self.opt1.place(x=200,y=100)
        

        self.opt2=Button(self.win,text="From Morse Code to Text",font="Ariel 15 bold",bg='#A4BAB7',fg='black',command=self.to_text,cursor="hand2")
        self.opt2.place(x=200,y=150)


        self.opt3=Button(self.win,text="Exit",width=21,font="Ariel 15 bold",bg='#A4BAB7',fg="black",command=sys.exit,cursor="hand2")
        self.opt3.place(x=200,y=200)
        
        input()

obj=morseCode()     
obj.main()          
tkinter.mainloop()  