############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import BOTTOM, HORIZONTAL, NO, RIGHT, TOP, VERTICAL, W, X, Y, Frame, Scrollbar, ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
import os
import subprocess
############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)

###################################################################################

def contact():
    mess._show(title='المطورين', message="تم الاعداد من قبل ابطال كلية النخبة")

###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='خطأ', message='لم يتم ايجاد الخوارزمية frontalface_default.xml')
        window.destroy()

###################################################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('كلمة المرور القديمة لم توجد', 'قم بادخال كلمة مرور جديدة ادناه', show='*')
        if new_pas == None:
            mess._show(title='لم يتم الحفظ', message='لم يتم تحديد كلمة مرور')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='تم الحفظ', message='تم حفظ كلمة المرور')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='خطأ', message='قم بكتابة تأكيد كلمة المرور')
            return
    else:
        mess._show(title='خطأ', message='كلمة المرور القديمة غير صحيحة')
        return
    mess._show(title='تم الحفظ', message='تم تغيير كلمة المرور')
    master.destroy()

###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False,False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='    كلمة المرور القديمة',bg='white',font=('times', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
    old.place(x=180,y=10)
    lbl5 = tk.Label(master, text='   كلمة المرور الجديدة', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='اعد كتابة كلمة المرور الجديدة', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cancel=tk.Button(master,text="الغاء", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="حفظ", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('لا توجد كلمة مرور قديمة', 'ادخل كلمة المرور الجديدة ادناه', show='*')
        if new_pas == None:
            mess._show(title='لم يتم ادخال كلمة مرور', message='لم يتم وضع كلمة مرور')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='تم الحفظ', message='تم حفظ كلمة المرور الجديدة بنجاح')
            return
    password = tsd.askstring('كلمة مرور', 'قم بأدخال كلمة المرور Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='كلمة المرور خطأ', message='ادخلت كلمة مرور خطأ')

######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "تعليمات: قم بكتابة رقم القيد والاسم ثم التقط الصورة وبعدها احفظ السجل"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "تعليمات: قم بكتابة رقم القيد والاسم ثم التقط الصورة وبعدها احفظ السجل"
    message1.configure(text=res)

def clear3():
    txt3.delete(0, 'end')
    res = "تعليمات: قم بكتابة رقم القيد والاسم ثم التقط الصورة وبعدها احفظ السجل"
    message1.configure(text=res)

#######################################################################################

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME','', 'DEPT']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    dept=(txt3.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
            cv2.imshow('Taking', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "تم التقاط صورة للقيد رقم  : " + Id
        row = [serial, '', Id, '', name, '',dept]
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "ادخل اسم صحيح"
            message.configure(text=res)

########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='لم يتم تسجيل طلاب', message='يجب تسجيل طلاب اولاً')
        return
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "تم حفظ السجل بنجاح"
    message1.configure(text=res)
    sum()
    clear()
    clear2()
    clear3()

############################################################################################3

def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

##############################################################

def sum():
    res=0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                res = res + 1
        res = (res // 2) - 1
        csvFile1.close()
    else:
        res = 0
    message.configure(text='مجموع الطلاب في قاعدة البيانات الان  : '+str(res))

###########################################################################################


def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
    if exists3:
        recognizer.read("TrainingImageLabel\Trainner.yml")
    else:
        mess._show(title='ملف التدريب مفقود', message='قم بالضغط على حفظ الملف لاعادة الاعداد')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name','','DEPT', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists1:
        df = pd.read_csv("StudentDetails\StudentDetails.csv")
    else:
        mess._show(title='ملف مفقود', message='ملف تفاصيل الطلاب مفقود')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                cc=df.loc[df['SERIAL NO.'] == serial]['DEPT'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                ee=str(cc)
                ee=ee[2:-2]
                attendance = [str(ID), '', bb, '',ee,'', str(date), '', str(timeStamp)]

            else:
                Id = 'Unknown'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Camera', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
    if exists:

        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
        csvFile1.close()
    else:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)
        csvFile1.close()
                    
    csvFile1.close()
    cam.release()
    cv2.destroyAllWindows()

######################################## USED STUFFS ############################################
    
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'كانون الثاني',
      '02':'شباط',
      '03':'اذار',
      '04':'نيسان',
      '05':'ايار',
      '06':'حزيران',
      '07':'تموز',
      '08':'اب',
      '09':'ايلول',
      '10':'تشرين الاول',
      '11':'تشرين الثاني',
      '12':'كانون الاول'
      }

######################################## GUI FRONT-END ###########################################

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("نظام الحضور والغياب")
window.configure(background='#265073')

frame1 = tk.Frame(window, bg="#00aeff")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="مشروع نظام الحضور والغياب للطلاب" ,fg="white",bg="#265073" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text = day+"-"+ month +"-"+year+"  |  ", fg="orange",bg="#265073" ,width=55 ,height=1,font=('times', 22, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="orange",bg="#265073" ,width=55 ,height=1,font=('times', 22, ' bold '))
clock.pack(fill='both',expand=1)
tick()

head2 = tk.Label(frame2, text="                       واجهة تسجيل طالب جديد                           ", fg="black",bg="#ECF4D6" ,font=('times', 17, ' bold ') )
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="                          واجهة تسجيل الحضور                              ", fg="black",bg="#ECF4D6" ,font=('times', 17, ' bold ') )
head1.place(x=0,y=0)

txt = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
txt.place(x=30, y=90)

lbl = tk.Label(frame2, text="رقم القيد",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 15, ' bold ') )
lbl.place(x=80, y=60)

txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=30, y=150)

