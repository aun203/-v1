
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
Family=["u85f20b0f0f3530349275159332f74882",lineMID]
admin=['u85f20b0f0f3530349275159332f74882',lineMID]
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
    "welcome":"สวัสดีคนมาใหม่\n\nตั้งข้อความต้อนรับด้วยคับ\n➢❍பꪔ🔝",
    "kick":"งิเตะทมอยยย😂\n➢❍பꪔ🔝",
    "bye":"ไปซ่ะละ ลาก่อยยย\n➢❍பꪔ🔝",
    "Respontag":"รักคนแทค (➢❍பꪔ🔝)!",
    "eror":"คุณใช้คำสั่งผิด สั่งบอทอีกครั้ง!",
    "spam":{},
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message1":"แอดมารัก หรือ แอดมารัน😊",
    "message":"บัญชีนี้ถูกป้องกันโดย ➢❍பꪔ🔝 ระบบได้บล็อคคุณอัตโนมัติ!",
    "comment":"""➢❍பꪔ🔝 BY:
╔══════════════┓
╠       ➢❍பꪔ🔝
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
╠     ➢❍பꪔ🔝
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
╰═❋➢❍பꪔ🔝 »"""
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
╰═❋➢❍பꪔ🔝 »"""
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
╰═❋➢❍பꪔ🔝 »"""
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
╰═❋BY: ➢❍பꪔ🔝"""
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
╰══❋BY: ➢❍பꪔ🔝 """
    return helpSetting

def helptexttospeech():
    helpTextToSpeech =   """╔══════════════┓
╠    ❋«สั่งสิริพูด»❋
╚══════════════┛
╔══════════════┓
╠❋►พูด พิมคำที่ต้องการ
╠❋► ขี้เกียดเขียนต่อ
╰═❋BY: ➢❍பꪔ🔝 »

「วิธีใช้ : พูด ➢❍பꪔ🔝」"""
    return helpTextToSpeech

def helplanguange():
    helpLanguange =    """╔══════════════┓
╠ ❋«คำสั่งแปลภาษา»❋
╚══════════════
╔══════════════┓
╠❋► ขี้เกียด เขียน
╰═❋BY: ➢❍பꪔ🔝 »

「วิธีใช้ :ปิดใช้งาน」"""
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
                    line.sendMessage(to, "➢❍பꪔ🔝")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s ต่อวินาที ] [ " % (elapsed_time) + str(int(round((tim$
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, "➢❍பꪔ🔝")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s ต่อวินาที ] [ " % (elapsed_time) + str(int(round((tim$
                elif text.lower() == 'รีบอท':
                    line.sendMessage(to, "➠กำลังรีบอท รอสักครู่ ❋")
                    restartBot()
                  elif text.lower() == 'บอทออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "➢❍பꪔ🔝\n {}".format(str(runtime)))
                elif text.lower() == 'ข้อมูล':
                    try:
                        arr = []
                        owner = "u0035a5a6c5ae9d30c9a0992ecbc39395"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[ ❋ ➢❍பꪔ🔝 ❋ ]"
                        ret_ += "\n╠❥ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠❥ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠❥ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠❥ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ Status ] \n═ {}".format(contact.statusMessage)
                        ret_ += "\n╠❥ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[ ❋ ➢❍பꪔ🔝 ❋]"
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
                elif "เทส" == msg.text.lower():
                    line.sendMessage(to,"ŚẾL₣ВΌŦLÍŇỀ\n(｡◕‿◕｡)")
                    line.sendMessage(to,"LOADING:▒...0%")
                    line.sendMessage(to,"█▒... 10.0%")
                    line.sendMessage(to,"██▒... 20.0%")
                    line.sendMessage(to,"███▒... 30.0%")
                    line.sendMessage(to,"████▒... 40.0%")
                    line.sendMessage(to,"█████▒... 50.0%")
                    line.sendMessage(to,"██████▒... 60.0%")
                    line.sendMessage(to,"███████▒... 70.0%")
                    line.sendMessage(to,"████████▒... 80.0%")
                    line.sendMessage(to,"█████████▒... 90.0%")
                    line.sendMessage(to,"███████████..100.0%")
                    line.sendMessage(to,"(｡◕‿◕｡)\n➢❍பꪔ🔝บอทยังทำงานคับท่าน😁")
#==============================================================================#
                elif "n" == msg.text.lower():
                    msg.contentType = 13
                    line.sendMessage(to, "=========================")
                    line.sendContact(to, "u85f20b0f0f3530349275159332f74882")
"=========================")
#===========
                elif "เพลงมา" == msg.text.lower():
                    line.sendMessage(to,"บ่แมนหมาวัดแล้วกะบ่ได้ใจนาง\nเลียหีจนครางกะดักใจนางไว้บ่ได้\nเย็ดดีปานได๋เ$ด้าหลายได้ยินบ่\nรอเด้าอยู่เด้อออออ..แคมแดง")
