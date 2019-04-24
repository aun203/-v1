
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
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps$
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\$
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentTyp$
    except Exception as error:
        logError(error)

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                line.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Mention {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def myhelp():
    myHelp = """╔══════════════┓
╠     VҜ ŚẾL₣ВΌŦ
╚══════════════┛
╔══════════════┓
╠❋►Me ↔คอนแทค
╠❋►Help1 ↔คำสั่งทั่วไป
╠❋►Help2 ↔คำสั่งกลุ่ม
╠❋►Help3 ↔คำสั่งตั้งค่า
╠❋►Help4 ↔ คำสั่งมีเดีย
╠❋►Help5 ↔ คำสั่งสิริ
╠❋►Help6 ↔ คำสั่งแปลภาษา
╠❋►บอทออน
╠❋►แทค
╠❋►ทีมบอท
╠❋►Creator
╠❋►Sp
╰═❋VҜ ŚẾL₣ВΌŦ »"""
    return myHelp

def listgrup():
    listGrup = """╔══════════════┓
╠     ❋คำสั่งกลุ่ม❋
╚══════════════┛
╔══════════════┓
╠❋►ข้อมูลกลุ่ม
╠❋►ชื่อกลุ่ม
╠❋►ไอดีกลุ่ม
╠❋►รูปกลุ่ม
╠❋►สมาชิก
╠❋►เปิดลิ้ง
╠❋►ปิดลิ้ง
╠❋►Gurl
╠❋►ลิ้ง
╠❋►แทค
╠❋►แทคล่องหน
╠❋►ไอดีล่องหน
╠❋►คทล่องหน
╠❋►เปิดแอบ
╠❋►ปิดแอบ
╠❋►มอง
╠❋►ไครอ่าน
╠❋►ยกเลิก
╠❋►โทร
╠❋►เชิญคลอ
╠❋►ดึง
╠❋►เปลี่ยนรูปกลุ่ม
╠❋►ประกาศ
╠❋►Vk @
╠❋►หีแหก @
╠❋►แบนหมด
╠❋►แบน @
╠❋►ยกเลิก @
╠❋►ล้างแบน @
╠❋►เตะแบน
╠❋►เช็คไอดี
╰═❋VҜ ŚẾL₣ВΌŦ »"""
    return listGrup

def socmedia():
    socMedia = """╔══════════════┓
╠    ❋คำสั่งมีเดี่ย❋
╚══════════════┛
╔══════════════┓
╠❋►หารูป
╠❋►รูปการ์ตูน
╠❋►ยูทูป
╠❋►เพลง
╠❋►ค้นหา
╠❋►หนัง
╠❋►ภาพ
╠❋►วีดีโอ
╠❋►เทส
╠❋►เพลงมา
╠❋►สปีด
╠❋►ไอจี
╠❋►เวลา
╠❋►ขอหื่น
╰═❋VҜ ŚẾL₣ВΌŦ »"""
    return socMedia

def helpset():
    helpSet = """╔══════════════┓
╠    ❋คำสั่งSELF❋
╚══════════════┛
╔══════════════┓
╠❋►Me
╠❋►คท
╠❋►Mid
╠❋►รูป
╠❋►ปก
╠❋►วีดีโอ
╠❋►ข้อมูล
╠❋►กลุ่มทั้งหมด
╠❋►ชื่อ
╠❋►ตัส
╠❋►คท @
╠❋►รูป @
╠❋►ปก @
╠❋►ชื่อ @
╠❋►ตัส @
╠❋►ข้อมูล @
╠❋►ไอดี
╠❋►Sp ↔ Speed
╠❋►เปลี่ยนดิส
╠❋►ไวรัส
╠❋►ปิดไฟ
╠❋►Creator
╠❋►ทีมบอท
╠❋►ผส
╠❋►บอทออน
╠❋►ข้อความเข้า
╠❋►ข้อความออก
╠❋►ข้อความเตะ
╠❋►ข้อความแอด
╠❋►ข้อความแอด2
╠❋►N
╠❋►เพื่อน
╠❋►เช็คบล็อค
╠❋►ไอดีเพื่อน
╠❋►ลบแชท
╠❋►ปิดบอท
╠❋►รัน @
╠❋►รันแชท
╠❋►รันแชท
╠❋►แบน @ ↔ ปลด @
╠❋►เลียนแบบ @
╠❋►ยกเลิก @
╠❋►Nutmic on ↔ off
╠❋►เชคเลียนแบบ
╠❋►เตะแบน
╠❋►ชื่อ;
╠❋►ตัส;
╠❋►Spam on ↔ off
╰═❋BY: VҜ ŚẾL₣ВΌŦ"""
    return helpSet

def helpsetting():
    helpSetting = """╔══════════════┓
╠ ❋«คำสั่งตั้งค่าบอท»❋
╚══════════════┛
╔══════════════┓
╠❋►เช็ค
╠❋►B on ↔ B off
╠❋►เปิดเข้า ↔ ปิดเข้า
╠❋►แชท on ↔แชท off
╠❋►อ่าน on ↔อ่าน off
╠❋►เปิดมุด ↔ ปิดมุด
╠❋►ติ้ก on ↔ ติ้ก off
╠❋►เปิดเสือก ↔ ปิดเสือก
╠❋►เปิดแทค ↔ ปิดแทค
╠❋►เปิดแทค2 ↔ ปิดแทค2
╠❋►เปิดแทค3 ↔ ปิดแทค3
╠❋►เตะแทค ↔ ปิดเตะแทค
╠❋►เปิดคท ↔ ปิดคท
╠❋►เปิดแชร์ ↔ ปิดแชร์
╠❋►เปิดตรวจ ↔ ปิดตรวจ
╠❋►เปิดพูด ↔ ปิดพูด
╠❋►ตั้งแอด;
╠❋►ตั้งแทค;
╠❋►คอมเม้น;
╠❋►ตั้งออก;
╠❋►ตั้งเข้า;
╠❋►เปิดกัน ↔ ปิดกัน
╠❋►กันลิ้ง ↔ ปิดกันลิ้ง
╠❋►กันยก ↔ ปิดกันยก
╠❋►กันเชิญ ↔ ปิดกันเชิญ
╠❋►กันกลุ่ม ↔ ปิดกันกลุ่ม
╠❋►กันเข้า ↔ ปิดกันเข้า
╠❋►เปิดหมด ↔ ปิดหมด
╰══❋BY: VҜ ŚẾL₣ВΌŦ """
    return helpSetting

def helptexttospeech():
    helpTextToSpeech =   """╔══════════════┓
╠    ❋«สั่งสิริพูด»❋
╚══════════════┛
╔══════════════┓
╠❋►พูด พิมคำที่ต้องการ
╠❋► af : แอฟริกัน
╠❋► sq : อัลเบเนีย
╠❋► hy : อาเมเนีย
╠❋► bn : เบนจาลี
╠❋► zh-cn : จีน
╠❋► zh-tw : ใต้หวัน
╠❋► cs : เช็ก
╠❋► nl : ดัช
╠❋► en : อังกฤษ
╠❋► en-us : สหรัฐ
╠❋► el : กรีก
╠❋► id : อินโดนีเซีย
╠❋► it : อิตาลี
╠❋► ja : ญี่ปุ่น
╠❋► ko : เกาหลี
╠❋► la : ลาติน
╠❋► ro : โรมาเนีย
╠❋► ru : รัสเซีย
╠❋► sr : เซอเบียร์
╠❋► th : ไทย
╠❋► vi : เวียดนาม
╰═❋BY: VҜ ŚẾL₣ВΌŦ »

「วิธีใช้ : พูด พี่คะหนูเงี่ยน」"""
    return helpTextToSpeech

def helplanguange():
    helpLanguange =    """╔══════════════┓
╠ ❋«คำสั่งแปลภาษา»❋
╚══════════════
╔══════════════┓
╠❋► af : แอฟริกัน
╠❋► sq : อัลเบเนีย
╠❋► ar : อราบิค
╠❋► hy : อาเมเนีย
╠❋► bn : บังการี่
╠❋► bs : บอสเนีย
╠❋► bg : บังแกเรีย
╠❋► zh-cn : จีน
╠❋► zh-tw : ใต้หวัน
╠❋► cs : เช็ก
╠❋► nl : ดัช
╠❋► en : อังกฤษ
╠❋► et : เอสโตเนียน
╠❋► el : กรีก
╠❋► id : อินโดนีเซีย
╠❋► ga : ไอริส
╠❋► it : อิตาลี
╠❋► ja : ญี่ปุ่น
╠❋► kn : แคนาดา
╠❋► la : ลาติน
╠❋► lv : ลัตเวีย
╠❋► ms : มาเลเซีย
╠❋► mt : มอลเตส
╠❋► mn : มองโกเลีย
╠❋► my : พม่า
╠❋► fa : เปอร์เซีย
╠❋► pt : โปรตุเกศ
╠❋► ro : โรมาเนีย
╠❋► ru : รัสเซีย
╠❋► th : ไทย
╠❋► zu : ซูลู
╰═❋BY: VҜ ŚẾL₣ВΌŦ »

「วิธีใช้ : Tr-th ตามด้วยคำที่จะแปล」"""
    return helpLanguange
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.blockContact(op.param1)
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("^^",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)
#        if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
        if op.type == 24:
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if settings["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = line.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 line.sendText(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จ")
                                 break
                             elif invite in settings["blacklist"]:
                                 line.sendText(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 line.sendText(msg.to,"ใช้คำสั่ง!, \n➡ล้างดำ➡ดึง" )
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     line.findAndAddContactsByMid(target)
                                     line.inviteIntoGroup(msg.to,[target])
                                     line.sendText(msg.to,"เชิญคนนี้สำเร็จแล้ว : \n➡" + _name)
                                     settings["winvite"] = False
                                     break
                                 except:
                                     try:
                                         line.findAndAddContactsByMid(invite)
                                         line.inviteIntoGroup(op.param1,[invite])
                                         settings["winvite"] = False
                                     except:
                                         line.sendText(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นไดว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         settings["winvite"] = False
                                         break

            if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if ".พูด " in msg.text.lower():
                    spl = re.split(".พูด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                if text.lower() == 'คำสั่ง':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                elif text.lower() == 'help1':
                    helpSet = helpset()
                    line.sendMessage(to, str(helpSet))
                    sendMessageWithMention(to, lineMID)
                elif text.lower() == 'help2':
                    listGrup = listgrup()
                    line.sendMessage(to, str(listGrup))
                elif text.lower() == 'help3':
                    helpSetting = helpsetting()
                    line.sendMessage(to, str(helpSetting))
                elif text.lower() == 'help4':
                    socMedia = socmedia()
                    line.sendMessage(to, str(socMedia))
                elif text.lower() == 'help5':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'help6':
                    helpLanguange = helplanguange()
                    line.sendMessage(to, str(helpLanguange))
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "ŚẾL₣ВΌŦ ŚPЄЄĐ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s ต่อวินาที ] [ " % (elapsed_time) + str(int(round((tim$
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, "ŚẾL₣ВΌŦ ŚPЄЄĐ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s ต่อวินาที ] [ " % (elapsed_time) + str(int(round((tim$
                elif text.lower() == 'รีบอท':
                    line.sendMessage(to, "➠กำลังรีบอท รอสักครู่ ❋")
                    restartBot()
                  elif text.lower() == 'บอทออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "ŚẾL₣ВΌŦ ÓŅLÍŇỀ\n {}".format(str(runtime)))
                elif text.lower() == 'ข้อมูล':
                    try:
                        arr = []
                        owner = "u0035a5a6c5ae9d30c9a0992ecbc39395"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[ ❋ VҜ ŚẾL₣ВΌŦ ❋ ]"
                        ret_ += "\n╠❥ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠❥ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠❥ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠❥ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ Status ] \n═ {}".format(contact.statusMessage)
                        ret_ += "\n╠❥ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[ ❋ VҜ ŚẾL₣ВΌŦ ❋]"
                        line.sendContact(to, owner)
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#========================  line.sendMessage(to, "❋รีบอทเสร็จแล้ว\nกดลิ้งเพื่อล็อคอินอีกครั้ง\nและตั้งค่าใหม่ด้วยคับพรี้")
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = line.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    line.kickoutFromGroup(msg.to,[target])
                                    line.findAndAddContactsByMid(target)
                                    line. inviteIntoGroup(msg.to,[target])
                                except:
                                    pass
                elif "โทร" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile()
.mid])
                    line.sendMessage(msg.to,"➠เชิญเข้าร่วมการโทรสำเร็จ (｡◕‿◕｡) ")
                elif "ยกเลิก" == msg.text.lower():
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            line.cancelGroupInvitation(msg.to,[_mid])
                        line.sendMessage(to,"ยกเลิกค้างเชิญแล้ว (｡◕‿◕｡) " )
#===========
                elif "สปีด" == msg.text.lower():
                    line.sendMessage(to,"「ความเร็ว...」\n███▒39%\n██████▒69%\n██████████▒99%\n0.0000000000000000 second")
                    line.sendMessage(to,"0.0000000000000000 second")
                    line.sendMessage(to,"(｡◕‿◕｡)")
#===========     
                