lbl2 = tk.Label(frame2, text="اسم الطالب",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 15, ' bold '))
lbl2.place(x=80, y=120)

txt3 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
txt3.place(x=30, y=210)

lbl3 = tk.Label(frame2, text="القسم",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 15, ' bold '))
lbl3.place(x=80, y=180)

message1 = tk.Label(frame2, text="تعليمات: قم بكتابة رقم القيد والاسم ثم التقط الصورة وبعدها احفظ السجل" ,bg="#00aeff" ,fg="yellow"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
message1.place(x=7, y=33)

message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
message.place(x=7, y=440)

lbl3 = tk.Label(frame1, text="الحضور",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(x=100, y=95)



sum()





##################### MENUBAR #################################

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='تغيير كلمة المرور', command = change_pass)
filemenu.add_command(label='المطورين', command = contact)
filemenu.add_command(label='الخروج',command = window.destroy)
menubar.add_cascade(label='مساعدة',font=('times', 29, ' bold '),menu=filemenu)

################## TREEVIEW ATTENDANCE TABLE ####################

def show_attendance():
    root = tk.Tk()
    root.title("سجل الحضور لهذا اليوم")
    width = 900
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=900)
    TableMargin.pack(side=tk.TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

    tree = ttk.Treeview(TableMargin, columns=("ID", "NAME","DETP", "DATE", "TIME"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('ID', text="القيد", anchor=W)
    tree.heading('NAME', text="الاسم", anchor=W)
    tree.heading('NAME', text="القسم", anchor=W)
    tree.heading('DATE', text="التاريخ", anchor=W)
    tree.heading('TIME', text="الوقت", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=150)
    tree.column('#4', stretch=NO, minwidth=0, width=150)
    tree.column('#5', stretch=NO, minwidth=0, width=150,)
    tree.pack()

    file_path = "Attendance\Attendance_" + date + ".csv"
    with open(file_path) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            id = row['Id']
            sname = row['Name']
            sdate = row['DEPT']
            sdept = row['Date']
            stime = row['Time']
            tree.insert("", 0, values=(id, sname,sdept, sdate, stime))

    root.mainloop()

# ... (existing code)
clearButton = tk.Button(frame2, text="مسح", command=clear  ,fg="black"  ,bg="#BE3144"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
clearButton.place(x=335, y=90)
clearButton2 = tk.Button(frame2, text="مسح", command=clear2  ,fg="black"  ,bg="#BE3144"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton2.place(x=335, y=150)    
clearButton2 = tk.Button(frame2, text="مسح", command=clear3  ,fg="black"  ,bg="#BE3144"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton2.place(x=335, y=210) 
takeImg = tk.Button(frame2, text="التقاط صورة", command=TakeImages  ,fg="white"  ,bg="#265073"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=30, y=300)
trainImg = tk.Button(frame2, text="حفظ السجل", command=psw ,fg="white"  ,bg="#265073"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trainImg.place(x=30, y=380)
trackImg = tk.Button(frame1, text="تسجيل حضور طالب", command=TrackImages  ,fg="black"  ,bg="#9AD0C2"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=30,y=50)
quitWindow = tk.Button(frame1, text="الخروج من التطبيق", command=window.destroy  ,fg="black"  ,bg="#BE3144"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)
showAttendance = tk.Button(frame1, text="عرض حضور اليوم", command=show_attendance, fg="black", bg="#9AD0C2", width=35, height=1, activebackground="white", font=('times', 15, ' bold '))
showAttendance.place(x=30, y=100)
##################### END ######################################
window.configure(menu=menubar)
window.mainloop()

####################################################################################################


