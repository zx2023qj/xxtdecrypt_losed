import hashlib
import json
import random
import time
import re
import urllib

import requests
import urllib3
from PIL import Image
from io import BytesIO
from datetime import datetime

from bs4 import BeautifulSoup
from enc import dftu_enc
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def write_file(content, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def spilt_cookie(set_cookie):
    cookie_parts = set_cookie.split(", ")
    valid_parts = []
    for part in cookie_parts:
        sub_parts = part.split(";")
        # 保留没有包含 Domain、Expires、GMT 和 Path 的 key-value 对
        sub_parts = [sub for sub in sub_parts if
                     not any(keyword in sub for keyword in ["Domain", "Expires", "Path", "GMT", "HttpOnly", "Secure"])]
        # 如果有有效字段，加入 valid_parts
        if sub_parts:
            valid_parts.append(";".join(sub_parts))
    # 将过滤后的字段重新连接为一个标准的 cookie 格式
    cookie_string = "; ".join(valid_parts)
    return cookie_string


def get_referer_cookie1_uuid_enc1():
    current_time = int(time.time() * 1000)
    url = "https://passport2.chaoxing.com/cloudscanlogin"

    params = {
        "mobiletip": "电脑端登录确认",
        "time": str(current_time),  # 将时间戳转换为字符串
        "pcrefer": "https://v1.chaoxing.com/backSchool/toLogin?source=num8"
    }

    # 定义请求头
    headers = {
        "Host": "passport2.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "iframe",
        "Referer": "https://v8.chaoxing.com/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7"
    }
    request = requests.Request('GET', url, params=params)
    referer = request.prepare().url
    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params, verify=False)
    # 打印响应内容
    print(response.status_code)
    set_cookie = response.headers.get('Set-Cookie')
    cookie_string = spilt_cookie(set_cookie)
    # 打印cookie
    print(cookie_string)
    # 提取 body 内容
    response_body = response.text

    # 使用正则表达式匹配并提取 id 和 value
    uuid_match = re.search(r'<input type\s*=\s*"hidden"\s*value\s*=\s*"([^"]+)"\s*id\s*=\s*"uuid"\s*/>', response_body)
    enc_match = re.search(r'<input type\s*=\s*"hidden"\s*value\s*=\s*"([^"]+)"\s*id\s*=\s*"enc"\s*/>', response_body)

    # 提取并打印结果
    if uuid_match:
        uuid_value = uuid_match.group(1)
        print("UUID Value:", uuid_value)
    else:
        print("UUID not found.")
        return set_cookie, None, None

    if enc_match:
        enc_value = enc_match.group(1)
        print("ENC Value:", enc_value)
    else:
        print("ENC not found.")
        return set_cookie, None, None
    return referer, cookie_string, uuid_value, enc_value


def qrcodeAuth(referer, cookie1, uuid):
    url = "https://passport2.chaoxing.com/createqr"

    params = {
        "uuid": uuid,
        "xxtrefer": "",
        "type": 1,
        "clientid": "",
        "mobiletip": "电脑端登录确认",
        "fid": ""
    }
    # 定义请求头
    headers = {
        "Host": "passport2.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "Windows",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "image",
        "Referer": referer,
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": cookie1
    }
    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params, verify=False)
    if response.status_code == 200:
        # 将二进制数据转换为图像对象
        img = Image.open(BytesIO(response.content))
        # 保存到本地文件
        output_file = "qrcode.png"  # 文件名
        img.save(output_file)
        img.show()
        '''
        qr = qrcode.QRCode(
            version=10,  # 设置二维码版本（范围：1-40）
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # 纠错级别：L、M、Q、H
            box_size=10,  # 每个小方块的大小
            border=4,  # 边框宽度（单位：小方块）
        )
        qr.clear()
        qr.add_data(img_data)
        qr.print_ascii()
        '''
    else:
        print(f'Error: {response.status_code}')