#==============================================================================#
                elif "creator" == msg.text.lower():
                    line.sendMessage(to,"CREATOR ➢❍பꪔ🔝\n(｡◕‿◕｡)")
                    line.sendContact(to, "u85f20b0f0f3530349275159332f74882")
                elif "ไวรัส" == msg.text.lower():
                    line.sendMessage(to, "หยุด ขอให้อยู่ในความสงบ")
                    line.sendContact(to, "u85f20b0f0f3530349275159332f74882',")
                elif "ทีมบอท" == msg.text.lower():
                    msg.contentType = 13
                    line.sendMessage(to, "ADMIN \n (｡◕‿◕｡)")
                    line.sendContact(to, "u85f20b0f0f3530349275159332f74882")
#==============================================================================#
                elif text.lower() == 'เช็ค':
                    try:
                        ret_ = "╔════[ ❋การตั้งค่า❋ ]═════┓"
                        if settings["autoAdd"] == True: ret_ += "\n╠❋ ออโต้บล็อคเปิด ✔"
                        else: ret_ += "\n╠❋ ออโต้บล็อคปิด   ✘ "
                        if settings["autoJoinTicket"] == True: ret_ += "\n╠❋ มุดลิ้งเปิด ✔"
                        else: ret_ += "\n╠❋ มุดลิ้งปิด ✘ "
                        if settings["autoJoin"] == True: ret_ += "\n╠❋ เข้ากลุ่มออโต้เปิด ✔"
                        else: ret_ += "\n╠❋ เข้ากลุ่มออโต้ปิด ✘ "
                        if settings["Api"] == True: ret_ += "\n╠❋ ข้อความApiเปิด ✔"
                        else: ret_ += "\n╠❋ ข้อความApiปิด ✘ "
                        if settings["Aip"] == True: ret_ += "\n╠❋ ตรวจคำสั่งบินเปิด✔"
                        else: ret_ += "\n╠❋ ตรวจคำสั่งบินปิด ✘ "
                        if settings["Wc"] == True: ret_ += "\n╠❋ ข้อความต้อนรับเปิด ✔"
                        else: ret_ += "\n╠❋ ข้อความต้อนรับปิด  ✘ "
                        if settings["Lv"] == True: ret_ += "\n╠❋ ข้อความคนออกเปิด ✔"
                        else: ret_ += "\n╠❋ ข้อความคนออกปิด ✘ "
                        if settings["Nk"] == True: ret_ += "\n╠❋ ข้อความแจ้งเตือนคนลบเปิด ✔"
                        else: ret_ += "\n╠❋ ข้อความแจ้งเตือนคนลบปิด ✘ "
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠❋ ปฏิเสธกลุ่มเชิญที่มีสมาชิกต่ำกว่า: $
                        else: ret_ += "\n╠❋ ปฏิเสธกลุ่มเชิญปิด    ✘ "                                     $
                        if settings["autoLeave"] == True: ret_ += "\n╠❋ ออกแชทรวมออโต้เปิด✔"
                        else: ret_ += "\n╠❋ ออกแชทรวมออโต้ปิด ✘ "
                        if settings["autoRead"] == True: ret_ += "\n╠❋ อ่านออโต้เปิด ✔"
                        else: ret_ += "\n╠❋ อ่านออโต้ปิด ✘ "
                        if settings["checkContact"] == True: ret_ += "\n╠❋ อ่านคทเปิด ✔"
                        else: ret_ += "\n╠❋ อ่านคทปิด   ✘ "
                        if settings["checkPost"] == True: ret_ += "\n╠❋ เช็คโพสเปิด ✔"
                        else: ret_ += "\n╠❋ เช็คโพสปิด    ✘ "
                        if settings["checkSticker"] == True: ret_ += "\n╠❋ เช็คStickerเปิด ✔"
                        else: ret_ += "\n╠❋ เช็คStickerปิด  ✘ "
                        if settings["detectMention"] == True: ret_ += "\n╠❋ ตอบกลับคนแทคเปิด ✔"
                        else: ret_ += "\n╠❋ ตอบกลับคนแทคปิด ✘ "
                        if settings["potoMention"] == True: ret_ += "\n╠❋ แสดงภาพ+คท คนแทคเปิด ✔"
