import hashlib
import json
import random
import socket
import time
import urllib
import requests
import urllib3
from bs4 import BeautifulSoup
import json
import re
import http.client
from function import get_referer_cookie1_uuid_enc1, spilt_cookie, qrcodeAuth, read_file, write_file, getstatus, \
    get_knowledgeid, get_clazzid_courseid_cpi, get_video, get_duration_dtoken, get_real_video, video_log, send_studylog, \
    get_dftu, send_mark, video_minitor, allsubtitle, viewpic, initdatawithviewerV2, get_points, ac_mark
from enc import dftu_enc

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_hotdata(clazzid, knowledgeid, objectid, courseid, personId, cookie):
    url = "https://mooc1.chaoxing.com/mooc-ans/courseapi/getvideohotdata"

    # 定义查询参数
    params = {
        "_dc": int(time.time() * 1000),
        "clazzid": clazzid,
        "knowledgeid": knowledgeid,
        "objectid": objectid,
        "courseid": courseid,
        "cpi": personId,
        "ut": "s"
    }

    # 定义请求头
    headers = {
        "Host": "mooc1.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": '"Windows"',
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": cookie
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params, verify=False)

    # 打印响应内容
    print("状态码:", response.status_code)
    print("响应内容:", response.text)


def api_getUploadConfig(cookie):
    url = "https://noteyd.chaoxing.com/pc/files/getUploadConfig"

    # 定义请求头
    headers = {
        "Host": "noteyd.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "Content-Type": "application/x-www-form-urlencoded",
        "sec-ch-ua-mobile": "?0",
        "Origin": "https://mooc1.chaoxing.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        # "Referer": "https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=888803645&courseId=245055799&clazzid=104076320&cpi=285104941&enc=e619568b77200ae4e7cc053e489355ba&mooc2=1&openc=d4f870ff250a870e94459efb37476bfc",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": cookie
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, verify=False)

    # 打印响应内容
    print("状态码:", response.status_code)
    print("响应内容:", response.text)


def api_getcookie(cookie):
    # 定义请求的 URL
    url = "https://noteyd.chaoxing.com/apis/getCookie?name=browserLocale"

    # 定义请求头
    headers = {
        "Host": "noteyd.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "Origin": "https://mooc1.chaoxing.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        # "Referer": "https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=888803645&courseId=245055799&clazzid=104076320&cpi=285104941&enc=e619568b77200ae4e7cc053e489355ba&mooc2=1&openc=d4f870ff250a870e94459efb37476bfc",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": cookie
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, verify=False)

    # 打印响应内容
    print("状态码:", response.status_code)
    print("响应内容:", response.text)


def set_log(setlog, cookie, chapterid=None, t=None):
    # 定义请求的 URL
    url = setlog
    if chapterid is not None:
        url += "&chapterId=" + chapterid
    if t is not None:
        url += "&_=" + str(t)

    # 定义请求头
    headers = {
        "Host": "fystat-ans.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "script",
        "Referer": "https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/studentcourse?courseid=245055799&clazzid=104076320&cpi=285104941&ut=s&t=1732176628496",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": cookie
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, verify=False)

    # 打印响应内容
    print("状态码:", response.status_code)
    print("响应内容:", response.text)

'''
# 初始化cookie,uuid和enc1
referer, cookie1, uuid, enc1 = get_referer_cookie1_uuid_enc1()
write_file(uuid, "uuid")
write_file(enc1, "enc1")
write_file(cookie1, "cookie1")
if uuid is not None and enc1 is not None:
    qrcodeAuth(referer, cookie1, uuid)
    # 100秒都扫不完码是吧
    for i in range(10):
        status, cookie2 = getstatus(referer, cookie1, uuid, enc1)
        time.sleep(5)
        if status:
            break
    write_file(cookie2, "cookie2")
'''
enc1 = read_file("enc1")
uuid = read_file("uuid")
cookie1 = read_file("cookie1")
cookie2 = read_file("cookie2")
'''
cookie3 = get_clazzid_courseid_cpi(cookie1, cookie2)
write_file(cookie3, "cookie3")
'''
cookie3 = read_file("cookie3")

