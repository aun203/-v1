
# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_lengthimport time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six,ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata
from gtts import gTTS                                                                                 
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#==============================================================================#
#line = LINE()                                                                                        
#line = LINE("เมล","พาส")                                                                             
line = LINE()                                                                                         
line.log("Auth Tokenprint ("Login Succes")
: " + str(line.authToken))                                                       
#line.log("Timeline Token : " + str(line.tl.channelAccessToken))

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

oepoll = OEPoll(line)
#call = Call(line)                                                                                    
readOpen = codecs.open("read.json","r","utf-8")                                                       
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
Rfu = [line]
Exc = [line]
lineMID = line.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID]
Family=["u0035a5a6c5ae9d30c9a0992ecbc39395",lineMID]
admin=['u0035a5a6c5ae9d30c9a0992ecbc39395',lineMID]
RfuFamily = RfuBot + Family

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#
msg_dict = {}

settings = {
    "autoAdd": False,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":10},
    "autoLeave": True,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": True,
    "checkSticker": False,
    "checkContact": False,
    "checkPost": False,
    "kickMention": False,
    "potoMention": True,
    "delayMention": False,                                                                                
    "lang":"JP",
    "Wc": False,
    "Lv": False,
    "Nk": False,
    "Api": False,
    "Aip": False,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "gift":False,
    "likeOn":False,
    "timeline":False,
    "commentOn":True,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "changeGroupPicture": [],
    "changePictureProfile":False,
    "unsendMessage": False,
    "autoJoinTicket": False,
    "welcome":"สวัสดีคนมาใหม่\n\nตั้งข้อความต้อนรับด้วยคับ\nVҜ ŚẾL₣ВΌŦ",
    "kick":"งิเตะทมอยยย😂\nVҜ ŚẾL₣ВΌŦ",
    "bye":"ไปซ่ะละ ลาก่อยยย\nVҜ ŚẾL₣ВΌŦ",
    "Respontag":"แทคทำไมเดะจับเย็ดตูด!",
    "eror":"คุณใช้คำสั่งผิด สั่งบอทอีกครั้ง!",
    "spam":{},
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message1":"แอดมารัก หรือ แอดมารัน😊",
    "message":"บัญชีนี้ถูกป้องกันโดย VҜ ŚẾL₣ВΌŦ ระบบได้บล็อคคุณอัตโนมัติ!",
    "comment":"""ŚẾL₣ВΌŦ BY:
╔══════════════┓
╠       VҜ ŚẾL₣ВΌŦ
╚══════════════┛""",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": True,
}

RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": True,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}

myProfile = {
        "displayName": "",
        "statusMessage": "",
        "pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

user1 = lineMID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile()
backup = line.getProfile()
backup.dispalyName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ",".","ปลิว"]
fukgerMessage = ["ควย","หี","แตด","เย็ดแม่","เย็ดเข้","ค.วย","สัส","เหี้ย","ไอ้เหี้ย","พ่อมึงตาย","ไอ้เลว","ระยำ","ชาติหมา","หน้าหี","เซลกาก","พ่องตาย","ส้นตีน","แม่มึงอ่ะ","แม่มึงดิ","พ่อมึงดิ"]

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#
