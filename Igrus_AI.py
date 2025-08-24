if __name__=="__main__":
    try:
        import pyttsx3
        import importlib
        import webbrowser
        import datetime
        import subprocess
        import wikipedia
        import speech_recognition as sr
        import playsound
        import time
        import random
        import pywhatkit
        igrus=pyttsx3.init()
        class mainprogram():
            def __init__(self):
                try:
                    self.cl_space=""
                    with open("reminder.txt","r") as file:
                        for line  in file:
                            self.rem,self.dt=line.strip().split(":")
                            if self.pr_use_code==self.rem:
                                print(self.dt)
                                igrus.say(self.dt)
                                igrus.runAndWait()
                    print("hello how can i help you today")
                    igrus.say("hello how can i help you today")
                    igrus.runAndWait()
                    while True: 
                        with open ("igrus_check.txt","w") as file:
                            file.write(self.cl_space)
                        with open ("Igrus_AI.py","r") as file:
                           self.ibr=file.read()
                        with open ("igrus_check.txt","w") as file:
                            file.write(self.ibr)
                        while True:
                            with open ("igrus_backup.py","r") as file:
                                self.pre_bk=file.read()
                            with open("igrus_check.txt") as file:
                                self.now_ig=file.read()
                            if self.pre_bk == self.now_ig:
                                break
                            if self.pre_bk != self.now_ig:
                                with open ("Igrus_AI.py","w") as file:
                                    file.write(self.pre_bk)
                                    break
                                
                        with open ("protectrem.txt","r") as file:
                            for line in file:
                                self.orig,self.sav_fil=line.strip().split("|-=-|")
                                with open(f"{self.orig}","r")as file:
                                    self.copy_ori=file.read()
                                with open(f"{self.sav_fil}","r") as file:
                                    self.copy_sav_fil=file.read()
                                if self.copy_ori != self.copy_sav_fil:
                                    print("ALERT! changes dected! \n type in clear to deleat the file,preventing it from harming your device if any virus\n type in re_str to reset the program removing newly found content  ")
                                    igrus.say("ALERT! changes dected!  type in clear to deleat the file,preventing it from harming your device if any virus type in re_str to reset the program removing newly found content  ")
                                    igrus.runAndWait()
                                    self.protect_deside=input(":")
                                    if self.protect_deside == "clear":
                                        with open (f"{self.orig}","w") as file:
                                            file.write("")
                                            print("file cleared")
                                            igrus.say("file cleared")
                                            igrus.runAndWait()
                                    if self.protect_deside == "re_str":
                                        with open (f"{self.orig}","w") as file:
                                            file.write(self.copy_sav_fil)
                                            print("file restored succesfully")
                                            igrus.say("file restored succesfully")
                                            igrus.runAndWait()
                                else:
                                    pass
                        self.date_fop=datetime.datetime.now().strftime('%d/%m/%Y')
                        self.time_fop=datetime.datetime.now().strftime('%H:%M')
                        self.date_fop1=self.date_fop.replace("/","_")
                        self.time_fop1=self.time_fop.replace(":","_")
                        self.date_fop2=self.date_fop.replace("/","")
                        self.time_fop2=self.time_fop.replace(":","")
                        self.priv_id=self.date_fop2+self.time_fop2
                        self.pr_use_code=self.date_fop1+self.time_fop1
                        self.recognizer = sr.Recognizer()
                        self.mic = sr.Microphone()
                        self.stop_function = None
                        self.latest_text = ""
                        with open("igp.py","w")as file:
                            file.write("")
                        self.a=False
                        self.r=False
                        self.game=False
                        self.open=False
                        self.message=False
                        self.mensuration=False
                        self.pg=False
                        self.sig=False
                        self.log=False
                        self.priv_continue=False
                        self.game_done=False
                        self.control=""
                        self.taskmanager=""
                        self.commandprompt=""
                        self.powershell=""
                        self.explorer=""
                        self.microsoftedge=""
                        self.phone_modified_india=""
                        self.chrome=""
                        self.firefox=""
                        self.notepad=""
                        self.mspaint=""
                        self.calculator=""
                        self.tr_ver='''self.question:self.user_reunit,'''
                        self.user_input=input("you:")
                        with open("igrus_search_history.txt","w") as file:
                            file.write(self.user_input)
                        self.save=self.user_input
                        self.user_input=self.user_input
                        self.user_input=self.user_input.lower()
                        self.user_input=self.user_input.strip().split(" ")



                        ##input directed condition
                        self.a=True
                        self.user_reunit=" ".join(self.user_input)

                        if self.user_reunit == "search history":
                            self.a=False
                            with open("igrus_search_history.txt","r") as file:
                                self.igrus_history=file.read()
                            print(self.igrus_history)

                        if "remember" in self.user_input:
                            self.a=False
                            self.r=True
                            self.user_input.remove("remember")
                            self.user_reunit=" ".join(self.user_input)
                        if "remember" in self.user_input and "this" in self.user_input:
                            self.a=False
                            self.r=True
                            self.user_input.remove("remember")
                            self.user_input.remove("this")
                            self.user_reunit=" ".join(self.user_input)

                        if "mensuration" in self.user_input:
                            self.a=False
                            self.user_reunit=" ".join(self.user_input)
                            self.mensuration=True

                        if "what" in self.user_input:
                            self.a=True
                            self.user_reunit=" ".join(self.user_input)

                        if "why" in self.user_input:
                            self.a=True
                            self.user_reunit=" ".join(self.user_input)

                        if "where" in self.user_input:
                            self.a=True
                            self.user_reunit=" ".join(self.user_input)

                        if "who" in self.user_input:
                            self.a=True
                            self.user_reunit=" ".join(self.user_input)

                        if "how" in self.user_input:
                            self.a=True
                            self.user_reunit=" ".join(self.user_input)

                        if "what" in self.user_input and "is" in self.user_input:
                            self.a=True
                            self.user_reunit=" ".join(self.user_input)

                        if "message" in self.user_input or "send" in self.user_input and "message" in self.user_input:
                            self.a=False
                            self.message=True
                            self.user_reunit=" ".join(self.user_input)

                        if "open" in self.user_input:
                            self.a=False
                            self.user_input.remove("open")
                            self.open=True
                            self.user_reunit=" ".join(self.user_input)


                        if "play" in self.user_input and "games" in self.user_input:
                            self.a=False
                            self.game=True
                            self.user_reunit=" ".join(self.user_input)

                        if self.user_reunit == "time":
                            self.a=False
                            self.user_reunit=" ".join(self.user_input)
                            igrus.say(f"the time is {datetime.datetime.now().strftime('%H:%M')}")
                            igrus.runAndWait()
                            print(f"the time is {datetime.datetime.now().strftime('%H:%M')}")

                        if self.user_reunit == "date":
                            self.a=False
                            self.user_reunit=" ".join(self.user_input)
                            igrus.say(f"the date is {datetime.datetime.now().strftime('%d/%m/%Y')}")
                            igrus.runAndWait()
                            print(f"the date is {datetime.datetime.now().strftime('%d/%m/%Y')}")

                        if self.user_reunit== "day":
                            self.a=False
                            self.user_reunit=" ".join(self.user_input)
                            igrus.say(f"the day is {datetime.datetime.now().strftime('%A')}")
                            igrus.runAndWait()
                            print(f"the day is {datetime.datetime.now().strftime('%A')}")

                        if "calc" in self.user_input:
                            self.a=False 
                            self.user_input.remove("calc")
                            print(eval(" ".join(self.user_input)))

                        if "play" in self.user_input and "music"  in self.user_input:
                            self.a=False
                            print("music player started")
                            igrus.say("music player started")
                            igrus.runAndWait()
                            print("note: kepp the music in downloads")
                            while True:
                                self.music_input=input("enter the name of the music:")
                                try:
                                    if "format" in self.music_input:
                                        self.formated_music_path=input("enter the path:")
                                        playsound.playsound(self.formated_music_path)
                                        if "stop" in self.formated_music_path:
                                            print("music player stopped")
                                            igrus.say("music player stopped")
                                            igrus.runAndWait()
                                            break 
                                except Exception as e:
                                    print("no such file found")
                                try:
                                    playsound.playsound(f'''C:\\Users\\User\\Downloads\\{self.music_input}.mp3''')
                                    if "stop" in self.music_input:
                                        print("music player stopped")
                                        igrus.say("music player stopped")
                                        igrus.runAndWait()
                                        break  
                                except Exception as e:
                                    print("no such file found")

                        if "reminder" in self.user_input and "date" in self.user_input:
                            self.remember_text=(input("ENTER what to remember:"))
                            self.date_input=(input("enter the date\n"))
                            with open("reminder.txt","a") as file:
                                file.write(f"{self.date_input}:{self.remember_text}\n")
                            self.a=False

                        #self.priv_id
                        if  "private_memory" in self.user_input :
                            self.a=False
                            self.log_sign=input("log_in or signup?")
                            if "sign" in self.log_sign.strip().split(" "):
                                self.sig=True
                            if "log" in self.log_sign.strip().split(" "):
                                self.log=True

                            if self.log==True:
                                while True:
                                    self.sig=False
                                    igrus.say("please enter your id")
                                    igrus.runAndWait()
                                    self.take_id=input("please enter your id")
                                    if self.take_id =="creat":
                                        self.sig=True
                                    igrus.say("please enter your password")
                                    igrus.runAndWait()
                                    self.take_pass=input("please enter your password")
                                    if self.take_pass =="creat":
                                        self.sig=True
                                    if self.sig==True:
                                        pass
                                    else:
                                        with open("priv_memory.txt","r") as file:
                                            for line in file:
                                                self.i,self.p=line.strip().split("*-~~")
                                                if self.i != self.take_id:
                                                    print("your id might not be correct, have no account? type creat in id section or in password section to creat one!")
                                                    igrus.say("your id might not be correct")
                                                    igrus.runAndWait()
                                                if self.p != self.take_pass:
                                                    print("your password might not be correct, have no account? type creat in id section or in password section to creat one!")
                                                    igrus.say("your password might not be correct")
                                                    igrus.runAndWait()
                                                if self.p==self.take_pass and self.i==self.take_id:
                                                    self.priv_continue=True
                                                    break
                                            break



                                        
                            if self.sig==True:
                                print("remember your id will be:")
                                igrus.say("remember your id will be:")
                                igrus.runAndWait()
                                print(self.priv_id)
                                igrus.say("please creat a password to your account")
                                igrus.runAndWait()
                                self.priv_pass=input("please creat a password to your account")
                                with open("priv_memory.txt","a") as file:
                                    file.write(f"{self.priv_id}*-~~{self.priv_pass}\n")
                                with open(self.priv_id+".txt","w") as file:
                                    file.write("")
                                self.take_id=self.priv_id
                                self.priv_continue=True

                            if self.priv_continue==True:
                                while True:
                                    self.priv_input=input("enter your input, enter exit to exit\n:")
                                    if self.priv_input=="exit":
                                        break
                                    if "remember" in self.priv_input:
                                        self.priv_question=(input("creat a question for this answer:"))
                                        self.priv_input=self.priv_input.replace("remember","").strip()
                                        with open("pr_me_help.txt","w") as file:
                                            file.write(f'''\n"{self.priv_question}":"{self.priv_input}"''')
                                        with open("pr_me_help.txt","r") as file:
                                            self.re_mem=file.read()
                                        with open(self.take_id+".py","w") as file:
                                            file.write("")
                                        with open(self.take_id+".py","w") as file:
                                            file.write("priv_mem={\n")
                                            file.write(f"{self.re_mem},\n")
                                            file.write("}")
                                    else:
                                        self.module = importlib.import_module(self.take_id)
                                        self.value = getattr(self.module, 'priv_mem')
                                        print(self.value.get(self.priv_input))


                        if "igrus_file_protect" in self.user_input:
                            self.protect_file=input("enter your file name and type such as \nexample.py or example.txt\n:")
                            with open (f"{self.protect_file}","r")as file:
                                self.pre_program=file.read() 
                            with open (f"{self.pr_use_code}.txt","w")as file:
                                file.write(self.pre_program)
                            with open ("protectrem.txt","a") as file:
                                file.write(f"{self.protect_file}|-=-|{self.pr_use_code}.txt")
                            self.a=False

                        if "shutdown" in self.user_input:
                            igrus.say("Shutting down the system")
                            igrus.runAndWait()
                            subprocess.call("shutdown /s /t 5")
                            self.a=False

                        if "lock" in self.user_input and "system" in self.user_input:
                            igrus.say("Locking the system")
                            igrus.runAndWait() 
                            subprocess.call("rundll32.exe user32.dll,LockWorkStation")
                            self.a=False 

                        if "igrus_file~~info/fetch" in self.user_input:
                            self.a=False 
                            try:
                                while True:
                                    self.hack_file_name=input("enter the file name\nNOTE: the file must be in same folder as this ai\n:")
                                    with open(self.hack_file_name,"r") as file:
                                        for line in file:
                                            if "with" in line and "as" in line:
                                                print(line)  
                                        break
                                self.info_opiniun=input("type e to exit \n i for grtting file info \n a for adding information to file\n c for clearing the file\n").lower()
                                if self.info_opiniun =="e":
                                    break
                                if self.info_opiniun =="a":
                                    try:
                                        while True:
                                            self.file_info_after=input("enter the file name\n enter e to exit\n:")
                                            if self.file_info_after=="e":
                                                break
                                            else:
                                                with open(self.file_info_after,"a") as file:
                                                    self.add_info=input("enter the information you want to add\n")
                                                    file.write(f"{self.add_info}\n")
                                                    print("information added succesfully")
                                    except Exception as e:
                                        print(e)

                                if self.info_opiniun =="c":
                                    try:
                                        while True:
                                            self.file_info_after=input("enter the file name enter e to exit\n:")
                                            if self.file_info_after=="e":
                                                break
                                            with open(self.file_info_after,"w") as file:
                                                file.write(" ")
                                                print("file cleared succesfully")
                                    except Exception as e:
                                        print(e)
                                if self.info_opiniun =="i":
                                    try:
                                        while True:
                                            self.file_info_after_fec=input("enter the file name enter e to exit\n:")
                                            if self.file_info_after_fec=="e":
                                                break
                                            with open(self.file_info_after_fec,"r") as file:
                                                self.final_fetch_output=file.read()
                                                print(self.final_fetch_output)

                                    except Exception as e:
                                        print(e)
                            except Exception as e:
                                print(e)
                        if "wikipedia" in self.user_input and "summary" in self.user_input:
                            self.a=False
                            self.query =input("Enter your query: ")
                            while True:
                                try:
                                    self.lines=int(input("enter the no of sentences you want to read: "))
                                    break
                                except ValueError:
                                    print("Invalid input. Please enter a number.")
                            self.summary = wikipedia.summary(self.query, sentences=self.lines)
                            print("Answer:", self.summary)

                        #function
                        if self.mensuration==True:
                            self.a=False
                            while True:
                                try:
                                    self.dic=(input("enter shape, enter exit to exit :")).lower()
                                    if ("rectangle_p"in self.dic):
                                        def ll(width, length):
                                            self.perimeter = 2 * (length + width)
                                            print("Perimeter is", self.perimeter, "cm")
                                            igrus.say("Perimeter is", self.perimeter, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("Enter the length: "))
                                        self.cc = int(input("Enter the width: "))
                                        ll(self.aa,self.cc)
                                    elif("rectangle_a"in self.dic):
                                            def ll(width, length):
                                                self.area = 2 * (length * width)
                                                print("area is", self.area, "cm")
                                                igrus.say("area is", self.area, "cm")
                                                igrus.runAndWait()
                                            self.aa = int(input("Enter the length: "))
                                            self.cc = int(input("Enter the width: "))
                                            ll(self.cc, self.aa)
                                    elif("square_a"in self.dic):
                                        def ll(side):
                                            self.area= (side*side)
                                            print("area is",self.area, "cm")
                                            igrus.say("area is",self.area, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("Enter the side: "))
                                        ll(self.aa)
                                    elif ("square_p"in self.dic):
                                            def ll(side):
                                                self.perimeter= 4*(side)
                                                print("Perimeter is", self.perimeter, "cm")
                                                igrus.say("Perimeter is", self.perimeter, "cm")
                                                igrus.runAndWait()
                                            self.aa = int(input("Enter the side: "))
                                            ll(self.aa)
                                    elif ("triangle_a"in self.dic):
                                        def ll(width, length):
                                            self.area = 1/2*(length * width)
                                            print("area is", self.area, "cm")
                                            igrus.say("area is", self.area, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("Enter the length: "))
                                        self.cc = int(input("Enter the width: "))
                                        ll(self.cc, self.aa)
                                    elif ("triangle_p"in self.dic):
                                            def ll(side1,side2,side3):
                                                self.perimeter =(side1 + side2 + side3)
                                                print("Perimeter is", self.perimeter, "cm")
                                                igrus.say("Perimeter is", self.perimeter, "cm")
                                                igrus.runAndWait()
                                            self.aa = int(input("side1: "))
                                            self.cc = int(input("side2: "))
                                            self.dd = int(input("side3: "))
                                            ll(self.aa,self.cc,self.dd)
                                    elif("circle_a"in self.dic):
                                        def ll(radius):
                                            self.area = 2*3.14*(radius)
                                            print("area is ", self.area, "cm")
                                            igrus.say("area is ", self.area, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("Enter the radius: "))
                                        ll(self.aa) 
                                    elif ("circle_c"in self.dic):
                                            def ll(radius):
                                                self.circumference = 3.14*(radius*radius)
                                                print("circumference is ",self.circumference, "cm")
                                                igrus.say("circumference is ",self.circumference, "cm")
                                                igrus.runAndWait()
                                            self.aa = int(input("Enter the radius: "))
                                            ll(self.aa)
                                    elif("parallelogram_a"in self.dic):
                                        def ll(width, length):
                                            self.area = (length * width)
                                            print("area is", self.area, "cm")
                                            igrus.say("area is", self.area, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("Enter the length: "))
                                        self.cc = int(input("Enter the width: "))
                                        ll(self.aa,self.cc)
                                    elif("parallelogram_p"in self.dic):
                                            def ll(adjecent_side1, adjecent_side2):
                                                self.perimeter = 2 * (adjecent_side1 +adjecent_side2)
                                                print("Perimeter is", self.perimeter, "cm")
                                                igrus.say("Perimeter is", self.perimeter, "cm")
                                                igrus.runAndWait()
                                            self.aa = int(input("adjecent_side1: "))
                                            self.cc = int(input("adjecent_side2: "))
                                            ll(self.aa,self.cc)
                                    elif("rhombus_a"in self.dic):
                                        def ll(diagnal1, diagnal2):
                                            self.area = 1/2*(diagnal1*diagnal2)
                                            print("area is", self.area, "cm")
                                            igrus.say("area is", self.area, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("diagnal 1: "))
                                        self.cc = int(input("diagnal 2: "))
                                        ll(self.aa,self.cc)
                                    elif ("rhombus_p"in self.dic):
                                            def ll(side):
                                                self.perimeter= 4*(side)
                                                print("Perimeter i5s", self.perimeter, "cm")
                                                igrus.say("Perimeter i5s", self.perimeter, "cm")
                                                igrus.runAndWait()
                                            self.aa = int(input("Enter the side: "))
                                            ll(self.aa)
                                    elif("trapezoid_a"in self.dic):
                                        def ll(base_1,base_2,height):
                                            self.area =1/2*base_1+base_2*height
                                            print("area is", self.area, "cm")
                                            igrus.say("area is", self.area, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("base_1: "))
                                        self.cc = int(input("base_2: "))
                                        self.dd = int(input("height: "))
                                        ll(self.aa,self.cc,self.dd)
                                    elif("trapezoid_p"in self.dic):
                                            def ll(base_1,base_2,non_parallel_saide_1,non_parallel_saide_2):
                                                self.perimeter =(  base_1+ base_2+non_parallel_saide_1+non_parallel_saide_2)
                                                print("Perimeter is", self.perimeter, "cm")
                                                igrus.say("Perimeter is", self.perimeter, "cm")
                                                igrus.runAndWait()
                                            self.aa = int(input("base_1: "))
                                            self.cc = int(input("base_2: "))
                                            self.dd = int(input("non_parallel_saide_1: "))
                                            self.ee = int(input("non_parallel_saide_2: "))
                                            ll(self.aa,self.cc,self.dd,self.ee)
                                    elif("cube_a"in self.dic):
                                        def ll(length):
                                            self.surface_area =6*(length*length)
                                            print("surface area is", self.surface_area, "cm")
                                            igrus.say("surface area is", self.surface_area, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("length: "))
                                        ll(self.aa)
                                    elif("cube_v"in self.dic):
                                            def ll(volume):
                                                self.volumew =(volume*volume*volume)
                                                print("volume is",self.volumew, "cm")
                                                igrus.say("volume is",self.volumew, "cm")
                                                igrus.runAndWait()
                                            self.aa = int(input("length: "))
                                            ll(self.aa)
                                    elif("cuboid_a"in self.dic):
                                        def ll(width,length,height):
                                            self.area =2*length*width+2*length*height+2*width*height
                                            print("surface area is", self.area, "cm")
                                            igrus.say("surface area is", self.area, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("width: "))
                                        self.cc = int(input("length: "))
                                        self.dd = int(input("height: "))
                                        ll(self.aa,self.cc,self.dd)
                                    elif("rhombus_v"in self.dic):
                                            def ll(width,length,height):
                                                self.volume =width*height*length
                                                print("vloume is", self.volume, "cm")
                                                igrus.say("vloume is", self.volume, "cm")
                                                igrus.runAndWait()
                                            self.aa = int(input("width: "))
                                            self.cc = int(input("length: "))
                                            self.dd = int(input("height: "))
                                            ll(self.aa,self.cc,self.dd)
                                    elif("sphere_a"in self.dic):
                                        def ll(radius):
                                            self.area =4*3.14*radius*radius
                                            print(" surfacea area is ", self.area, "cm")
                                            igrus.say(" surfacea area is ", self.area, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("Enter the radius: "))
                                        ll(self.aa) 
                                    elif ("sphere_v"in self.dic):
                                            def ll(radius):
                                                self.volume=4/3*3.14*radius*radius*radius
                                                print("volume  is ",self.volume , "cm")
                                                igrus.say("volume  is ",self.volume , "cm")
                                                igrus.runAndWait()
                                            self.aa = int(input("Enter the radius: "))
                                            ll(self.aa) 
                                    elif("cylinder_a"in self.dic):
                                        def ll(height,radius):
                                            self.area =2*3.14*radius*radius+2*3.14*radius*height
                                            print("surface area is", self.area, "cm")
                                            igrus.say("surface area is", self.area, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("height: "))
                                        self.cc = int(input("radius: "))
                                        ll(self.aa,self.cc)
                                    elif("cylinder_v"in self.dic):
                                        def ll(height,radius):
                                            self.volume =3.14*radius*radius*height
                                            print("volume is", self.volume, "cm")
                                            igrus.say("volume is", self.volume, "cm")
                                            igrus.runAndWait()
                                        self.aa = int(input("height: "))
                                        self.cc = int(input("radius: "))
                                        ll(self.aa,self.cc)
                                    #help_function_system
                                    elif self.dic.startswith("re"):
                                        print("are u thinking about rectangle_a or rectangle_p") 
                                        igrus.say("are you thinking about rectangle_a or rectangle_p")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("sq"):
                                        print("are u thinking about square_a or square_p")
                                        igrus.say("are you thinking about square_a or square_p")
                                        igrus.runAndWait() 
                                    elif self.dic.startswith("tr"):
                                        print("are u thinking about triangle_a or triangle_p")
                                        igrus.say("are u thinking about triangle_a or triangle_p") 
                                        igrus.runAndWait()
                                    elif self.dic.startswith("ci"):
                                        print("are u thinking about circle_a or circle_c") 
                                        igrus.say("are u thinking about circle_a or circle_c")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("pa"):
                                        print("are u thinking about parallelogram_a or parallelogram_p") 
                                        igrus.say("are u thinking about parallelogram_a or parallelogram_p")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("rh"):
                                        print("are u thinking about rhombus_a or rhombus_p") 
                                        igrus.say("are u thinking about rhombus_a or rhombus_p")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("tra"):
                                        print("are u thinking about trapezoid_a or trapezoid_p") 
                                        igrus.say("are u thinking about trapezoid_a or trapezoid_p")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("cubo"):
                                        print("are u thinking about cuboid_a or cuboid_v")
                                        igrus.say("are u thinking about cuboid_a or cuboid_v")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("cub"):
                                        print("are u thinking about cube_a or cube_v")   
                                        igrus.say("are u thinking about cube_a or cube_v")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("sp"):
                                        print("are u thinking about sphere_a or sphere_v")
                                        igrus.say("are u thinking about sphere_a or sphere_v")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("cy"):
                                        print("are u thinking about cylinder_a or cylinder_v")
                                        igrus.say("are u thinking about cylinder_a or cylinder_v")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("r"):
                                        print("are u thinking about rectangle_a or rectangle_p\n rhombus_a or rhombus_p")
                                        igrus.say("are u thinking about rectangle_a or rectangle_p rhombus_a or rhombus_p")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("s"):
                                        print("are u thinking about\nsquare_a or square_p\nsphere_a or sphere_v")
                                        igrus.say("are u thinking about square_a or square_p sphere_a or sphere_v")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("t"):
                                        print("are u thinking about\ntriangle_a or triangle_p\ntrapezoid_a or trapezoid_p")
                                        igrus.say("are u thinking about triangle_a or triangle_p trapezoid_a or trapezoid_p")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("c"):
                                        print("are u thinking about\ncircle_a or circle_c\ncuboid_a or cuboid_v\ncube_a or cube_v")
                                        igrus.say("are u thinking about circle_a or circle_c cuboid_a or cuboid_v cube_a or cube_v")
                                        igrus.runAndWait()
                                    elif self.dic.startswith("p"):
                                        print("are u thinking about\nparallelogram_a or parallelogram_p")
                                        igrus.say("are u thinking about parallelogram_a or parallelogram_p")
                                        igrus.runAndWait()
                                    else:
                                        ("i cant understand what u telling?")
                                        igrus.say("i cant understand what u telling?")
                                        igrus.runAndWait()
                                    if "exit" in self.dic:
                                        break
                                except Exception as e:
                                    print(e)



                        if self.game==True:
                            self.game_choise=input("enter 1 for 1v1 battle enter 2 for prefect guess enter 3 for collect 4\n")
                            igrus.say("enter 1 for 1v1 battle enter 2 for prefect guess enter 3 for collect 4")
                            igrus.runAndWait()
                            if self.game_choise=="1":
                                self.after=False
                                from lot3 import refresh
                                self.complement=("HEY! DO YOU REALLY THINK YOU HAVE THAT?","DUDE! BE CONCIOUS! FOCUS ON THE GAME!","FEELING SLEEPY? BUT YOUR OPPONENTS ARENT WAKE UP!","HEY! WHAT DO YOU WANT ME TO DO?","PUT ON YOUR GLASSES DUDE?","TYPOO?","IS THIS A LITTLR KID PLAYING?","DUDE ARE YOU KIDDING ME?","MAN WAKE UP THATS NOT POSSIBLE")
                                self.p1_hp=50
                                self.p2_hp=50
                                self.p1_energy=50
                                self.p2_energy=50
                                self.player_win=False
                                self.comp_win=False   
                                while True:
                                    if self.p2_energy >=20:
                                        self.opponent_choise=["attack","heal","defend","energy"]
                                    elif self.p2_energy ==15:
                                        self.opponent_choise=["attack","defend","energy"]
                                    elif self.p2_energy ==10:
                                        self.opponent_choise=["attack","defend","energy"]
                                    elif self.p2_energy<=5:
                                        self.opponent_choise=["energy","attack"]
                                    elif self.p2_energy==10 and self.p1_hp==10:
                                        self.opponent_choise={"attack"}
                                    elif self.p1_hp==10:
                                        self.opponent_choise=["attack"]
                                    elif self.p2_hp<=15:
                                        self.opponent_choise=["defend","heal"]
                                    else:
                                        self.opponent_choise=["attack"]
                                    print(f"YOU                                                                                                                                                                                                                                                                                                                                 computer")
                                    print(f"HP:{self.p1_hp}                                                                                                                                                                                                                                                                                                                               HP:{self.p2_hp}")
                                    print(f"ENERGY:{self.p1_energy}                                                                                                                                                                                                                                                                                                                           ENERGY:{self.p2_energy}")
                                    self.player_choise=["attack","heal","defend","energy"]
                                    print(refresh)
                                    while True:
                                        self.player_opiniune=input(f"                                                        WHAT DO YOU WANT TO DO? {self.player_choise}\n                                                                                       ")
                                        time.sleep(1)
                                        if self.player_opiniune in self.player_choise:
                                            break
                                        else:
                                            print(f"                                                                                   {self.complement}")
                                    self.opponent_opiniune = random.choice(self.opponent_choise)
                                    print(f"                                                                             YOUR OPPONENT CHOSE:{self.opponent_opiniune}")
                                    time.sleep(5)
                                    if self.player_opiniune == "attack" and self.opponent_opiniune == "attack":
                                        self.p1_hp=self.p1_hp-10
                                        self.p2_hp=self.p2_hp-10
                                        #
                                        self.p1_energy=self.p1_energy-5
                                        self.p2_energy=self.p2_energy-5
                                    elif self.player_opiniune == "attack" and self.opponent_opiniune == "defend":
                                    
                                        self.p1_hp=self.p1_hp
                                        self.p2_hp=self.p2_hp
                                        #
                                        self.p1_energy=self.p1_energy-5
                                        self.p2_energy=self.p2_energy-10
                                    elif self.player_opiniune=="attack" and self.opponent_opiniune=="heal":
                                    
                                        self.p1_hp=self.p1_hp
                                        self.p2_hp=self.p2_hp-10
                                        self.p2_hp=self.p2_hp+20
                                        #
                                        self.p1_energy=self.p1_energy-5
                                        self.p2_energy=self.p2_energy-20
                                    elif self.player_opiniune=="heal" and self.opponent_opiniune=="attack":
                                    
                                        self.p1_hp=self.p1_hp-10
                                        self.p1_hp=self.p1_hp+20
                                        self.p2_hp=self.p2_hp
                                        #
                                        self.p1_energy=self.p1_energy-20
                                        self.p2_energy=self.p2_energy-5
                                    elif self.player_opiniune=="heal" and self.opponent_opiniune=="defend":
                                    
                                        self.p1_hp=self.p1_hp+20
                                        self.p2_hp=self.p2_hp
                                        #
                                        self.p1_energy=self.p1_energy-20
                                        self.p2_energy=self.p2_energy-10
                                    elif self.player_opiniune=="heal" and self.opponent_opiniune=="heal":
                                    
                                        self.p1_hp=self.p1_hp+20
                                        self.p2_hp=self.p2_hp+20
                                        #
                                        self.p1_energy=self.p1_energy-20
                                        self.p2_energy=self.p2_energy-20
                                    elif self.player_opiniune=="defend" and self.opponent_opiniune=="attack":
                                    
                                        self.p1_hp=self.p1_hp
                                        self.p2_hp=self.p2_hp-10
                                        #
                                        self.p1_energy=self.p1_energy-10
                                        self.p2_energy=self.p2_energy-5
                                    elif self.player_opiniune=="defend" and self.opponent_opiniune=="defend":
                                    
                                        self.p1_hp=self.p1_hp
                                        self.p2_hp=self.p2_hp
                                        #
                                        self.p1_energy=self.p1_energy-10
                                        self.p2_energy=self.p2_energy-10
                                    elif self.player_opiniune=="defend" and self.opponent_opiniune=="heal":
                                    
                                        self.p1_hp=self.p1_hp
                                        self.p2_hp=self.p2_hp+20
                                        #
                                        self.p1_energy=self.p1_energy-10
                                        self.p2_energy=self.p2_energy-20
                                    elif self.player_opiniune=="energy" and self.opponent_opiniune=="attack":
                                        self.p1_hp=self.p1_hp-20
                                        self.p2_hp=self.p2_hp
                                        #
                                        self.p1_energy=self.p1_energy+20
                                        self.p2_energy=self.p2_energy-5
                                    elif self.player_opiniune=="energy" and self.opponent_opiniune=="defend":
                                        self.p1_hp=self.p1_hp-10
                                        self.p2_hp=self.p2_hp
                                        #
                                        self.p1_energy=self.p1_energy+20
                                        self.p2_energy=self.p2_energy-10
                                    elif self.player_opiniune=="energy" and self.opponent_opiniune=="heal":
                                        self.p1_hp=self.p1_hp-10
                                        self.p2_hp=self.p2_hp+20
                                        #
                                        self.p1_energy=self.p1_energy+20
                                        self.p2_energy=self.p2_energy-20
                                    elif self.player_opiniune=="energy" and self.opponent_opiniune=="energy":
                                        self.p1_hp=self.p1_hp-10
                                        self.p2_hp=self.p2_hp-10
                                        #
                                        self.p1_energy=self.p1_energy+20
                                        self.p2_energy=self.p2_energy+20
                                    elif self.player_opiniune=="attack" and self.opponent_opiniune=="energy":
                                        self.p1_hp=self.p1_hp
                                        self.p2_hp=self.p2_hp-10
                                        #
                                        self.p1_energy=self.p1_energy-5
                                        self.p2_energy=self.p2_energy+20
                                    elif self.player_opiniune=="heal" and self.opponent_opiniune=="energy":
                                        self.p1_hp=self.p1_hp+20
                                        self.p2_hp=self.p2_hp-10
                                        #
                                        self.p1_energy=self.p1_energy-20
                                        self.p2_energy=self.p2_energy+20
                                    elif self.player_opiniune=="defend" and self.opponent_opiniune=="energy":
                                        self.p1_hp=self.p1_hp 
                                        self.p2_hp=self.p2_hp-10
                                        #
                                        self.p1_energy=self.p1_energy-10
                                        self.p2_energy=self.p2_energy+20
                                    if (self.p1_hp<=0) or (self.p1_energy<=0):
                                        self.comp_win=True   
                                    elif (self.p2_hp<=0) or (self.p2_energy<=0):
                                        self.player_win=True
                                    if self.player_win:
                                        print("YOU WIN!")
                                        self.after=True
                                    elif self.comp_win:
                                        print("YOU LOSE!")
                                        self.after=True
                                    if self.after==True:
                                        self.a=input("PRESS 1 TO PLAY AGAIN OR 2 TO EXIT\n")
                                        if self.a == "2":
                                            print("THANK YOU FOR PLAYING!")
                                            break
                                    print(refresh,refresh)

                            elif self.game_choise=="2":
                                with open("score_ip.txt","r")as file:
                                    self.reminder=file.read()
                                print(f"HELLO PLAYER!, I HAVE CHOSEN A NUMBER FROM 1 TO 1000 TRY TO GUESS IT?\nTHE LOWER THE SCORE THE HIGHER THE VALUE IT HAS\nLAST HIGH SCORE{self.reminder}")
                                self.cc=random.randint(1,1000)
                                self.a=0
                                while True:
                                    self.pc=int(input("enter:"))
                                    if self.pc > self.cc :
                                        print("your value is more than my choise")
                                        self.a=self.a+1
                                        igrus.say("your value is more than my choise")
                                        igrus.runAndWait()
                                    if self.pc < self.cc:
                                        print("your value is less than my choise")
                                        self.a=self.a+1
                                        igrus.say("your value is less than my choise")
                                        igrus.runAndWait()
                                    if self.pc == self.cc :
                                        print(f"you guessed it right you win!\n your score:{self.a}")
                                        with open("score_ip.txt","w") as file:
                                            file.write(self.a)
                                        break
                            else:
                                print("please select from the given options")
                                igrus.say("please select from the given options")
                                igrus.runAndWait()

                            if self.game_choise=="3":
                                self.complement=("HEY! DO YOU REALLY THINK YOU HAVE THAT?","DUDE! BE CONCIOUS! FOCUS ON THE GAME!","FEELING SLEEPY? BUT YOUR OPPONENTS ARENT WAKE UP!","HEY! WHAT DO YOU WANT ME TO DO?","PUT ON YOUR GLASSES DUDE?","TYPOO?","IS THIS A LITTLR KID PLAYING?","DUDE ARE YOU KIDDING ME?","MAN WAKE UP THATS NOT POSSIBLE")
                                self.p1=[]
                                self.p2=[]
                                self.p3=[]
                                self.p4=[]
                                self.card_shuffel=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
                                print("suffeling cards!")
                                time.sleep(2)
                                for i in range(4):
                                    self.send=random.choice(self.card_shuffel)
                                    self.p1.append(self.send)
                                    self.card_shuffel.remove(self.send)
                                    self.send=random.choice(self.card_shuffel)
                                    self.p2.append(self.send)
                                    self.card_shuffel.remove(self.send)
                                    self.send=random.choice(self.card_shuffel)
                                    self.p3.append(send)
                                    self.card_shuffel.remove(self.send)
                                    self.send=random.choice(self.card_shuffel)
                                    self.p4.append(self.send)
                                    self.card_shuffel.remove(self.send)
                                if self.p1.count(1) == 4 or self.p1.count(2) == 4 or self.p1.count(3) == 4 or self.p1.count(4) == 4:
                                    print("YOU ARE LUCKY! YOU COLLECTED ALL THE CARDS!")
                                    self.game_done=True
                                #
                                elif self.p2.count(1) == 4 or self.p2.count(2) == 4 or self.p2.count(3) == 4 or self.p2.count(4) == 4:
                                    print("p2 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                    self.game_done=True
                                #
                                elif self.p3.count(1)==4 or self.p3.count(2) == 4 or self.p3.count(3) == 4 or self.p3.count(4) == 4:
                                    print("p3 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                    self.game_done=True
                                #
                                elif self.p4.count(1)==4 or self.p4.count(2) == 4 or self.p4.count(3) == 4 or self.p4.count(4) == 4:
                                    print("p4 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                    self.game_done=True

                                while True:
                                    while True:
                                        try:
                                            print(f"{self.p1}\nYOUR CARDS!")
                                            self.pass_select=int(input("ENTER WHICH CARD TO PASS ON TO P2?\n"))
                                            if self.pass_select in p1:
                                                self.p1.remove(self.pass_select)
                                                self.p2.append(self.pass_select)
                                                break
                                            else:
                                                self.respond=random.choices(self.complement)
                                                print(self.respond)
                                                time.sleep(5)
                                        except ValueError:
                                            self.respond=random.choice(self.complement)
                                            print(self.respond)
                                    print("p2 got your card!")
                                    time.sleep(1)
                                    print("p2 IS PASSING THE CARD!")
                                    time.sleep(1)
                                    if self.p1.count(1) == 4 or self.p1.count(2) == 4 or self.p1.count(3) == 4 or self.p1.count(4) == 4:
                                        print("YOU ARE LUCKY! YOU COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                        break
                                    #
                                    elif self.p2.count(1) == 4 or self.p2.count(2) == 4 or self.p2.count(3) == 4 or self.p2.count(4) == 4:
                                        print("p2 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                        break
                                    #
                                    elif self.p3.count(1)==4 or self.p3.count(2) == 4 or self.p3.count(3) == 4 or self.p3.count(4) == 4:
                                        print("p3 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                        break
                                    #
                                    elif self.p4.count(1)==4 or self.p4.count(2) == 4 or self.p4.count(3) == 4 or self.p4.count(4) == 4:
                                        print("p4 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                        break
                                    self.p2_send=random.choice(self.p2)
                                    self.p2.remove(self.p2_send)
                                    self.p3.append(self.p2_send)
                                    #
                                    print("p3 got p2's card")
                                    time.sleep(1)
                                    print("p3 IS PASSING THE CARD!")
                                    time.sleep(1)
                                    if self.p1.count(1) == 4 or self.p1.count(2) == 4 or self.p1.count(3) == 4 or self.p1.count(4) == 4:
                                        print("YOU ARE LUCKY! YOU COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    #
                                    elif self.p2.count(1) == 4 or self.p2.count(2) == 4 or self.p2.count(3) == 4 or self.p2.count(4) == 4:
                                        print("p2 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    #
                                    elif self.p3.count(1)==4 or self.p3.count(2) == 4 or self.p3.count(3) == 4 or self.p3.count(4) == 4:
                                        print("p3 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    #
                                    elif self.p4.count(1)==4 or self.p4.count(2) == 4 or self.p4.count(3) == 4 or self.p4.count(4) == 4:
                                        print("p4 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    self.p3_send=random.choice(self.p3)
                                    self.p3.remove(self.p3_send)
                                    self.p4.append(self.p3_send)
                                    #
                                    print("p4 got p3's card")
                                    time.sleep(1)
                                    print("p4 IS PASSING THE CARD!")
                                    time.sleep(1)
                                    if self.p1.count(1) == 4 or self.p1.count(2) == 4 or self.p1.count(3) == 4 or self.p1.count(4) == 4:
                                        print("YOU ARE LUCKY! YOU COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    #
                                    elif self.p2.count(1) == 4 or self.p2.count(2) == 4 or self.p2.count(3) == 4 or self.p2.count(4) == 4:
                                        print("p2 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    #
                                    elif self.p3.count(1)==4 or self.p3.count(2) == 4 or self.p3.count(3) == 4 or self.p3.count(4) == 4:
                                        print("p3 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    #
                                    elif self.p4.count(1)==4 or self.p4.count(2) == 4 or self.p4.count(3) == 4 or self.p4.count(4) == 4:
                                        print("p4 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    self.p4_send=random.choice(self.p4)
                                    self.p4.remove(self.p4_send)
                                    self.p1.append(self.p4_send)
                                    print("YOU RECIVED P4's CARD!")
                                    if self.p1.count(1) == 4 or self.p1.count(2) == 4 or self.p1.count(3) == 4 or self.p1.count(4) == 4:
                                        print("YOU ARE LUCKY! YOU COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    #
                                    elif self.p2.count(1) == 4 or self.p2.count(2) == 4 or self.p2.count(3) == 4 or self.p2.count(4) == 4:
                                        print("p2 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    #
                                    elif self.p3.count(1)==4 or self.p3.count(2) == 4 or self.p3.count(3) == 4 or self.p3.count(4) == 4:
                                        print("p3 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    #
                                    elif self.p4.count(1)==4 or self.p4.count(2) == 4 or self.p4.count(3) == 4 or self.p4.count(4) == 4:
                                        print("p4 WAS FOUND LUCKY! HE COLLECTED ALL THE CARDS!")
                                        self.game_done=True
                                    if self.game_done==True:
                                        print("GAME OVER!")
                                        break
                                    
                                    
                        if self.open==True:

                            self.control="control.exe"
                            self.taskmanager="taskmgr.exe"
                            self.commandprompt="cmd.exe"
                            self.powershell="powershell.exe"
                            self.explorer="explorer.exe"
                            self.microsoftedge="msedge.exe"
                            self.chrome="chrome.exe"
                            self.firefox="firefox.exe"
                            self.notepad="notepad.exe"
                            self.mspaint="mspaint.exe"
                            self.calculator="calc.exe"
                            if self.user_reunit=="control pannel":
                                subprocess.Popen(self.control)
                            if self.user_reunit=="taskmanager":
                                subprocess.Popen(self.taskmanager)
                            if self.user_reunit=="command prompt":
                                subprocess.Popen(self.commandprompt)
                            if self.user_reunit=="powershell":
                                subprocess.Popen(self.powershell)
                            if self.user_reunit=="explorer":
                                subprocess.Popen(self.explorer)
                            if self.user_reunit=="microsoft edge":
                                subprocess.Popen(self.microsoftedge)
                            if self.user_reunit=="chrome":
                                subprocess.Popen(self.chrome)
                            if self.user_reunit=="firefox":
                                subprocess.Popen(self.firefox)
                            if self.user_reunit=="notepad":
                                subprocess.Popen(self.notepad)
                            if self.user_reunit=="mspaint" or self.user_reunit=="microsoft paint":
                                subprocess.Popen(self.mspaint)
                            if self.user_reunit=="calculator":
                                subprocess.Popen(self.calculator)

                        if self.message==True:
                            while True:
                                try:
                                    igrus.say(f"enter your phone number")
                                    igrus.runAndWait()
                                    self.phone_no=int(input("remember if wrong phone no the message wont be sent\n"))
                                    self.phone_no=str(self.phone_no)
                                    if len(self.phone_no)==10:
                                       break
                                    else:
                                        igrus.say("please give the correct information")
                                        igrus.runAndWait()
                                except ValueError:
                                    print("the phone number must contain only numbers and not any othe special charecters")
                                    igrus.say("the phone number must contain only numbers and not any othe special charecters")
                                    igrus.runAndWait()
                            igrus.say("please enter what to send")
                            igrus.runAndWait() 
                            self.message_info=input("please enter what to send\n")
                            self.phone_modified_india=("+91"+self.phone_no)
                            pywhatkit.sendwhatmsg_instantly(self.phone_modified_india, self.message_info, wait_time=40, tab_close=True)

                        if self.r==True:
                            igrus.say("please creat a question for this answer")
                            igrus.runAndWait()
                            self.question=input("please creat a question for this answer\n")
                            print("thanks i will remember this")
                            igrus.say("thanks i will remember this")
                            igrus.runAndWait()
                            with open("abhi.txt","a")as file:
                                file.write(f'''"{self.question}":"{self.user_reunit}",\n''')

                        ##function

                        if self.a==True:
                            with open("abhi.txt","r")as file:
                                self.pre_dict=file.read()

                            with open("igp.py","a") as file:
                                file.write("ig_mem={\n")
                                file.write(f"{self.pre_dict}")
                                file.write("}")

                            from igp import ig_mem
                            print(ig_mem.get(self.user_reunit))
                            igrus.say(ig_mem.get(self.user_reunit))
                            igrus.runAndWait()
                            if ig_mem.get(self.user_reunit) == None:
                                webbrowser.open(f"https://www.google.com/search?q={self.user_reunit}") 
                except Exception as et:

                    with open ("igrus_backup.py","r") as file:
                        self.pre_bk=file.read()
                    with open ("Igrus_AI.py","w") as file:
                        file.write(self.pre_bk)

        
    except Exception as e:
        with open ("igrus_backup.py","r") as file:
            pre_bk=file.read()
            with open ("Igrus_AI.py","w") as file:
                file.write(pre_bk)
    run=mainprogram()