# 从 JSON 文件中读取数据
with open("courses.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)  # 解析 JSON 数据
    course = data[0]  # for course in data:
    title = course.get("title")
    courseid = course.get("courseid")
    clazzid = course.get("clazzid")
    personId = course.get("personId")
    print("title:", title)
    print("courseId:", courseid)
    print("clazzId:", clazzid)
    print("personId:", personId)

cookie = cookie1 + cookie2 + cookie3
cookie4, setlog = get_knowledgeid(courseid, clazzid, personId, cookie)
# write_file(cookie4, "cookie4")

# cookie4 = read_file("cookie4")
cookie = cookie1 + cookie2 + cookie4

# 从 JSON 文件中读取数据
with open("chapters.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)  # 解析 JSON 数据
    course = data[15]  # for course in data:
    knowledgeid = course.get("knowledgeid")
    title = course.get("title")
    print("knowledgeid:", knowledgeid)
    print("title:", title)

objectId, otherInfo, jobid, userid, videoFaceCaptureEnc, attDuration, attDurationEnc, fid, mtEnc, aid, playTime, interval, from_value, objectid3, imgcount, mid, objectid = get_video(
    clazzid, courseid, knowledgeid, personId, cookie)
print(objectId, otherInfo, jobid, userid, videoFaceCaptureEnc, attDuration, attDurationEnc, fid, mtEnc, aid, from_value,
      objectid3, imgcount, mid, objectid)

ac_mark(objectid3, from_value, cookie, userid, imgcount, objectid)
set_log(setlog, cookie, knowledgeid)
api_getcookie(cookie)
set_log(setlog, cookie, knowledgeid, int(time.time() * 1000))
send_studylog(cookie, courseid, clazzid, personId, aid, objectId, userid, knowledgeid, fid, jobid, mtEnc, 1)
video_minitor()
api_getcookie(cookie)
api_getUploadConfig(cookie)
duration, dtoken, video_http, thumb_http, thumb_enc = get_duration_dtoken(objectId, fid, cookie)
initdatawithviewerV2(mid, personId, clazzid, courseid, cookie)
get_points(courseid, mid, cookie)
viewpic(thumb_http, thumb_enc, cookie)
allsubtitle(mid, objectid, courseid, cookie)
ac_mark(objectid3, from_value, cookie, userid, imgcount, objectid)
get_hotdata(clazzid, knowledgeid, objectid, courseid, personId, cookie)
playTime = playTime // 1000
status_code, isPassed = video_log(personId, dtoken, clazzid, duration, objectId, otherInfo, courseid, jobid, userid,
                                  videoFaceCaptureEnc, attDuration,
                                  attDurationEnc, cookie, playTime, 3)
print(playTime)
playTime += 58
send_studylog(cookie, courseid, clazzid, personId, aid, objectId, userid, knowledgeid, fid, jobid, mtEnc, 4)
while isPassed is False and playTime < duration:
    print(playTime)
    get_points(courseid, mid, cookie)
    ac_mark(objectid3, from_value, cookie, userid, imgcount, objectid)
    time.sleep(30)
    get_points(courseid, mid, cookie)
    ac_mark(objectid3, from_value, cookie, userid, imgcount, objectid)
    time.sleep(30)
    status_code, isPassed = video_log(personId, dtoken, clazzid, duration, objectId, otherInfo, courseid, jobid, userid,
                                      videoFaceCaptureEnc, attDuration,
                                      attDurationEnc, cookie, playTime, 0)
    playTime += 58


''''
f, u, d, t = get_dftu(objectid3, from_value, cookie, userid, imgcount)
enc = dftu_enc(d, f, t, u)
send_mark(f, u, d, t, enc, objectid, from_value)
duration, dtoken, video_http, thumb_http, thumb_enc = get_duration_dtoken(objectId, fid, cookie)

print(duration, dtoken, video_http, thumb_http, thumb_enc)
# getpoint
initdatawithviewerV2(mid, personId, clazzid, courseid, cookie)
get_points(courseid, mid, cookie)
viewpic(thumb_http, thumb_enc, cookie)
allsubtitle(mid, objectid, courseid, cookie)
# print(duration, dtoken, video_http)

f, u, d, t = get_dftu(objectid3, from_value, cookie, userid, imgcount)
# print(f, u, d, t)
enc = dftu_enc(d, f, t, u)
print(enc)
#
# get_real_video(video_http)
# video_minitor()
isPassed = False
playTime = playTime // 1000
print(playTime)
print(interval)
for i in range(2):
    if i == 0 and not isPassed:  # 点击视频的开始键
        send_mark(f, u, d, t, enc, objectid, from_value)
        video_minitor()
        isdrag = 3
        status_code, isPassed = video_log(personId, dtoken, clazzid, duration, objectId, otherInfo, courseid, jobid,
                                          userid,
                                          videoFaceCaptureEnc,
                                          attDuration, attDurationEnc, cookie, playTime, isdrag)
        send_studylog(cookie, courseid, clazzid, personId, aid, objectId, userid, knowledgeid, fid, jobid, mtEnc, 4)

    elif i >= 1 and not isPassed:  # 正常的经过六十秒
        time.sleep(30)
        send_mark(f, u, d, t, enc, objectid, from_value)
        video_minitor()
        time.sleep(30)
        send_mark(f, u, d, t, enc, objectid, from_value)
        video_minitor()
        playTime += 60
        if playTime > duration:
            playTime = duration
        isdrag = 0
        status_code, isPassed = video_log(personId, dtoken, clazzid, duration, objectId, otherInfo, courseid, jobid,
                                          userid,
                                          videoFaceCaptureEnc,
                                          attDuration, attDurationEnc, cookie, playTime, isdrag)
        if status_code != 200:
            for j in range(3):
                status, status_code = video_log(personId, dtoken, clazzid, duration, objectId, otherInfo, courseid,
                                                jobid,
                                                userid,
                                                videoFaceCaptureEnc,
                                                attDuration, attDurationEnc, cookie, playTime, isdrag)
        if status_code != 200:
            print("error,please retry")
    elif isPassed:
        playTime = duration
        isdrag = 4
        status_code, isPassed = video_log(personId, dtoken, clazzid, duration, objectId, otherInfo, courseid, jobid,
                                          userid,
                                          videoFaceCaptureEnc,
                                          attDuration, attDurationEnc, cookie, playTime, isdrag)
        break
'''