else: ret_ += "\n╠❋ แทคกลับคนแทคปิด ✘ "
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n╠❋ กันเชิญเปิด ✔"
                        else: ret_ += "\n╠❋ กันเชิญปิด ✘ "
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n╠❋ กันยกเชิญเปิด ✔"
                        else: ret_ += "\n╠❋ กันยกเชิญปิด ✘ "
                        if RfuProtect["protect"] == True: ret_ += "\n╠❋ ป้องกันเปิด ✔"
                        else: ret_ += "\n╠❋ ป้องกันปิด ✘ "
                        if RfuProtect["linkprotect"] == True: ret_ += "\n╠❋ ป้องกันเปิดลิ้งเปิด ✔"
                        else: ret_ += "\n╠❋ ป้องกันเปิดลิ้งปิด ✘ "
                        if RfuProtect["Protectguest"] == True: ret_ += "\n╠❋ ป้องกันสมาชิกเปิด ✔"
                        else: ret_ += "\n╠❋ ป้องกันสมาชิกปิด ✘ "
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n╠❋ ป้องกันคนนอกเข้ากลุ่ม ✔"
                        else: ret_ += "\n╠❋ ป้องกันคนนนอกเข้ากลุ่ม ✘ "                                    $
                        ret_ += "\n╚════[ ➢❍பꪔ🔝 ]═════┛"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == 'b on':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "❥เปิดไช้งาน ออโต้บล็อค ❋")
                elif text.lower() == 'b off':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "❥ปิด ออโต้บล็อค ❋")
                elif text.lower() == 'เปิดเข้า':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "❥เปิดเข้ากลุ่มออโต้ ❋")
                elif text.lower() == 'ปิดเข้า':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "❥ปิดเข้ากลุ่มออโต้ ❋")
                elif "gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,str(settings["eror"]))
                                else:
                                    line.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to, " สมาชิกในกลุ่มที่ไม่ถึง" + strnum + "จะถูกปฏิเสธคำเ$
                                else:
                                    line.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,str(settings["eror"]))
                        else:
                                line.sendText(msg.to,"Bizarre ratings")                              $
                elif text.lower() == 'แชท on':
                    settings["autoLeave"] = Truesettings["autoLeave"] = True
                    line.sendMessage(to, "❥ออกแชทรวมอัตโนมัติ ❋")
                elif text.lower() == 'แชท off':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "❥ปิดออกแชทรวม ❋")
                elif text.lower() == 'อ่าน on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "❥อ่านแชท อัตโนมัติ ❋")
                elif text.lower() == 'อ่าน off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "❥ปิดอ่านแชทอัตโนมัติ ❋")
                elif text.lower() == 'ติ้ก on':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "❥เปิดระบบเช็คสติ้กเกอร์ ❋")
                elif text.lower() == 'ติ้ก off':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "❥ปิดระบบเช็คสติ้กเกอร์ ❋")
                elif text.lower() == 'เปิดมุด':
                    settings["autoJoinTicket"] = True
                    line.sendMessage(to, "❥เปิดระบบมุดลิ้ง ❋")
                elif text.lower() == 'ปิดมุด':
                    settings["autoJoinTicket"] = False
                    line.sendMessage(to, "❥ปิดระบบมุดลิ้ง ❋")
                elif text.lower() == 'เปิดเสือก':
                    settings["unsendMessage"] = True
                    line.sendMessage(to, "❥unsendMessage  enabled ❋")
                elif text.lower() == 'ปิดเสือก':
                    settings["unsendMessage"] = False
                    line.sendMessage(to, "❥unsendMessage disabled ❋")