def getstatus(referer, cookie1, uuid, enc1):
    # 定义URL
    url = 'https://passport2.chaoxing.com/getauthstatus'

    headers = {
        'Connection': 'keep-alive',
        'Content-Length': '74',  # 这个值通常不需要手动设置
        'sec-ch-ua-platform': '"Windows"',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'Origin': 'https://passport2.chaoxing.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': referer,
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'Cookie': cookie1
    }

    # 定义请求体
    data = {
        'enc': enc1,
        'uuid': uuid
    }

    # 发送POST请求
    response = requests.post(url, headers=headers, data=data, verify=False)
    # 打印响应内容
    set_cookie = response.headers.get('Set-Cookie')
    cookie_string = ''
    if set_cookie:
        cookie_string = spilt_cookie(set_cookie)
        # 打印cookie
        print(cookie_string)
    print('Response Text:', response.text)
    if '"status":true' in response.text:
        return True, cookie_string
    else:
        return False, cookie_string


def get_clazzid_courseid_cpi(cookie1, cookie2):
    # 请求URL
    url = "https://mooc1-1.chaoxing.com/mooc-ans/visit/courselistdata"

    # 请求头
    headers = {
        "Host": "mooc1-1.chaoxing.com",
        "Connection": "keep-alive",
        "Content-Length": "80",
        "sec-ch-ua-platform": '"Windows"',
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Accept": "text/html, */*; q=0.01",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "Origin": "https://mooc1-1.chaoxing.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        # "Referer": "https://mooc1-1.chaoxing.com/visit/interaction?s=b7218d31024eb57c03a05e9c9358f603",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": cookie1 + cookie2
    }

    # 请求数据
    data = {
        "courseType": "1",
        "courseFolderId": "0",
        "baseEducation": "0",
        "superstarClass": "",
        "courseFolderSize": "0"
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=data, verify=False)
    cookie_string = ""
    if response.status_code == 200:
        # 输出响应内容
        set_cookie = response.headers.get('Set-Cookie')
        cookie_string = spilt_cookie(set_cookie)
        print(cookie_string)
        # 使用正则表达式匹配整个 <li> 标签
        matches1 = re.findall(
            r'<li class="course clearfix" courseId="([^"]+)" clazzId="([^"]+)" personId="([^"]+)" id="[^"]*">',
            response.text)
        # 使用正则表达式匹配 <span> 标签并提取 title 属性
        matches2 = re.findall(r'<span class="course-name overHidden2" title="([^"]+)">', response.text)

        # 创建一个列表来存储结果
        results = []

        for (course_id, clazz_id, person_id), title in zip(matches1, matches2):
            result = {
                "title": title,
                "courseid": course_id,
                "clazzid": clazz_id,
                "personId": person_id
            }
            results.append(result)

        # 将结果写入 JSON 文件
        with open("courses.json", "w", encoding="utf-8") as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)

        '''
        # 确保两个列表的长度相同
        if len(matches1) == len(matches2):
            # 遍历所有匹配结果并打印
            for (course_id, clazz_id, person_id), title in zip(matches1, matches2):
                print("title:", title)
                print("courseId:", course_id)
                print("clazzId:", clazz_id)
                print("personId:", person_id)
                print("---")  # 分隔符
        else:
            print("匹配的数量不一致，无法一一对应。")
        '''
    return cookie_string


def get_knowledgeid(courseid, clazzid, cpi, cookie):
    url = "https://mooc2-ans.chaoxing.com/mycourse/studentcourse"
    params = {
        "courseid": courseid,
        "clazzid": clazzid,
        "vc": "1",
        "cpi": cpi,
        "ismooc2": "1",
        "v": "2"
    }

    headers = {
        "Host": "mooc2-ans.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Sec-Purpose": "prefetch;prerender",
        "Purpose": "prefetch",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": cookie
    }

    response = requests.get(url, params=params, headers=headers, verify=False)
    set_cookie = response.headers.get('Set-Cookie')
    cookie_string = spilt_cookie(set_cookie)
    print(cookie_string)
    pattern = r'src="(https://fystat-ans\.chaoxing\.com/log/setlog\?.*?)"'
    match = re.search(pattern, response.text)

    if match:
        setlog = match.group(1)
        print(setlog)
    else:
        print("没有找到匹配的 URL")

    matches1 = re.findall(r'<div class="inputCheck fl"><input type="checkbox" name="checkbox" value="([^"]+)"/>',
                          response.text)
    matches2 = re.findall(r'<span class="catalog_sbar">(.*?)</span>\s*(.*)',
                          response.text)
    '''
    for knowledgeid, (index, name) in zip(matches1, matches2):
        print(knowledgeid, index + ' ' + name)
    '''
    # 创建一个列表来存储结果
    results = []

    for knowledgeid, (index, name) in zip(matches1, matches2):
        result = {
            "knowledgeid": knowledgeid,
            "title": index + ' ' + name
        }
        results.append(result)

    # 将结果写入 JSON 文件
    with open("chapters.json", "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    return cookie_string, setlog


def get_video(clazzid, courseid, knowledgeid, cpi, cookie):
    url = "https://mooc1.chaoxing.com/mooc-ans/knowledge/cards"
    params = {
        "clazzid": clazzid,
        "courseid": courseid,
        "knowledgeid": knowledgeid,
        "num": "0",
        "ut": "s",
        "cpi": cpi,
        "v": "20160407-3",
        "mooc2": "1",
        "isMicroCourse": "false"
    }

    headers = {
        "Host": "mooc1.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "iframe",
        # "Referer": "https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=888803600&courseId=245055799&clazzid=104076320&cpi=285104941&enc=e619568b77200ae4e7cc053e489355ba&mooc2=1&openc=d4f870ff250a870e94459efb37476bfc",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": cookie
    }

    response = requests.get(url, params=params, headers=headers, verify=False)
    # print(response.text)
    if response.status_code == 200:
        match = re.search(r"var _from = '([^']+)';", response.text)
        if match:
            from_value = match.group(1)
            # print("Extracted value:", from_value)
        else:
            print("No match found.")

        # 使用正则表达式提取 JavaScript 对象
        match = re.search(r"mArg\s*=\s*({.*?});", response.text, re.DOTALL)
        if match:
            json_string = match.group(1)  # 提取匹配的 JSON 字符串
            # print(json_string)
            data = json.loads(json_string)
            with open("video.json", "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            attachment_type = data['attachments'][0]['type']
            if attachment_type != 'video':
                print("本章节无视频")
                return
            else:
                # isPassed = data['attachments'][0]['isPassed']
                # if isPassed is True:
                #    print("本章节视频已观看")
                #    return
                # else:
                objectId = data['attachments'][0]['objectId']
                otherInfo = data['attachments'][0]['otherInfo'].split('&')[0]
                jobid = data['attachments'][0]['jobid']
                userid = data['defaults']['userid']
                videoFaceCaptureEnc = data['attachments'][0]['videoFaceCaptureEnc']
                attDuration = data['attachments'][0]['attDuration']
                attDurationEnc = data['attachments'][0]['attDurationEnc']
                fid = data['defaults']['fid']
                mtEnc = data['defaults']['mtEnc']
                aid = data['attachments'][0]['aid']
                interval = data['defaults']['reportTimeInterval']
                objectid = data['attachments'][0]['property']['objectid']
                objectid3 = data['attachments'][3]['property']['objectid']
                imgcount = data['attachments'][3]['property']['pagenum']
                mid = data['attachments'][0]['mid']
                try:
                    playTime = data['attachments'][0]['playTime']
                except KeyError:
                    print("no playTime")
                    playTime = 0
        else:
            print("未找到匹配的字符串")
        # print(response.headers.get('Set-Cookie'))
        return objectId, otherInfo, jobid, userid, videoFaceCaptureEnc, attDuration, attDurationEnc, fid, mtEnc, aid, playTime, interval, from_value, objectid3, imgcount, mid, objectid
    else:
        return


def get_duration_dtoken(objectId, fid, cookie):
    # 定义请求的 URL
    url = "https://mooc1.chaoxing.com/ananas/status/" + objectId
    current_time = int(time.time() * 1000)
    params = {
        "k": fid,
        "flag": "normal",
        "_dc": current_time
    }
    # 定义请求头
    headers = {
        "Host": "mooc1.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": '"Windows"',
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
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
    # print("Status Code:", response.status_code)
    # print(response.headers.get('Set-Cookie'))
    # print("Response Body:", response.text)
    data = json.loads(response.text)
    # print(data)
    dtoken = data['dtoken']
    duration = data['duration']
    video_http = data['http']
    thumb_http = data['thumbnails']
    thumb_enc = data['thumbnailsEnc']
    return duration, dtoken, video_http, thumb_http, thumb_enc


def get_real_video(url):
    # 请求头
    headers = {
        "Host": "s2.ananas.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Windows\"",
        "Accept-Encoding": "identity;q=1, *;q=0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://mooc1.chaoxing.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "video",
        "Referer": "https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Range": "bytes=0-"
    }

    # 发送请求
    response = requests.get(url, headers=headers, verify=False)

    # 输出响应状态码和部分响应内容
    print("状态码:", response.status_code)
    print("响应头", response.headers)

    # 保存到文件（可选）
    # with open("video_part.mp4", "wb") as file:
    #     file.write(response.content)


def video_log(cpi, dtoken, clazzid, duration, objectId, otherInfo, courseId, jobid, userid, videoFaceCaptureEnc,
              attDuration, attDurationEnc, cookie, playingTime, isdrag):
    # 定义请求的 URL
    url = "https://mooc1.chaoxing.com/mooc-ans/multimedia/log/a/" + cpi + "/" + dtoken
    # print(courseId)
    # playingTime = 0
    SALT = 'd_yHJ!$pdA~5'
    _string = '[{cid}][{uid}][{jid}][{oid}][{pt}][{salt}][{d}][{ct}]' \
        .format(cid=clazzid, uid=userid, jid=jobid, oid=objectId, pt=playingTime * 1000,
                d=duration * 1000, ct='0_' + str(duration), salt=SALT)
    md5 = hashlib.md5()
    md5.update(_string.encode())
    enc = md5.hexdigest()
    current_time = int(time.time() * 1000)
    current_time = 1731836096484
    # 定义查询参数
    params = {
        "clazzId": clazzid,
        "playingTime": playingTime,
        "duration": duration,
        "clipTime": "0_" + str(duration),
        "objectId": objectId,
        "otherInfo": otherInfo,
        "courseId": courseId,
        "jobid": jobid,
        "userid": userid,
        "isdrag": isdrag,
        "view": "pc",
        "enc": enc,
        "rt": 0.9,
        "videoFaceCaptureEnc": videoFaceCaptureEnc,
        "dtype": "Video",
        "_t": current_time,
        "attDuration": attDuration,
        "attDurationEnc": attDurationEnc
    }
    # print(params)
    # 定义请求头
    headers = {
        "Host": "mooc1.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "Content-Type": "application/json",
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
    # request = requests.Request('GET', url, params=params)
    # referer = request.prepare().url
    # print(referer)
    # 打印响应内容
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    if '"isPassed":true' in response.text:
        return response.status_code, True
    else:
        return response.status_code, False


def send_studylog(cookie, courseid, clazzid, personId, aid, objectId, userid, knowledgeid, fid, jobid, mtEnc,
                  eventType):
    # 定义请求的 URL
    url = "https://mooc1.chaoxing.com/keeper/api/receive-studylog"

    # 定义请求头
    headers = {
        "Host": "mooc1.chaoxing.com",
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://mooc1.chaoxing.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": cookie
    }
    # 定义要发送的 log 数据
    log_data = {
        "courseId": courseid,
        "clazzId": clazzid,
        "personId": personId,
        "eventType": eventType,
        "eventTime": int(time.time() * 1000),
        "data": {
            "relationId": aid,
            "objectId": objectId,
            "userId": userid,
            "knowledgeId": knowledgeid,
            "fid": fid,
            "jobId": jobid
        }
    }

    # 将 log 数据转换为 JSON 字符串
    log_json = json.dumps(log_data)

    # 定义要发送的表单数据
    data = {
        "log": log_json,
        "enc": mtEnc
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=data, verify=False)

    # 打印响应内容
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)


def get_dftu(objectid, from_value, cookie, userid, imgcount, ):
    # 定义请求的 URL
    # print(objectid)
    # print(from_value)
    # url = "https://pan-yz.chaoxing.com/screen/file_8d128ee00fa7b354857c8652f6dedced?ext=%7B%22_from_%22%3A%22245055799_104076320_254538083_e619568b77200ae4e7cc053e489355ba%22%7D"
    url = "https://pan-yz.chaoxing.com/screen/file_" + objectid + "?ext=%7B%22_from_%22%3A%22" + from_value + "%22%7D"
    # 定义请求头
    headers = {
        "Host": "pan-yz.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "iframe",
        "Referer": "https://mooc1.chaoxing.com/ananas/modules/pdf/index.html?v=2024-0906-2130",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": cookie
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, verify=False)

    # 输出响应内容
    # print("Status Code:", response.status_code)
    # print("Response Text:", response.text)

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到指定的 div
    div = soup.find('div', id='markDataStr')

    if div:
        # &d=7B%5C%22_from_%5C%22%3A%5C%22245055799_104076320_254538083_e619568b77200ae4e7cc053e489355ba%5C%22%7D%22%7D&t=20241120170045401&enc=032b23c99606462b92b6e6d716a00312
        # 获取 JSON 字符串
        json_str = div.string
        # 解析 JSON 字符串
        data = json.loads(json_str)
        # print("Extracted JSON:", data)
        wordcount = ''
        for i in range(int(imgcount)):
            wordcount += str(i) + '\n'
        wordcount = len(wordcount)
        resouceId = data['resourceID']
        resourceType = data['resourceType']
        location = str(data['location'])
        _from = str(data['from'])
        curPage = str(data['curPage'])
        totalPage = str(data['totalPage'])
        f = "readPoint"
        u = userid
        # d = "%7B%22r%22%3A%22" + resouceId + "%22%2C%22t%22%3A%22" + resourceType + "%22%2C%22l%22%3A" + location \
        #     + "%2C%22f%22%3A" + _from + "%2C%22p%22%3A" + curPage + "%2C%22tp%22%3A" + totalPage + "%2C%22wc%22%3A" \
        #     + wordcount + "%2C%22ic%22%3A" + imgcount + "%2C%22v%22%3A2%2C%22s%22%3A1%2C%22h%22%3A0%2C%22ext%22%3A%22%" + \
        #     ext
        d = '{"r":"' + resouceId + '","t":"' + resourceType + '","l":' + location + ',"f":' + _from + ',"p":' + curPage + ',"tp":' + totalPage + ',"wc":' + str(
            wordcount) + ',"ic":' + str(
            imgcount) + ',"v":2,"s":1,"h":0,"ext":"{\\"_from_\\":\\"' + from_value + '\\"}"}'
        d = urllib.parse.quote(d)

        # 获取当前时间
        now = datetime.now()

        # 格式化为所需的字符串格式
        t = now.strftime('%Y%m%d%H%M%S') + str(int(now.microsecond / 1000)).zfill(3)

        # print(f, u, d, t)
        return f, u, d, t
    else:
        print("No match found.")


def send_mark(f, u, d, t, enc, objectid, from_value):
    # 定义请求的 URL
    url = "https://data-xxt.aichaoxing.com/analysis/ac_mark"

    # 定义请求的参数
    params = {
        'f': f,
        'u': u,
        'd': d,
        't': t,
        'enc': enc
    }

    # 定义请求头
    headers = {
        'Host': 'data-xxt.aichaoxing.com',
        'Connection': 'keep-alive',
        'sec-ch-ua-platform': '"Windows"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Origin': 'https://pan-yz.chaoxing.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://pan-yz.chaoxing.com/screen/file_' + objectid + '?ext={"_from_":"' + from_value + '"}',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7'
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params, verify=False)

    # 打印响应内容
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)


def video_minitor():
    # 设置请求的 URL 和参数
    random_number = random.random()
    callback_name = 'jsonp' + str(random_number).replace(".", "")
    t = int(time.time() * 1000)
    url = "https://detect.chaoxing.com/api/monitor"
    params = {
        "version": "1731828748503",
        "refer": "http://i.mooc.chaoxing.com",
        "from": "",
        "fid": "378",
        "jsoncallback": callback_name,
        "t": t
    }

    # 设置请求头
    headers = {
        "Host": "detect.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "script",
        # "Referer": "https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=888803601&courseId=245055799&clazzid=104076320&cpi=285104941&enc=e619568b77200ae4e7cc053e489355ba&mooc2=1&openc=d4f870ff250a870e94459efb37476bfc",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7"
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params, verify=False)

    # 打印响应内容
    print(response.text)


def allsubtitle(mid, objectid, courseid, cookie):
    url = "https://mooc1.chaoxing.com/mooc-ans/richvideo/allsubtitle"
    t = int(time.time() * 1000)
    # 定义请求的参数
    params = {
        'mid': mid,
        'objectid': objectid,
        'courseid': courseid,
        '_dc': t
    }

    # 定义请求头
    headers = {
        'Host': 'mooc1.chaoxing.com',
        'Connection': 'keep-alive',
        'sec-ch-ua-platform': '"Windows"',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        "Cookie": cookie
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params)

    # 打印响应内容
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)


def viewpic(thumb_http, thumb_enc, cookie):
    url = "https://mooc1.chaoxing.com/mooc-ans/richvideo/viewpic"
    t = int(time.time() * 1000)

    params = {
        'url': thumb_http,
        'enc': thumb_enc,
        '_dc': t
    }

    # 定义请求头
    headers = {
        'Host': 'mooc1.chaoxing.com',
        'Connection': 'keep-alive',
        'sec-ch-ua-platform': '"Windows"',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        "Cookie": cookie
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params)

    # 打印响应内容
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)


def initdatawithviewerV2(mid, cpi, clazzid, courseid, cookie):
    url = "https://mooc1.chaoxing.com/mooc-ans/richvideo/initdatawithviewerV2"

    t = int(time.time() * 1000)
    # 定义请求的参数
    params = {
        'mid': mid,
        'cpi': cpi,
        'classid': clazzid,
        'courseid': courseid,
        '_dc': t
    }

    # 定义请求头
    headers = {
        'Host': 'mooc1.chaoxing.com',
        'Connection': 'keep-alive',
        'sec-ch-ua-platform': '"Windows"',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        "Cookie": cookie
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params)

    # 打印响应内容
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)


def get_points(courseid, mid, cookie):
    url = "https://mooc1.chaoxing.com/ananas/getpoints"
    t = int(time.time() * 1000)
    # 定义请求的参数
    params = {
        'courseid': courseid,
        'mid': mid,
        '_dc': t
    }

    # 定义请求头
    headers = {
        'Host': 'mooc1.chaoxing.com',
        'Connection': 'keep-alive',
        'sec-ch-ua-platform': '"Windows"',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'Cookie': cookie
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params)

    # 打印响应内容
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

def ac_mark(objectid3, from_value, cookie, userid, imgcount, objectid):
    f, u, d, t = get_dftu(objectid3, from_value, cookie, userid, imgcount)
    enc = dftu_enc(d, f, t, u)
    send_mark(f, u, d, t, enc, objectid, from_value)