#==============================================================================#
                elif text.lower() == 'คท':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == 'me':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == 'ผส':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, "u0035a5a6c5ae9d30c9a0992ecbc39395")
                elif text.lower() == 'mid':
                    line.sendMessage(msg.to,"❥MID❋👇\n\n" +  lineMID)
                elif text.lower() == 'ชื่อ':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"❥ชื่อคุณ❋👇\n\n" + me.displayName)
                elif text.lower() == 'ตัส':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"❥สเตตัส❋👇\n\n" + me.statusMessage)
                elif text.lower() == 'รูป':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'วีดีโอ':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus$
                elif text.lower() == 'ปก':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)
                    line.sendImageWithURL(msg.to, cover)
                elif text.lower() == 'คอมเม้น':
                    line.sendMessage(msg.to,str(settings["comment"]))
                elif text.lower() == 'ข้อความเข้า':
                    line.sendMessage(msg.to, str(settings["welcome"]))
                elif text.lower() == 'ข้อความออก':
                    line.sendMessage(msg.to, str(settings["bye"]))
                elif text.lower() == 'ข้อความเตะ':
                    line.sendMessage(msg.to, str(settings["kick"]))
                elif text.lower() == 'ข้อความแอด':
                    line.sendMessage(msg.to, str(settings["message"]))
                elif text.lower() == 'ข้อความแอด2':
                    line.sendMessage(msg.to, str(settings["message1"]))
                elif text.lower() == 'ข้อความแทค':
                    line.sendMessage(msg.to, str(settings["Respontag"]))
                elif text.lower() == 'แทคล่องหน':
                    gs = line.getGroup(to)
                    targets = []                
		    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(to, "❥ไม่มีคนใส่ร่องหนในกลุ่มนี้ ❋")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == 'ไอดีล่องหน':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "❥ไม่มีmidคนใส่ร่องหนในกลุ่มนี้ ❋")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)
                elif text.lower() == 'คทล่องหน':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "❥ไม่มีคนใส่ร่องหนในกลุ่มนี้ ❋")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("ไอดี "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                       names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ ❥Mid User❋ ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ ❥Display Name❋ ]\n" + contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ ❥ สเตตัส ❋ ]\n{}" + contact.statusMessage)
     		elif msg.text.lower().startswith("รูป "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureSt$
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("วีดีโอ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureSt$
                            line.sendImageWithURL(msg.to, str(path))
		elif msg.text.lower().startswith("ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
#==========================================
		elif msg.text.lower().startswith("ข้อมูล "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, contact.displayName)
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, contact.statusMessage)
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ">"
                        for ls in lists:
                            ret_ += ls
                        line.sendMessage(msg.to, str(ret_))
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
		
		elif "โพส " in msg.text:
                    tl_text = msg.text.replace("โพส ","")
                    line.sendText(msg.to,"line://home/post?userMid="+lineMID+"&postId="+line.new_pos
t(tl_text)["result"]["post"]["postInfo"]["postId"])
                elif "copy " in msg.text:
                  if msg._from in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = line.getContact(target)
                            X = contact.displayName
                            profile = line.getProfile()
                            profile.displayName = X
                            line.updateProfile(profile)
                            line.sendMessage(msg.to, "Success...")
                        #---------------------------------------
                            Y = contact.statusMessage
                            lol = line.getProfile()
                            lol.statusMessage = Y
                            line.updateProfile(lol)
                        #---------------------------------------
                            P = contact.pictureStatus
                            hun = line.getProfile()
                            hun.pictureStatus = P
                            line.updateProfile(hun)
                        except Exception as e:
                            line.sendMessage(msg.to, "Failed!")
                            print (e)

		elif msg.text in ["คืนร่าง"]:
                    try:
                        #line.updateProfile.pictureStatus(backup.pictureStatus)
                        line.updateProfile.statusMessage(backup.statusMessage)
                        line.updateProfile.displayName(backup.displayName)
                        line.sendMessage(msg.to, "กลับร่างเดิมแล้ว")
                    except Exception as e:
                        line.sendText(msg.to, str (e))

                elif msg.text in ["allprotect on",".เปิดกทม"]:
                        settings["kickMention"] = True
                        settings["Aip"] = False
                        RfuProtect["protect"] = True
                        RfuProtect["cancelprotect"] = True
                        RfuProtect["inviteprotect"] = True
                        RfuProtect["linkprotect"] = True
                        RfuProtect["Protectguest"] = True
                        RfuProtect["Protectjoin"] = True
                        line.sendText(msg.to,"❥ระบบป้องกันทั้งหมดเปิด ❋")

                elif msg.text in ["allprotect off",".ปิดกทม"]:
                        settings["kickMention"] = False
                        settings["Aip"] = False
                        RfuProtect["protect"] = False
                        RfuProtect["cancelprotect"] = False
                        RfuProtect["inviteprotect"] = False
                        RfuProtect["linkprotect"] = False
                        RfuProtect["Protectguest"] = False
                        RfuProtect["Protectjoin"] = False
                        line.sendText(msg.to,"❥ระบบป้องกันทั้งหมดปิด ❋")
		
		elif msg.text in ["Allmsg on",".เปิดข้อความ"]:
                        settings["Wc"] = True
                        settings["Lv"] = True
                        settings["Nk"] = True
                        settings["autoRead"] = True
                        settings["checkSticker"] = True
                        settings["checkContact"] = True
                        settings["checkPost"] = True
                        settings["potoMention"] = True
                        settings["detectMention"] = True
                        settings["delayMention"] = True
                        settings["Api"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด เปิด👌")

                elif msg.text in ["Allmsg off",".ปิดข้อความ"]:
                        settings["Wc"] = False
                        settings["Lv"] = False
                        settings["Nk"] = False
                        settings["autoRead"] = True
                        settings["checkSticker"] = False
                        settings["checkContact"] = False
                        settings["checkPost"] = False
                        settings["detectMention"] = False
                        settings["potoMention"] = False
                        settings["delayMention"] = False
                        settings["Api"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด ปิด👌")
#==============================================================================#
		elif msg.text.lower().startswith("เลียนแบบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"❥เลียนแบบ สำเร็จ ❋")
                            break
                        except:
                            line.sendMessage(msg.to,"ผิดพลาด!")
                            break
                elif msg.text.lower().startswith("ยกเลิก "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"❥ยกเลิกการเลียนแบบ ❋")
                            break
                        except:
                            line.sendMessage(msg.to,"ผิดพลาด !!")
                            break
                elif text.lower() == 'เชคเลียนแบบ':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"❥ ไม่พบ ❋")
                    else:
                        mc = "╔══[ ลิสการเลียนแบบ ]"
		        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ VҜ ŚẾL₣ВΌŦ ]")

                elif "nutmic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"❥ระบบเลียนแบบทำงาน ❋")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"❥ปิดระบบเลียนแบบ ❋")

		elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")
#==============================================================================#
                elif text.lower() == 'แอด':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "❥ผู้สร้างกลุ่มนี้ ❋")
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "❥ไอดีกลุ่ม❋ \n\n" + gid.id)
                elif text.lower() == 'รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = line.getGroup(to)
		    line.sendMessage(to, "❥ชื่อกลุ่ม ❋ \n\n" + gid.name)
                elif text.lower() == 'ลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "❥ลิ้งของกลุ่ม❋\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'เปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "❥เปิดลิ้ง สำเร็จ ❥")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "❥ เปิดลิ้ง สำเร็จ ❋")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "❥ปิดลิ้ง สำเร็จ ❋")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "❥ปิดลิ้ง สำเร็จ ❋")
		elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "คนนี้คือผู้สร้างกลุ่มนี้"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[❥ ข้อมูลของกลุ่มนี้❥ ]"
                    ret_ += "\n╠ ❥ชื่อของกลุ่ม❋ : {}".format(str(group.name))
                    ret_ += "\n╠ ❥ไอดีของกลุ่ม❋ : {}".format(group.id)
                    ret_ += "\n╠ ❥ผู้สร้างกลุ่ม❋ : {}".format(str(gCreator))
                    ret_ += "\n╠ ❥จำนวนสมาชิก❋ : {}".format(str(len(group.members)))
                    ret_ += "\n╠ ❥จำนวนค้างเชิญ❋ : {}".format(gPending)
                    ret_ += "\n╠ ❥ลิ้งของกลุ่ม❋ : {}".format(gQr)
                    ret_ += "\n╠ ❥ลิ้งกลุ่ม❋ : {}".format(gTicket)
                    ret_ += "\n╚══[ VҜ ŚẾL₣ВΌŦ ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'สมาชิก':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ ❋รายชื่อสมาชิก❋ ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} คน ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
		elif text.lower() == 'กลุ่มทั้งหมด':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))
                elif "เชิญคลอ" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    line.sendMessage(msg.to,"❋เชิญเข้าร่วมการโทรสำเร็จ❋")
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass
                elif msg.text.lower() == 'เชิญแอด':
                        if msg.toType == 2:
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "❋พิมพ์คำเชิญกลุ่ม")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "❥ผู้สร้างกลุ่มอยู่ในแล้ว❋")

                elif msg.text.lower() == "getjoined":
                    line.sendText(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = line.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += line.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            line.sendText(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    line.sendText(msg.to,text[:-2])
                    cnt = 0
		elif ".ข้อ " in msg.text.lower():
                    spl = re.split(".ข้อ ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = line.getContact(uid)
                            try:
                                line.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net{}".format(userData.picturePath))
                            except:
                                pass
                            line.sendText(msg.to,"ชื่อที่แสดง: "+userData.displayName)
                            line.sendText(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)
                            line.sendText(msg.to,"ไอดีบัญชี: "+userData.mid)

                elif "รับแก้ไฟล์+เพิ่มไฟล์+แก้ภาษา\n" in msg.text:
                    spl = msg.text.split("รับแก้ไฟล์+เพิ่มไฟล์+แก้ภาษา\n💝\n╚══════════════┛")
                    if spl[len(spl)-1] == "":
                        line.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)
		elif "รัน @" in msg.text:
                    print ("[Command]covergroup")
                    _name = msg.text.replace("รัน @","")
                    _nametarget = _name.rstrip('  ')
                    gs = line.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        line.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                               thisgroup = line.getGroups([msg.to])
                               Mids = [target for contact in thisgroup[0].members]
                               mi_d = Mids[:33]
		               line.createGroup("VҜ ŚẾL₣ВΌŦ",mi_d)
                               line.sendText(msg.to,"[ŚẾL₣ВΌŦ LÍŇỀ]")
                               line.createGroup("VҜ ŚẾL₣ВΌŦ",mi_d)
                               line.sendText(msg.to,"[ŚẾL₣ВΌŦ LÍŇỀ]")
                               line.createGroup("VҜ ŚẾL₣ВΌŦ",mi_d)
                               line.sendText(msg.to,"[ŚẾL₣ВΌŦ LÍŇỀ]")
                               line.createGroup("VҜ ŚẾL₣ВΌŦ",mi_d)
                               line.sendText(msg.to,"[ŚẾL₣ВΌŦ LÍŇỀ]")
                               line.createGroup("VҜ ŚẾL₣ВΌŦ",mi_d)
                               line.sendText(msg.to,"[ŚẾL₣ВΌŦ LÍŇỀ]")
                               line.createGroup("VҜ ŚẾL₣ВΌŦ",mi_d)
                               line.sendText(msg.to,"[ŚẾL₣ВΌŦ LÍŇỀ]")
                               line.createGroup("VҜ ŚẾL₣ВΌŦ",mi_d)
                               line.sendText(msg.to,"[ŚẾL₣ВΌŦ LÍŇỀ]")
                               line.createGroup("VҜ ŚẾL₣ВΌŦ",mi_d)
                               line.sendText(msg.to,"[ŚẾL₣ВΌŦ LÍŇỀ]")
                               line.createGroup("VҜ ŚẾL₣ВΌŦ",mi_d)
                               line.sendText(msg.to,"[ŚẾL₣ВΌŦ LÍŇỀ]")
                               line.createGroup("VҜ ŚẾL₣ВΌŦ",mi_d)
                               line.sendText(msg.to,"[ŚẾL₣ВΌŦ LÍŇỀ]")
                               line.sendText(msg.to,"❋ทำการรัน สำเร็จ")
                            except:
                                pass
                    print ("[Command]covergroup]")
		elif "รันแชท @" in msg.text:
                    _name = msg.text.replace("รันแชท @","")
                    _nametarget = _name.rstrip(' ')
                    gs = line.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
			   line.sendText(g.mid,"VҜ ŚẾL₣ВΌŦ")
                           line.sendText(msg.to, "❋ทำการรันแชท สำเร็จ❋")
                           print (" Spammed !")
		elif "รัน: " in msg.text.lower():
                        key = msg.text[-33:]
                        line.findAndAddContactsByMid(key)
                        contact = cl.getContact(key)
                        line.createGroup("VҜ ŚẾL₣ВΌŦ",[key])
                        line.sendText(msg,to,"❋ทำการรัน สำเร็จ❋")
                elif "ไม่รับเชิญ " in msg.text.lower():
                    spl = re.split("ไม่รับเชิญ ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = line.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        line.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                line.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    line.sendText(gr,spl[1])
                                line.leaveGroup(gr)
                            except:
                                pass
                        line.sendText(msg.to,"❋สำเร็จแล้ว")
                elif ".whois " in msg.text.lower():
                    spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {"mid":spl[1]}
                        line.sendMessage(msg)
                elif "ฟัก" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
		elif "หีแหก" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)

                elif msg.text.lower() == "mid":
                    line.sendText(msg.to,user1)

                elif ".name " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = spl[1]
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".nmx " in msg.text.lower():
                    spl = re.split(".nmx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = line.nmxstring(spl[1])
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
		elif "มุด " in msg.text.lower():
                    spl = re.split("มุด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/$"http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendText(msg.to,str(e))
		
		elif msg.text.lower() == ".groupurl":
                    if msg.toType == 2:
                        line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(msg$
                    else:
                        line.sendText(msg.to,"❋คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".groupurl " in msg.text.lower():
                    spl = re.split(".groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket$
                        except Exception as e:
                            line.sendText(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")
                if "gift " in msg.text.lower():
                    red = re.compile(re.escape('gift '),re.IGNORECASE)
                    themeid = red.sub('',msg.text)
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': themeid,
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)
#==============================================================================#
		elif text.lower() == 'แทค':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTI$
                        line.sendMessage(to, "❋ทั้งหมด {} คน❋".format(str(len(nama))))
#===================================================================#
		elif msg.text.lower().startswith("ประกาศ: "):
                      sep = text.split(" ")
                      bc = text.replace(sep[0] + " ","")
                      saya = line.getGroupIdsJoined()
                      for group in saya:
                         ret_ = "{}".format(str(bc))
                         text = ret_ + ""
                         line.sendMessage(group, text)

                elif "ประกาศแชท " in msg.text:
                    bc = msg.text.replace("ประกาศแชท ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendText(i,"======[ข้อความประกาศแชท]======\n\n"+bc+"\n\nBy: ✬١ढेืਹℓట่થ✭!! ")

                elif "ส่งรูปภาพกลุ่ม: " in msg.text:
                    bc = msg.text.replace("ส่งรูปภาพกลุ่ม: ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendImageWithURL(i, bc)

                elif "ส่งรูปภาพแชท: " in msg.text:
                    bc = msg.text.replace(".ส่งรูปภาพแชท: ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendImageWithURL(i, bc)
		
		elif msg.text in ["เปิดแอบ"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"เปิดระบบเช็คคนอ่านอัตโนมัติ❋")
                elif msg.text in ["ปิดแอบ"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        #line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    #else:
                        line.sendMessage(msg.to, "ปิดระบบเช็คคนอ่านแล้ว❋")

		elif text.lower() == 'ปิดบอท':
                    line.sendMessage(receiver, '❋ปิดการทำงานของบอทแล้ว❋')
                    print ("Selfbot Off")
                    exit(1)
                elif text.lower() == "ลบแชท":
                        if msg._from in lineMID:
                            try:
                                line.removeAllMessages(op.param2)
                                line.sendMessage(msg.to,"❋ลบแชททั้งหมด เรียบร้อย❋")
                            except:
                                pass
                                print ("ลบแชท")
                elif text.lower() == 'เพื่อน':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="❋รายชื่อเพื่อนทั้งหมด❋"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n❋รายชื่อเพื่อนทั้งหมด❋\n\nมีดังต่อไปนี้ : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

		blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═══ไม่มีรายการบัญชีที่ถูกบล็อค═══"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n══════รายการบัญชีที่ถูกบล็อค══════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["ไอดีเพื่อน"]:
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════ไอดีเพื่อน═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════ไอดีเพื่อน═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

		elif msg.text.lower() == 'gurl':
                        if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"╔══════════════┓\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂Link ลิ้งของกลุ่ม ❋ Qr\n╚══════════════┛")

                elif msg.text == "ขอหื่น":
                        line.sendMessage(receiver,">thumzilla.com\n>anyporn.com")
                elif msg.text == ".ประ":
                        line.sendMessage(msg.to,str(settings["message1"]))
                elif msg.text.lower() == '.ดึงแอด':
                        if msg.toType == 2:
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Type👉 Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in ["ไม่รับเชิญ"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)                                                $
                        except:
                            pass
                elif msg.text in ["เช็คไอดี"]:
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="✬١ढेืਹℓట่થ✭"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\nจำนวน  %i" % len(kontak)
                    line.sendMessage(receiver, msgs)
		
		elif msg.text in ["ปิดเตะแทค"]:
                    settings["kickMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบเตะคนแทค❋")

                elif msg.text in ["เปิดแทค"]:
                        settings['detectMention'] = True
                        line.sendMessage(msg.to,"❋เปิดข้อความตอบรับคนแทค")

                elif msg.text in ["ปิดแทค"]:
                        settings['detectMention'] = False
                        line.sendMessage(msg.to,"❋ปิดข้อความตอบรับคนแทค")

                elif msg.text in ["เปิดแทค2"]:
                    settings["potoMention"] = True
                    line.sendMessage(msg.to,"❋เปิดแสดงรูปและคทคนแทค")

                elif msg.text in ["ปิดแทค2"]:
                    settings["potoMention"] = False
                    line.sendMessage(msg.to,"❋ปิดแสดงรูปและคทคนแทค")

                elif msg.text in ["เปิดแทค3"]:
                    settings["delayMention"] = True
                    line.sendMessage(msg.to,"❋เปิดแทค คนแทคกลับ")

                elif msg.text in ["ปิดแทค3"]:
                    settings["delayMention"] = False
                    line.sendMessage(msg.to,"❋ปิดแทค คนแทคกลับ")

                elif msg.text in ["เปิดตรวจ"]:
                    settings["Aip"] = True
                    line.sendMessage(msg.to,"❋เปิดระบบตรวจสอบบอทบิน")

                elif msg.text in ["ปิดตรวจ"]:
                    settings["Aip"] = False
                    line.sendMessage(msg.to,"❋ปิดระบบตรวจสอบบอทบิน")

                elif msg.text in ["เปิดพูด"]:
                    settings["Api"] = True
                    line.sendMessage(msg.to,"❋เปิดระบบบอทapi")

                elif msg.text in ["ปิดพูด"]:
                    settings["Api"] = False
                    line.sendMessage(msg.to,"❋ปิดระบบบอทapi")

		elif msg.text in ["ดึง"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"❋ส่งคท คนที่ต้องการดึง❋")
                elif msg.text.lower() == ".ยกเชิญ":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == ".บอทยก":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(Exc).cancelGroupInvitation(msg.to,[i])
#=============COMMAND KICKER===========================#
                elif msg.text in ["ล้างแบน"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"❋เคลียร์บันชีดำทั้งหมดเรียบร้อย❋")
                    print ("Clear Ban")

                elif 'ลาก่อย' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(Rfu).kickoutFromGroup(msg.to,[target])
                               print ("Rfu kick User")
                           except:
                               random.choice(Rfu).sendMessage(msg.to,"Limit kaka 😫")

                elif 'สอย' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])
                               print ("Sb Kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")

		elif msg.text in ["เตะแบน"]:
                        if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"❋ไม่พบคนติดแบนในกลุ่มนี้❋")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"❋bye 👋 ")
                                     print ("Blacklist di Kick")
                elif "ชื่อ: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อเป็น\n " + string)
                        print ("Update Name")

                elif "ตัส: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนตัสเป็น\n " + string)
                        print ("Update Bio Succes")

#=============COMMAND PROTECT=========================#
		elif text.lower() == 'ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "❋ลบรันเสร็จแล้ว❋")
                    line.sendMessage(to, "❋เวลาที่ใช้: %sวินาที❋" % (elapsed_time))

                elif "แบนหมด" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("แบนหมด","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"แบนสมาชิกทุกคนในกลุ่มนี้❋")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"พบข้อผิดพลาดที่ไม่ทราบสาเหตุ")
		elif 'แบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"ทำการแบน สำเร็จ❋")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"ผิดพลาด")
		elif msg.text in ["เช็คแบน"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่มีผู้ไช้ที่ติดแบน ❋")
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้ไช้ที่ติดแบน❋")
                        mc = "รายชื่อ ❋\n"
                        for mi_d in settings["blacklist"]:
                            mc += "➠ " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")
#==============================================================================#
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
#==============================================================================#
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])

		if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])

        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 in settings["blacklist"] == {}:
                line.kickoutFromGroup(op.param1,[op.param2])
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                line.sendText(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")
        if op.type == 26:
            msg = op.message
            if settings ["Aip"] == True:
                if msg.text in dangerMessage:
                    random.choice(Rfu).kickoutFromGroup(receiver,[sender])
                    random.choice(Rfu).sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก (｀・ω・´)")
            if settings ["Aip"] == True:
                if msg.text in fukgerMessage:
                    random.choice(Rfu).kickoutFromGroup(receiver,[sender])
                    random.choice(Rfu).sendText(msg.to,"ตรวจพบคำพูดหยาบคายไม่สุภาพ จำเป็นต้องนำออกเพื่อความสงบสุขของสมาชิก (｀・ω・´)")
            if settings ["Api"] == True:
                if msg.text in ["ป๊า","นาย","เพื่อน","จาร์ย","อาจาร์ย","เฮีย"]:
                    line.sendMessage(msg.to, str(settings["comment"]))
            if settings ["Api"] == True:
                if msg.text in ["บอท","เซล","เซลบอท","selfbot","คนรึบอท","Help","help",".help","/help","คำสั่ง"]:
                    line.sendMessage(msg.to, str(settings["comment"]))
            if settings ["Api"] == True:
                if msg.text in ["55","555","5555","55555","55+","555+","5555+","ขำ",".ขำ"]:
                    line.sendText(msg.to,"ขำขนาดนี้ไปขี้เถอะ")
            if settings ["Api"] == True:
        if op.type == 26:
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
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                if settings["unsendMessage"] == True:
                    try:
                        msg = op.message
                        if msg.toType == 0:
                            line.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            line.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        logError(error)
                if msg.contentType == 0:
                    if text is None:
                        return
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
			    links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                line.sendMessage(to, "มุดลิ้งเข้าไปในกลุ่ม👉 %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in msg.contentMetadata.keys() != None:
                             if settings['kickMention'] == True:
                                     contact = line.getContact(msg._from)
                                     cName = contact.displayName
                                     balas = ["เนื่องจากตอนนี้ผมเปิดระบบเตะคนแทคไว้ " + "\n👉" +cName + "\n🙏ต้องขออภัยด้วยจริงๆ🙏Bye!!!"]
				     ret_ = "" + random.choice(balas)
                                     name = re.findall(r'@(\w+)', msg.text)
                                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                                     mentionees = mention["MENTIONEES"]
                                     for mention in mentionees:
                                               if mention['M'] in admin:
                                                          line.sendText(msg.to,ret_)
                                                          random.choice(Rfu).kickoutFromGroup(msg.to,[msg._from])
                                                          break
                                               if mention['M'] in lineMID:
                                                          line.sendText(msg.to,ret_)
                                                          random.choice(Rfu).kickoutFromGroup(msg.to,[msg._from])
                                                          break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             mi_d = contact.mid
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          line.sendContact(msg.to, mi_d)
                                          break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["『ข้อความ อัตโนมัติ』\n " + cName + "\n\n『❋Auto Respon❋』"]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_)
                                          line.sendMessage(to,str(settings["Respontag"]))
					  line.sendMessage(msg.to, None, contentMetadata={"STKID":"62542990","STKPKGID":"4063114","STKVER":"1"}, contentType=7)
                                          break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['delayMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          break
        if op.type == 65:
           print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
           if settings["unsendMessage"] == True:
               try:
                   at = op.param1
                   msg_id = op.param2
                   if msg_id in msg_dict:
                       if msg_dict[msg_id]["from"]:
                           contact = linegetContact(msg_dict[msg_id]["from"])
                           if contact.displayNameOverridden != None:
                               name_ = contact.displayNameOverridden
                           else:
                               name_ = contact.displayName
                               ret_ = "Send Message cancelled."
                               ret_ += "\nSender : @!"
			       ret_ += "\nSend At : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                               ret_ += "\nType : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                               ret_ += "\nText : {}".format(str(msg_dict[msg_id]["text"]))
                               sendMention(at, str(ret_), [contact.mid])
                           del msg_dict[msg_id]
                       else:
                           line.sendMessage(at,"SentMessage cancelled,But I didn't have logdata.\nSorry > <")
               except Exception as error:
                   logError(error)
                   #traceback.print_tb(error.__traceback__)

        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Wc"] == True:
             if op.param2 in lineMID:
                 return
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1, str(settings["welcome"]) +"\n❋สวัสดี {}, Welcome to Group {}\nมาใหม่แก้ผ้าเลย❋".format(str(dan.displayName),str(tgb.name)))
             line.sendContact(op.param1, op.param2)
             line.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
             line.sendMessage(op.param1, str(settings["comment"]))
        if op.type == 19:
           print ("MEMBER KICKOUT TO GROUP")
           if settings["Nk"] == True:
             if op.param2 in lineMID:
                 return
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
	     line.sendMessage(op.param1,str(settings["kick"]) + "\nเฮ้ย {}, คือหยังมันโหดแท้วะΣ(っﾟДﾟ；)っ ".format(str(dan.displayName)))
             line.sendContact(op.param1, op.param2)
             line.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["Lv"] == True:
             if op.param2 in lineMID:
                 return
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1,str(settings["bye"]) + "\n {}, ไปซะละ {} \nลาก่อยยย❋".format(str(dan.displayName),str(tgb.name)))
             line.sendContact(op.param1, op.param2)
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰" + Name
                            pref=['แอบทมายออกมาควยกัน']
                            sendMessageWithMention(op.param1, op.param2)
                            line.sendMessage(op.param1, str(random.choice(pref)) + '\n❋❋❋')
                            line.sendContact(op.param1, op.param2)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
			        nick = Name.split(' ')
                            if len(nick) == 2:
                                line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print (" [ ทดสอบเสือเผ่น ]  ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True


while True:
    try:
        ops = oepoll.singleTrace(count=5)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
