## 学习通破解流程

总结：虽然破解了前端加密，也完成了模拟发包，但是无法绕过人脸验证，所以只是一个自娱自乐的项目。

其他人的成品我也有试过，都无法破解人脸验证，我想或许在手机端可能会更好实现绕过，毕竟pc端的人脸验证也是通过手机扫码实现的。

##### 1、绕过人脸

使用https://mooc2-ans.chaoxing.com/mycourse/studentcourse?代替掉人脸验证界面的https://mooc1-1.chaoxing.com/mooc-ans/visit/stucoursemiddle?

##### 2、关闭反调试

```js
Function.prototype.temp_constructor= Function.prototype.constructor; Function.prototype.constructor=function(){
    if (arguments && typeof arguments[0]==="string"){
        if (arguments[0]==="debugger")    
    		return "" } 
 	return Function.prototype.temp_constructor.apply(this, arguments); };

```

##### 3、绕过视频页人脸

```
document.addEventListener("DOMContentLoaded", function() {
    var chapterVideoFaceQrMaskDiv = document.querySelector(".chapterVideoFaceQrMaskDiv");
    if (chapterVideoFaceQrMaskDiv) {
        // 隐藏该元素
        chapterVideoFaceQrMaskDiv.style.display = "none";
    }
});

var chapterVideoFaceQrMaskDiv = document.querySelector(".chapterVideoFaceQrMaskDiv");
    if (chapterVideoFaceQrMaskDiv) {
        // 隐藏该元素
        chapterVideoFaceQrMaskDiv.style.display = "none";
    }
```

##### 4、关闭事件监听器

关闭网页中关于移动鼠标之后视频暂停的事件监听器

mouseout中的window

~~赤石大王~~

exp：



```
Function.prototype.temp_constructor= Function.prototype.constructor; Function.prototype.constructor=function(){
    if (arguments && typeof arguments[0]==="string"){
        if (arguments[0]==="debugger")    
    		return "" } 
 	return Function.prototype.temp_constructor.apply(this, arguments); };
document.addEventListener("DOMContentLoaded", function() {
    var chapterVideoFaceQrMaskDiv = document.querySelector(".chapterVideoFaceQrMaskDiv");
    if (chapterVideoFaceQrMaskDiv) {
        // 隐藏该元素
        chapterVideoFaceQrMaskDiv.style.display = "none";
    }
});
```

##### 5、抓包

视频检测包

正常发包返回403

看看能不能逆向出算法

```
GET https://mooc1.chaoxing.com/mooc-ans/multimedia/log/a/285104941/e62bbeef83a5e41bda3fd0e930170efa?clazzId=104076320&playingTime=531&duration=2901&clipTime=0_2901&objectId=5a276d0b6fed472617a68a1456d0548a&otherInfo=nodeId_888803598-cpi_285104941-rt_d-ds_0-ff_1-be_0_0-vt_1-v_6-enc_6ba82be3774b660f3209d0296577257b&courseId=245055799&jobid=1519952205147318&userid=254538083&isdrag=0&view=pc&enc=905962284bf268a9291aeeab0e456751&rt=0.9&videoFaceCaptureEnc=f91dd63bdfbfa251239b30846a947f54&dtype=Video&_t=1731508491338&attDuration=2901&attDurationEnc=3deae503a452a1714f68acfaedaae238 HTTP/1.1
Host: mooc1.chaoxing.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
Content-Type: application/json
sec-ch-ua-mobile: ?0
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: fid=378; lv=3; _uid=254538083; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; xxtenc=21218285d5d4f3a17cb3c0511867d711; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6de401a3b9d3787d6f9f471d130e75e4cc49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe537c1800dc0287af8ce346aa2e3718c8; _d=1731506032795; vc2=336ACDD7C888018FA1F74BC8B8AF99F2; vc3=JiFCZTzIHvpf0%2B0KWmIYlvMVJK%2B3n7j9TN6p1te1ho2SlUo48wLXivRQWv3QMo%2FgHEh3z7Wv5tTel8qeYxb3lB0Whj%2B6pho3geZcvFK2RMplzyiJ8p3eLKHWAL6f%2BUDP02OV8LzScq5c1JzKh4F6XXvsEWbzQz16H7IOObZa7I4%3D48a69601a07c75d5b9bcad98b047bedd; cx_p_token=87e89354869f71071ab190ff9f1c3e23; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE1MDYwMzI3OTcsImV4cCI6MTczMjExMDgzMn0.0XDvj7wy23Egdmr8w1FzhnEVEGcgpU36pWV1uDmQBpo; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731506032797; createSiteSource=num8; source=num8; wfwEnc=4E59B739D4AAA28FC8F126AEA9ACED4F; spaceFid=378; spaceRoleId=""; k8s=1731507984.504.11251.466485; jrose=FC955C97063B243656E2C896EE36F4BC.mooc-3085126854-grd4s; route=c010ccedb771f8b7c7793c67ee1d2aae; videojs_id=1273735; writenote=yes


```

```
GET https://mooc1.chaoxing.com/mooc-ans/multimedia/log/a/285104941/e62bbeef83a5e41bda3fd0e930170efa?clazzId=104076320&playingTime=651&duration=2901&clipTime=0_2901&objectId=5a276d0b6fed472617a68a1456d0548a&otherInfo=nodeId_888803598-cpi_285104941-rt_d-ds_0-ff_1-be_0_0-vt_1-v_6-enc_6ba82be3774b660f3209d0296577257b&courseId=245055799&jobid=1519952205147318&userid=254538083&isdrag=0&view=pc&enc=ca6f3fa5731c8ac9de5acd139a6227c3&rt=0.9&videoFaceCaptureEnc=f91dd63bdfbfa251239b30846a947f54&dtype=Video&_t=1731508611471&attDuration=2901&attDurationEnc=3deae503a452a1714f68acfaedaae238 HTTP/1.1
Host: mooc1.chaoxing.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
Content-Type: application/json
sec-ch-ua-mobile: ?0
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: fid=378; lv=3; _uid=254538083; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; xxtenc=21218285d5d4f3a17cb3c0511867d711; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6de401a3b9d3787d6f9f471d130e75e4cc49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe537c1800dc0287af8ce346aa2e3718c8; _d=1731506032795; vc2=336ACDD7C888018FA1F74BC8B8AF99F2; vc3=JiFCZTzIHvpf0%2B0KWmIYlvMVJK%2B3n7j9TN6p1te1ho2SlUo48wLXivRQWv3QMo%2FgHEh3z7Wv5tTel8qeYxb3lB0Whj%2B6pho3geZcvFK2RMplzyiJ8p3eLKHWAL6f%2BUDP02OV8LzScq5c1JzKh4F6XXvsEWbzQz16H7IOObZa7I4%3D48a69601a07c75d5b9bcad98b047bedd; cx_p_token=87e89354869f71071ab190ff9f1c3e23; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE1MDYwMzI3OTcsImV4cCI6MTczMjExMDgzMn0.0XDvj7wy23Egdmr8w1FzhnEVEGcgpU36pWV1uDmQBpo; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731506032797; createSiteSource=num8; source=num8; wfwEnc=4E59B739D4AAA28FC8F126AEA9ACED4F; spaceFid=378; spaceRoleId=""; k8s=1731507984.504.11251.466485; jrose=FC955C97063B243656E2C896EE36F4BC.mooc-3085126854-grd4s; route=c010ccedb771f8b7c7793c67ee1d2aae; videojs_id=1273735; writenote=yes


```

页面检测包

感觉应该是检测是不是在别的浏览器播放的包

```
GET https://detect.chaoxing.com/api/monitor?version=1731508206578&refer=http%3A%2F%2Fi.mooc.chaoxing.com&from=&fid=378&jsoncallback=jsonp08688927060430742&t=1731508596567 HTTP/1.1
Host: detect.chaoxing.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Accept: */*
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: script
Referer: https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=888803598&courseId=245055799&clazzid=104076320&cpi=285104941&enc=e619568b77200ae4e7cc053e489355ba&mooc2=1&openc=d4f870ff250a870e94459efb37476bfc
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: fid=378; lv=3; _uid=254538083; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; xxtenc=21218285d5d4f3a17cb3c0511867d711; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6de401a3b9d3787d6f9f471d130e75e4cc49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe537c1800dc0287af8ce346aa2e3718c8; _d=1731506032795; vc2=336ACDD7C888018FA1F74BC8B8AF99F2; vc3=JiFCZTzIHvpf0%2B0KWmIYlvMVJK%2B3n7j9TN6p1te1ho2SlUo48wLXivRQWv3QMo%2FgHEh3z7Wv5tTel8qeYxb3lB0Whj%2B6pho3geZcvFK2RMplzyiJ8p3eLKHWAL6f%2BUDP02OV8LzScq5c1JzKh4F6XXvsEWbzQz16H7IOObZa7I4%3D48a69601a07c75d5b9bcad98b047bedd; cx_p_token=87e89354869f71071ab190ff9f1c3e23; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE1MDYwMzI3OTcsImV4cCI6MTczMjExMDgzMn0.0XDvj7wy23Egdmr8w1FzhnEVEGcgpU36pWV1uDmQBpo; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731506032797; createSiteSource=num8; source=num8; wfwEnc=4E59B739D4AAA28FC8F126AEA9ACED4F; spaceFid=378; spaceRoleId=""; JSESSIONID=83232CDDCAFD875478D78D8ECB650E25


```

```
正常返回
HTTP/1.1 200 OK
Date: Wed, 13 Nov 2024 14:36:36 GMT
Content-Type: text/html;charset=UTF-8
Content-Length: 78
Connection: keep-alive
Set-Cookie: JSESSIONID=61A07ECBC1DC4B6363AA910329A34123; Path=/; HttpOnly
upstreamdocker: 172.30.117.6:8081
Origin-Agent-Cluster: ?0

jsonp08688927060430742('{"refer":"http://i.mooc.chaoxing.com","status":true}')
```

##### 6、js前端调试

```
_0x37e6a1[_0x1400d4]['call'](_0x1251fb, _0x1ea38e, _0x37f329);

_0x37e6a1是一个array，_0x1400d4是0，_0x1251fb是video元素集合，_0x1ea38e是object元素集合，_0x37f329是undefined

var _0x2399c1 = _0x2b57c5;

_0x2b57c5是一个函数返回的结果

 return _0x2b413c[_0x2399c1(0x26e)](_0x8b7bc6, arguments);
 _0x2b413c是一个函数，_0x8b7bc6是跟video相关的元素集合，arguments是一个集合
 
 
current = 173.51989
isSuppostFace


clazzId userid jobid objectid  SALT=d_yHJ!$pdA~5  duration

reportURL dtoken 

join jobid hasJobLimit videoTimeLimit
```

```
public function onSendlog(logdata:Object, isdrag:int) : void
      {
         var url:String = null;
         var key:String = null;
         var n:int = 0;
         var enc:String = null;
         var t:int = 0;
         if(Boolean(logdata.chapterId) && isdrag != 1)
         {
            t = 0;
            if(isdrag == 4 || isdrag == 2)
            {
               t = 2;
            }
            else if(isdrag == 3)
            {
               t = 1;
            }
            url = "s=" + logdata.clazzId + "&c=" + logdata.chapterId + "&o=" + logdata.objectId + "&st=" + t + "&m=0&d=" + logdata.duration;
            enc = MD5.startMd("[" + logdata.chapterId + "]" + "[" + logdata.clazzId + "]" + "[" + logdata.duration + "]" + "[0]" + "[" + logdata.objectId + "]" + "[" + t + "]" + "[535e933c498001]");
            url = url + "&enc=" + enc;
            this.jQuery("sendlogzt",url);
         }
         if(logdata.isSendLog != "1")
         {
            return;
         }
         url = "";
         var isSendLog:String = "";
         for(key in logdata)
         {
            if(key == "isSendLog")
            {
               isSendLog = logdata[key];
            }
            else if(key != "dtoken")
            {
               url += "&" + key + "=" + logdata[key];
            }
         }
         n = this.getPlaySecond();
         url = url + "&view=pc&playingTime=" + n;
         url = url + "&isdrag=" + isdrag;
         enc = MD5.startMd("[" + logdata.clazzId + "]" + "[" + logdata.userid + "]" + "[" + logdata.jobid + "]" + "[" + logdata.objectId + "]" + "[" + n * 1000 + "]" + "[d_yHJ!$pdA~5]" + "[" + int(logdata.duration) * 1000 + "]" + "[" + logdata.clipTime + "]");
         url = url + "&enc=" + enc;
         url = url.substring(1);
         if(isSendLog == "1")
         {
            this.jQuery("logFunc",url);
         }
      }
```

这个是检测视频播放的请求包，返回值为任务点是否完成，涉及到的变量有clazzId、playingTime、duration、clipTime、objectId、otherInfo、courseId、jobid、userid、isdrag、view、enc、rt、videoFaceCaptureEnc、dtype、_t、attDuration、attDurationEnc，其中只有enc和 _ t是通过计算得到的，其他值都是从对象中直接获得。

命名这个包为包1，注意这个包发包还有url中的285104941，3acd6107bc789e522df3f6bec8017c07，第一个是cpi，第二个是dtoken

```
https://mooc1.chaoxing.com/mooc-ans/multimedia/log/a/285104941/3acd6107bc789e522df3f6bec8017c07?clazzId=104076320&playingTime=173&duration=1243&clipTime=0_1243&objectId=3090c9236e7c9161b718f5718edfef1d&otherInfo=nodeId_888803600-cpi_285104941-rt_d-ds_0-ff_1-be_0_0-vt_1-v_6-enc_9eb5bc8431eda809e993a17897c7310e&courseId=245055799&jobid=151989526627791&userid=254538083&isdrag=3&view=pc&enc=c8e9f31467791385d36d0d1879971279&rt=0.9&videoFaceCaptureEnc=4f8b76990bda7c44739106640da3339c&dtype=Video&_t=1731682457125&attDuration=1243&attDurationEnc=1bda01ac60c0ad70129c198518f21432

HTTP/1.1 200
Date: Fri, 15 Nov 2024 14:54:14 GMT
Content-Type: application/json;charset=utf-8
Content-Length: 61
Connection: keep-alive
Rose: mooc-3085126854-grd4s
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET
Access-Control-Allow-Credentials: true
upstreamdocker: 172.177.54.13:8080
Referrer-Policy: unsafe-url
Origin-Agent-Cluster: ?0

{"isPassed":false,"videoTimeLimit":false,"hasJobLimit":false}
```

根据这个包可以查找数据存储的路径

首先搜索clazzId，可以发现存储在这个请求包中，这个请求包会返回一个mArg数据，包含了clazzId、objectId、otherInfo、courseId、jobid、userid、videoFaceCaptureEnc、attDuration、attDurationEnc，接下来只需要寻找playingTime、duration、clipTime、isdrag、view、enc、rt、dtype、_t

命名这个包为包2

```
https://mooc1.chaoxing.com/mooc-ans/knowledge/cards?clazzid=104076320&courseid=245055799&knowledgeid=888803600&num=0&ut=s&cpi=285104941&v=20160407-3&mooc2=1&isMicroCourse=false

GET https://mooc1.chaoxing.com/mooc-ans/knowledge/cards?clazzid=104076320&courseid=245055799&knowledgeid=888803600&num=0&ut=s&cpi=285104941&v=20160407-3&mooc2=1&isMicroCourse=false HTTP/1.1
Host: mooc1.chaoxing.com
Connection: keep-alive
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: iframe
Referer: https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=888803600&courseId=245055799&clazzid=104076320&cpi=285104941&enc=e619568b77200ae4e7cc053e489355ba&mooc2=1&openc=d4f870ff250a870e94459efb37476bfc
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: k8s=1731507984.504.11251.466485; route=c010ccedb771f8b7c7793c67ee1d2aae; writenote=yes; videojs_id=4083103; lv=3; fid=378; _uid=254538083; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6092f7e000996af8221eb536edab03657c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe335d2c507a0b4c1ce7b5d52e475bea55; _d=1731741734625; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; vc2=AB2963DF883FA02611ED455D5EE60B69; vc3=AUDlay24%2B2ygacoBROFq0HHpVMn0sSF0K%2B1hBa8bvFoQZDI56j9Zq4%2FW5qbwE%2B7KlDgtv%2Btx%2BTQ2SaD3wFOr8%2BAOajHTuXX2Fo0e6KcQZ1Wzn0Ojdv2NxJeYo6w019AFUstzBBHl9d3WfrUNe9Ih9hSbDi8Oy4FgdHvOFOwFya0%3Df22b6eeda40e4a6e7b4770a36f63e0a4; cx_p_token=34ff39e566a5babaf121124d1b097b03; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE3NDE3MzQ2MjcsImV4cCI6MTczMjM0NjUzNH0.fcpM7BlIbETOk1K4AavrhcFuajgDHlLyS3l9P3h5LDI; xxtenc=21218285d5d4f3a17cb3c0511867d711; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731741734627; createSiteSource=num8; source=num8; wfwEnc=4E59B739D4AAA28FC8F126AEA9ACED4F; spaceFid=378; spaceRoleId=""; jrose=5ECFDA28EB872C8CE1D9FE514C5DFAD6.mooc-444288205-mtj7s



mArg = {"hiddenConfig":false,"isMirror":false,"attachments":[{"headOffset":173000,"otherInfo":"nodeId_888803600-cpi_285104941-rt_d-ds_0-ff_1-be_0_0-vt_1-v_6-enc_9eb5bc8431eda809e993a17897c7310e&courseId=245055799","isPassed":false,"mid":"12009108168101519895266092","jumpTimePointList":[],"type":"video","begins":0,"jobid":"151989526627791","customType":0,"attDurationEnc":"1bda01ac60c0ad70129c198518f21432","videoFaceCaptureEnc":"4f8b76990bda7c44739106640da3339c","ends":0,"randomCaptureTime":180,"property":{"switchwindow":"true","hsize":"236.22 MB","module":"insertvideo","mid":"12009108168101519895266092","type":".mp4","jobid":"151989526627791","size":247689864,"fastforward":"true","retract":"false","name":"工程经济分析的基本要素.mp4","ywbf":1,"doublespeed":0,"objectid":"3090c9236e7c9161b718f5718edfef1d","_jobid":"151989526627791"},"playTime":173000,"attDuration":1243,"headOffsetVersion":0,"job":true,"aid":1802157384,"objectId":"3090c9236e7c9161b718f5718edfef1d"},{"begins":0,"otherInfo":"nodeId_888803600-cpi_285104941","ends":0,"jtoken":"8cc533d876b1e2cb222d9979a364d1f4","property":{"size":251933,"hsize":"246.03 KB","retract":"false","module":"insertdoc","name":"第2讲 工程经济分析的基本要素1.pptx","mid":"10542678357891519788717279","type":".pptx","pagenum":"29","objectid":"4c7ad0fc6c66f1d8e52387436cb66c46","_jobid":"1585558613939612"},"mid":"10542678357891519788717279","enc":"580144c8879400e0f78c080d65cd7384","type":"document","aid":1802157385}],"coursename":"工程管理（2024秋）","defaults":{"fid":"378","ktoken":"7f71ae3ff69bd9b11f45b66736372d6d","mtEnc":"db83d900fcf307b3e660a78f7ab096d7","appInfo":"","playingCapture":1,"videoAutoPlay":0,"userid":"254538083","reportTimeInterval":60,"showVideoWaterMark":1,"endCapture":1,"defenc":"7fcea31861f16c9824b6bb32cc2d11a3","cardid":846583536,"imageUrl":"https://p.ananas.chaoxing.com/star3/origin/06fb7fde8e9630c900b3614f16eedab3.jpg","loginName":"3122004438","state":0,"cpi":285104941,"captureInterval":0,"playAginCapture":1,"startCapture":1,"isFiled":0,"ignoreVideoCtrl":0,"reportUrl":"https://mooc1.chaoxing.com/mooc-ans/multimedia/log/a/285104941","chapterCapture":1,"initdataUrl":"https://mooc1.chaoxing.com/mooc-ans/richvideo/initdatawithviewer","cFid":"378","knowledgeid":888803600,"videoTopicCloud":0,"qnenc":"fa55a7a1310db1ece195bc5e7514a194","clazzId":104076320,"chapterCollectionType":0,"lastmodifytime":1731292759000,"aiVideoInterpret":0,"courseid":245055799,"subtitleUrl":"https://mooc1.chaoxing.com/mooc-ans/richvideo/subtitle","playingLoopCapture":1,"username":"黄光昊"},"mooc2":1,"knowledgename":"资产","control":true,"chapterVideoTranslate":0,"isErya":2,"ut":"s"};

```

在这个包中可以找到duration和dtoken，接下来还缺少playingTime、clipTime、isdrag、view、enc、rt、dtype、_t，其中 _t和enc是自己生成的，view应该是个固定值，clipTime就是变换了一下的duration，那么就还差playingTime、isdrag、view、rt、dtype，其中isdrag、view、rt、dtype的值都是固定值，而playingTime是自定义的值，因为要模拟发包，而playingTime就是已经播放了的视频的时长，所以这个值是自定义的，不需要获取。

命名这个包为包3，url中还包括一个objectId

```
https://mooc1.chaoxing.com/ananas/status/3090c9236e7c9161b718f5718edfef1d?k=378&flag=normal&_dc=1731683760675 

{"length":247689864,"thumbnailsEnc":"2f5e6fd8c26d0754a17e3a77d961d4ed","screenshot":"https://p2.ananas.chaoxing.com/sv-w3/video/5a/73/90/3090c9236e7c9161b718f5718edfef1d/snapshot.jpg","dtoken":"3acd6107bc789e522df3f6bec8017c07","duration":1243,"mp3":"https://s2.ananas.chaoxing.com/sv-w3/video/5a/73/90/3090c9236e7c9161b718f5718edfef1d/mp3/","download":"http://d0.ananas.chaoxing.com/download/3090c9236e7c9161b718f5718edfef1d?at_=1731682071523&ak_=d994d9f3cfc4f0837ce7de0ccecabd33&ad_=af0a23b94977bb18c8684217ca3b647c","filename":"工程经济分析的基本要素.mp4","crc":"5718480e3b2e8737b3e20b7ef34946aa","public_cdn_prefix":["s2","s1"],"http":"https://s2.ananas.chaoxing.com/sv-w3/video/5a/73/90/3090c9236e7c9161b718f5718edfef1d/sd.mp4?at_=1731682071524&ak_=5dea197ec0152ff9d3521cd018388aaa&ad_=1a313e160b7aa1ffe489a79db8776db0","thumbnails":"https://p2.ananas.chaoxing.com/sv-w3/video/5a/73/90/3090c9236e7c9161b718f5718edfef1d/thumbnails/","objectid":"3090c9236e7c9161b718f5718edfef1d","key":"a9df69e3b561f00ec4773ebd84f1dbf1","status":"success"}
```

然后解决包2和包3的参数问题

包2的参数为clazzid、courseid、knowledgeid、num、ut、cpi、v、mooc2、isMicroCourse

包3的参数为k、flag、_dc，k应该是固定值，flag应该是固定值， _dc应该是个时间戳

命名这个包为包4

在包4返回的关于课程的词条中有一个value，那个就是knowledgeid

经过观察，num、ut、v、mooc2、isMicroCourse都是固定值，所以只需要clazzid、courseid和cpi

```
GET https://mooc2-ans.chaoxing.com/mycourse/studentcourse?courseid=245055799&clazzid=104076320&vc=1&cpi=285104941&ismooc2=1&v=2 HTTP/1.1
Host: mooc2-ans.chaoxing.com
Connection: keep-alive
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Sec-Purpose: prefetch;prerender
Purpose: prefetch
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: fid=378; k8s=1731507532.145.4114.378267; route=ac9a7739314fa6817cbac7e56032374b; jrose=406F6F019A24E6BDF5965BA16542D34B.mooc2-659113057-c48j2; lv=3; _uid=254538083; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6365f7e369648819dbc1ceabd8811a5d4c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe35523a45b6210570e7b5d52e475bea55; _d=1731724814682; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; vc2=AB2963DF883FA02611ED455D5EE60B69; vc3=MqsP8Os7FB894wSZU61GwhQUKpzrGoXw7wxVfIQyb5clobl2qaOTyKmWDi3eSBJowRbM4%2BCDvGn%2B2aTRthz1tewCCmDYDlx4G5GO6hTBIVDzGcqTOtltKSNw2JBmr9%2BP9KUn7F38a9Fc8mS9sO%2FUvGmcdAQwLM4j2ILJ0Pa5pIQ%3Db7fa26571b37b499399ac8dd2872c829; cx_p_token=9352bf516acb1461053856791f28acfe; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE3MjQ4MTQ2ODMsImV4cCI6MTczMjMyOTYxNH0.J24DHZQ2Xowd7N8ABA134tei6to5VhKhYTTZV3Iqfyg; xxtenc=21218285d5d4f3a17cb3c0511867d711; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731724814683; createSiteSource=num8; source=num8; wfwEnc=4E59B739D4AAA28FC8F126AEA9ACED4F; spaceFid=378; spaceRoleId=""

...
<div class="inputCheck fl"><input type="checkbox" name="checkbox" value="888803600"/></div>
...
```

命名为包5

在包5的返回中有一个关于课程的词条，包括了cpi、clazzid和courseid

```
POST https://mooc1-1.chaoxing.com/mooc-ans/visit/courselistdata HTTP/1.1
Host: mooc1-1.chaoxing.com
Connection: keep-alive
Content-Length: 80
sec-ch-ua-platform: "Windows"
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: text/html, */*; q=0.01
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
sec-ch-ua-mobile: ?0
Origin: https://mooc1-1.chaoxing.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://mooc1-1.chaoxing.com/visit/interaction?s=b7218d31024eb57c03a05e9c9358f603
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: fid=378; k8s=1731507531.164.12664.493064; route=7644025d506561102d55bac4c90cbeeb; lv=3; _uid=254538083; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6365f7e369648819dbc1ceabd8811a5d4c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe35523a45b6210570e7b5d52e475bea55; _d=1731724814682; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; vc2=AB2963DF883FA02611ED455D5EE60B69; vc3=MqsP8Os7FB894wSZU61GwhQUKpzrGoXw7wxVfIQyb5clobl2qaOTyKmWDi3eSBJowRbM4%2BCDvGn%2B2aTRthz1tewCCmDYDlx4G5GO6hTBIVDzGcqTOtltKSNw2JBmr9%2BP9KUn7F38a9Fc8mS9sO%2FUvGmcdAQwLM4j2ILJ0Pa5pIQ%3Db7fa26571b37b499399ac8dd2872c829; cx_p_token=9352bf516acb1461053856791f28acfe; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE3MjQ4MTQ2ODMsImV4cCI6MTczMjMyOTYxNH0.J24DHZQ2Xowd7N8ABA134tei6to5VhKhYTTZV3Iqfyg; xxtenc=21218285d5d4f3a17cb3c0511867d711; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731724814683; createSiteSource=num8; source=num8; wfwEnc=4E59B739D4AAA28FC8F126AEA9ACED4F; spaceFid=378; spaceRoleId=""; jrose=3CA050249161E3332E0F52A7FC12EF84.mooc-444288205-4vxls

courseType=1&courseFolderId=0&baseEducation=0&superstarClass=&courseFolderSize=0


...
<li class="course clearfix" courseId="245055799" clazzId="104076320" personId="285104941" id="course_245055799_104076320">
...
```

接下来获取一下cookie，所有发包都是需要cookie的

命名为包6，这个getauthstatus应该是根据uuid生成的二维码来判断的，所以想要有效访问就应该先扫二维码

包6中包含两个参数，enc和uuid，还有cookie，注意包6只是返回了一部分cookie，另外的cookie是别的包set的。

```
POST https://passport2.chaoxing.com/getauthstatus HTTP/1.1
Host: passport2.chaoxing.com
Connection: keep-alive
Content-Length: 74
sec-ch-ua-platform: "Windows"
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/javascript, */*; q=0.01
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
sec-ch-ua-mobile: ?0
Origin: https://passport2.chaoxing.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://passport2.chaoxing.com/cloudscanlogin?mobiletip=%e7%94%b5%e8%84%91%e7%ab%af%e7%99%bb%e5%bd%95%e7%a1%ae%e8%ae%a4&time=1731724796305&pcrefer=https://v1.chaoxing.com/backSchool/toLogin?source=num8
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: fid=378; route=3a66e47c0ac92560e5c67cd5e1803201; retainlogin=1; JSESSIONID=1A056B0707810954ADBAAEDE96B3CDBD

enc=9ca8c0a50b23f633694986474cf2b30e&uuid=3eb036c6a97648879bd9f82d5c9cb2b0


Set-Cookie: lv=3; Domain=.chaoxing.com; Expires=Mon, 16-Dec-2024 02:40:14 GMT; Path=/
Set-Cookie: fid=378; Domain=.chaoxing.com; Expires=Mon, 16-Dec-2024 02:40:14 GMT; Path=/
Set-Cookie: _uid=254538083; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:40:14 GMT; Path=/
Set-Cookie: uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6365f7e369648819dbc1ceabd8811a5d4c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe35523a45b6210570e7b5d52e475bea55; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:40:14 GMT; Path=/
Set-Cookie: _d=1731724814682; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:40:14 GMT; Path=/
Set-Cookie: UID=254538083; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:40:14 GMT; Path=/
Set-Cookie: vc=95EFCA782B78211657973AE5692F481F; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:40:14 GMT; Path=/; HttpOnly
Set-Cookie: vc2=AB2963DF883FA02611ED455D5EE60B69; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:40:14 GMT; Path=/; HttpOnly
Set-Cookie: vc3=MqsP8Os7FB894wSZU61GwhQUKpzrGoXw7wxVfIQyb5clobl2qaOTyKmWDi3eSBJowRbM4%2BCDvGn%2B2aTRthz1tewCCmDYDlx4G5GO6hTBIVDzGcqTOtltKSNw2JBmr9%2BP9KUn7F38a9Fc8mS9sO%2FUvGmcdAQwLM4j2ILJ0Pa5pIQ%3Db7fa26571b37b499399ac8dd2872c829; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:40:14 GMT; Path=/; HttpOnly
Set-Cookie: cx_p_token=9352bf516acb1461053856791f28acfe; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:40:14 GMT; Path=/
Set-Cookie: p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE3MjQ4MTQ2ODMsImV4cCI6MTczMjMyOTYxNH0.J24DHZQ2Xowd7N8ABA134tei6to5VhKhYTTZV3Iqfyg; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:40:14 GMT; Path=/; HttpOnly
Set-Cookie: xxtenc=21218285d5d4f3a17cb3c0511867d711; Domain=.chaoxing.com; Expires=Mon, 16-Dec-2024 02:40:14 GMT; Path=/
Set-Cookie: DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731724814683; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:40:14 GMT; Path=/
Origin-Agent-Cluster: ?0

{"mes":"验证通过","status":true}
```

命名为包7，根据uuid会生成一个二维码，扫码之后才能getauthstatus，其中的mobiletip是电脑端登录确认

```
GET https://passport2.chaoxing.com/createqr?uuid=3eb036c6a97648879bd9f82d5c9cb2b0&xxtrefer=&type=1&clientid=&mobiletip=%E7%94%B5%E8%84%91%E7%AB%AF%E7%99%BB%E5%BD%95%E7%A1%AE%E8%AE%A4&fid= HTTP/1.1
Host: passport2.chaoxing.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: image
Referer: https://passport2.chaoxing.com/cloudscanlogin?mobiletip=%e7%94%b5%e8%84%91%e7%ab%af%e7%99%bb%e5%bd%95%e7%a1%ae%e8%ae%a4&time=1731724796305&pcrefer=https://v1.chaoxing.com/backSchool/toLogin?source=num8
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: fid=378; route=3a66e47c0ac92560e5c67cd5e1803201; retainlogin=1; JSESSIONID=1A056B0707810954ADBAAEDE96B3CDBD


```

命名为包8，最开始的起始包，返回值中包括了enc和uuid，但是本身就存在cookie，存在cookie应该是发送这个包之后会自动set

```
GET https://passport2.chaoxing.com/cloudscanlogin?mobiletip=%e7%94%b5%e8%84%91%e7%ab%af%e7%99%bb%e5%bd%95%e7%a1%ae%e8%ae%a4&time=1731724796305&pcrefer=https://v1.chaoxing.com/backSchool/toLogin?source=num8 HTTP/1.1
Host: passport2.chaoxing.com
Connection: keep-alive
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: iframe
Referer: https://v8.chaoxing.com/
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: fid=378; route=3a66e47c0ac92560e5c67cd5e1803201; retainlogin=1; JSESSIONID=1A056B0707810954ADBAAEDE96B3CDBD

...
<input type = "hidden" value="3eb036c6a97648879bd9f82d5c9cb2b0" id = "uuid"/>
		<input type = "hidden" value="9ca8c0a50b23f633694986474cf2b30e" id = "enc"/>
...
```

##### 7、模拟发包

使用request模块尝试模拟发包获得数据

```
访问https://passport2.chaoxing.com/cloudscanlogin，获得cookie1、uuid和enc

```

```
lv=3; Domain=.chaoxing.com; Expires=Mon, 16-Dec-2024 08:44:21 GMT; Path=/, 
fid=378; Domain=.chaoxing.com; Expires=Mon, 16-Dec-2024 08:44:21 GMT; Path=/, 
_uid=254538083; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:44:21 GMT; Path=/, uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6092f7e000996af82cb357548e07d9939c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fea1056353b090df48ee6bbd4b8e812e2e; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:44:21 GMT; Path=/,
_d=1731746661505; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:44:21 GMT; Path=/, 
UID=254538083; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:44:21 GMT; Path=/, 
vc=95EFCA782B78211657973AE5692F481F; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:44:21 GMT; Path=/; HttpOnly,
vc2=AB2963DF883FA02611ED455D5EE60B69; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:44:21 GMT; Path=/; HttpOnly, 
vc3=KQLCK9M1aOzm7ex5611%2BZdvBToClhfMSOXDaznvlXU2cvzaUKtSYaCkkr8DIBdng4DFV3BSIpd7B4w8QV5B1mkCkYf3re3eX4e6wq1W7u1W8%2Bcxnheyh2KPC51lt2MBZjPdENyjDZ7Wy8NpnOl0K%2BasE1CFRQtG2QLDRewSHNoc%3D277668883e723bb9cf049073b46c9be1; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:44:21 GMT; Path=/; HttpOnly, 
cx_p_token=ac699c904320ad9ac4f33fddb439e8ca; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:44:21 GMT; Path=/, 
p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE3NDY2NjE1MDcsImV4cCI6MTczMjM1MTQ2MX0.D9fsjoOy7zKWMdhzIuW-Y7X3uhb2tZHq2kesNVnMGw4; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:44:21 GMT; Path=/; HttpOnly, 
xxtenc=21218285d5d4f3a17cb3c0511867d711; Domain=.chaoxing.com; Expires=Mon, 16-Dec-2024 08:44:21 GMT; Path=/, 
DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731746661507; Domain=.chaoxing.com; Expires=Sat, 23-Nov-2024 19:44:21 GMT; Path=/
```

```
lv=3; 
Domain=.chaoxing.com; 
Expires=Sat, 23-Nov-2024 19:58:50 GMT; 
Path=/; 
vc2=AB2963DF883FA02611ED455D5EE60B69; vc3=QbvIXy6PVg2hkyCf2t1FlzsXMjnKTX8aZfxFMN9yqB3xT%2FOS3zF3rgXk9VAQySBXmXvU6y2ybtpGtqTmIDAygCs96UEcwSiOEwKco5%2BqdrCJhQLy87N2o1AVULxTfOGP8EYBHw1HXI9pv3TZDyQqAGiYtj5vYcUTCfsM%2FhwyUb4%3D6d94c764648ef24fac68dddec241503a; 
cx_p_token=3384bed595f86d9029e1a8a334cb7ce9; 
xxtenc=21218285d5d4f3a17cb3c0511867d711

lv=3; HttpOnly, vc2=AB2963DF883FA02611ED455D5EE60B69; HttpOnly, vc3=f9y9tpI3uM9oKYTS0SQY9Qt4rZzWRz5Zaf2FR4vxit4TWS6GckVpFCAC3cfbJRG27e%2Bp%2FcWQ8767m1Gl%2FoD2JLatLWSwr5lEbGgjdZW8wtZ3TTK15lFDhXGvWuDY5RN41i2PzoDfjsIyRRkF6jB0FETVnPa2uXegQyHKDnIVdLU%3Ddb72d1f05082530fed77b7f2127077b5; HttpOnly, cx_p_token=2b369aa4d13d93f64f3c45abcae12a4a; HttpOnly, xxtenc=21218285d5d4f3a17cb3c0511867d711

```

##### 8、视频播放模拟发包

```
GET https://mooc1.chaoxing.com/mooc-ans/courseapi/getvideohotdata?_dc=1731824259301&clazzid=104076320&knowledgeid=888803600&objectid=3090c9236e7c9161b718f5718edfef1d&courseid=245055799&cpi=285104941&ut=s HTTP/1.1
Host: mooc1.chaoxing.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: k8s=1731507984.504.11251.466485; route=c010ccedb771f8b7c7793c67ee1d2aae; writenote=yes; lv=3; fid=378; _uid=254538083; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6ac9d9a2f7a8a4d9933f4b9062323a079c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe33f68a3bfdd534836dec0d3b676e8e79; _d=1731812271468; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; vc2=1E20335C0E141E4951C658DE58D7A719; vc3=X%2FzVUiQmPP%2Fi3pjUkZJqnaAeyWFDgvay1nqcIS1QbIEje9M3ckAmpXTvVSLzDpG3%2B7GUeNSBMydJbhxBjBi3VCSgs9a6L1lFv2yEQTqQ%2FNWgaAOx9I9ScwdvdAdgpQeaboZnwF5Mv7bbk3C3uLSYjIw1OmZKP8GiU2JMy2qNhak%3D1bd94d24e672b720915458704aee92cb; cx_p_token=403097396f1bf921a104ac465c697240; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE4MTIyNzE0NjksImV4cCI6MTczMjQxNzA3MX0.YeO3oyePxWSU6fX2vajC-kN3SpW2vgUN5RJrjnPVqOg; xxtenc=21218285d5d4f3a17cb3c0511867d711; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731812271469; createSiteSource=num8; source=num8; wfwEnc=4E59B739D4AAA28FC8F126AEA9ACED4F; spaceFid=378; spaceRoleId=""; jrose=E9AA483D178B6126A739CFD892CB2204.mooc-444288205-mtj7s; videojs_id=7848134


```

```
GET https://mooc1.chaoxing.com/mooc-ans/multimedia/log/a/285104941/3acd6107bc789e522df3f6bec8017c07?clazzId=104076320&playingTime=0&duration=1243&clipTime=0_1243&objectId=3090c9236e7c9161b718f5718edfef1d&otherInfo=nodeId_888803600-cpi_285104941-rt_d-ds_0-ff_1-be_0_0-vt_1-v_6-enc_9eb5bc8431eda809e993a17897c7310e&courseId=245055799&jobid=151989526627791&userid=254538083&isdrag=3&view=pc&enc=48fa7f9c493442e093ca4f6643d5838b&rt=0.9&videoFaceCaptureEnc=6108e4fca186387d4d43e971752ee2f5&dtype=Video&_t=1731824259304&attDuration=1243&attDurationEnc=1bda01ac60c0ad70129c198518f21432 HTTP/1.1
Host: mooc1.chaoxing.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
Content-Type: application/json
sec-ch-ua-mobile: ?0
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: k8s=1731507984.504.11251.466485; route=c010ccedb771f8b7c7793c67ee1d2aae; writenote=yes; lv=3; fid=378; _uid=254538083; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6ac9d9a2f7a8a4d9933f4b9062323a079c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe33f68a3bfdd534836dec0d3b676e8e79; _d=1731812271468; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; vc2=1E20335C0E141E4951C658DE58D7A719; vc3=X%2FzVUiQmPP%2Fi3pjUkZJqnaAeyWFDgvay1nqcIS1QbIEje9M3ckAmpXTvVSLzDpG3%2B7GUeNSBMydJbhxBjBi3VCSgs9a6L1lFv2yEQTqQ%2FNWgaAOx9I9ScwdvdAdgpQeaboZnwF5Mv7bbk3C3uLSYjIw1OmZKP8GiU2JMy2qNhak%3D1bd94d24e672b720915458704aee92cb; cx_p_token=403097396f1bf921a104ac465c697240; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE4MTIyNzE0NjksImV4cCI6MTczMjQxNzA3MX0.YeO3oyePxWSU6fX2vajC-kN3SpW2vgUN5RJrjnPVqOg; xxtenc=21218285d5d4f3a17cb3c0511867d711; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731812271469; createSiteSource=num8; source=num8; wfwEnc=4E59B739D4AAA28FC8F126AEA9ACED4F; spaceFid=378; spaceRoleId=""; jrose=E9AA483D178B6126A739CFD892CB2204.mooc-444288205-mtj7s; videojs_id=3467620


```

```
POST https://mooc1.chaoxing.com/keeper/api/receive-studylog HTTP/1.1
Host: mooc1.chaoxing.com
Connection: keep-alive
Content-Length: 422
sec-ch-ua-platform: "Windows"
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
sec-ch-ua-mobile: ?0
Accept: */*
Origin: https://mooc1.chaoxing.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: k8s-ke=1731507985.656.11770.193232; jrose=B5C73E3A002455A2ADFCD8BAAF5F99F6.exam-keeper-4052863757-fkzz4; k8s=1731507984.504.11251.466485; route=c010ccedb771f8b7c7793c67ee1d2aae; writenote=yes; lv=3; fid=378; _uid=254538083; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6ac9d9a2f7a8a4d9933f4b9062323a079c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe33f68a3bfdd534836dec0d3b676e8e79; _d=1731812271468; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; vc2=1E20335C0E141E4951C658DE58D7A719; vc3=X%2FzVUiQmPP%2Fi3pjUkZJqnaAeyWFDgvay1nqcIS1QbIEje9M3ckAmpXTvVSLzDpG3%2B7GUeNSBMydJbhxBjBi3VCSgs9a6L1lFv2yEQTqQ%2FNWgaAOx9I9ScwdvdAdgpQeaboZnwF5Mv7bbk3C3uLSYjIw1OmZKP8GiU2JMy2qNhak%3D1bd94d24e672b720915458704aee92cb; cx_p_token=403097396f1bf921a104ac465c697240; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE4MTIyNzE0NjksImV4cCI6MTczMjQxNzA3MX0.YeO3oyePxWSU6fX2vajC-kN3SpW2vgUN5RJrjnPVqOg; xxtenc=21218285d5d4f3a17cb3c0511867d711; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731812271469; createSiteSource=num8; source=num8; wfwEnc=4E59B739D4AAA28FC8F126AEA9ACED4F; spaceFid=378; spaceRoleId=""; jrose=E9AA483D178B6126A739CFD892CB2204.mooc-444288205-mtj7s; videojs_id=3467620

log=%7B%22courseId%22%3A245055799%2C%22clazzId%22%3A104076320%2C%22personId%22%3A285104941%2C%22eventType%22%3A4%2C%22eventTime%22%3A1731824259356%2C%22data%22%3A%7B%22relationId%22%3A1802157384%2C%22objectId%22%3A%223090c9236e7c9161b718f5718edfef1d%22%2C%22userId%22%3A%22254538083%22%2C%22knowledgeId%22%3A888803600%2C%22fid%22%3A%22378%22%2C%22jobId%22%3A%22151989526627791%22%7D%7D&enc=db83d900fcf307b3e660a78f7ab096d7
```

```
GET https://detect.chaoxing.com/api/monitor?version=1731828748503&refer=http%3A%2F%2Fi.mooc.chaoxing.com&from=&fid=378&jsoncallback=jsonp07743548818385957&t=1731829110644 HTTP/1.1
Host: detect.chaoxing.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Accept: */*
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: script
Referer: https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=888803601&courseId=245055799&clazzid=104076320&cpi=285104941&enc=e619568b77200ae4e7cc053e489355ba&mooc2=1&openc=d4f870ff250a870e94459efb37476bfc
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: lv=3; fid=378; _uid=254538083; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb6ac9d9a2f7a8a4d9933f4b9062323a079c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fe33f68a3bfdd534836dec0d3b676e8e79; _d=1731812271468; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; vc2=1E20335C0E141E4951C658DE58D7A719; vc3=X%2FzVUiQmPP%2Fi3pjUkZJqnaAeyWFDgvay1nqcIS1QbIEje9M3ckAmpXTvVSLzDpG3%2B7GUeNSBMydJbhxBjBi3VCSgs9a6L1lFv2yEQTqQ%2FNWgaAOx9I9ScwdvdAdgpQeaboZnwF5Mv7bbk3C3uLSYjIw1OmZKP8GiU2JMy2qNhak%3D1bd94d24e672b720915458704aee92cb; cx_p_token=403097396f1bf921a104ac465c697240; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE4MTIyNzE0NjksImV4cCI6MTczMjQxNzA3MX0.YeO3oyePxWSU6fX2vajC-kN3SpW2vgUN5RJrjnPVqOg; xxtenc=21218285d5d4f3a17cb3c0511867d711; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731812271469; createSiteSource=num8; source=num8; wfwEnc=4E59B739D4AAA28FC8F126AEA9ACED4F; spaceFid=378; spaceRoleId=""; JSESSIONID=387B739597DBE23D9DD3697E0EDDCA4A


```

00172662592657451

08586026142154168

```
import requests

# URL 和查询参数
url = "https://mooc1.chaoxing.com/mooc-ans/multimedia/log/a/285104941/7cc9ac7a0e3cc6a85dbe8c037dca555d"
params = {
    "clazzId": "104076320",
    "playingTime": "7",
    "duration": "511",
    "clipTime": "0_511",
    "objectId": "4e16b4f74377b7612a3a72d0589ffc3b",
    "otherInfo": "nodeId_888803601-cpi_285104941-rt_d-ds_0-ff_1-be_0_0-vt_1-v_6-enc_b23b720612d0f078427387d62b7d068e",
    "courseId": "245055799",
    "jobid": "151997284121169",
    "userid": "254538083",
    "isdrag": "2",
    "view": "pc",
    "enc": "edd7ffd374a36489c72be03306a73d4a",
    "rt": "0.9",
    "videoFaceCaptureEnc": "6c31b1cf0cdff9c8513ea8e9923e320c",
    "dtype": "Video",
    "_t": "1731830002921",
    "attDuration": "511",
    "attDurationEnc": "c4490350b2ab819298a3336bdf2cc2d4"
}

# 请求头
headers = {
    "Host": "mooc1.chaoxing.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
    "Cookie": "k8s=1731507984.504.11251.466485; route=c010ccedb771f8b7c7793c67ee1d2aae; writenote=yes; jrose=6C73372E5B01FC574181B9C20EF627D7.mooc-444288205-mtj7s; lv=3; fid=378; _uid=254538083; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb60e921afc60c899369b0f8838e43b1493c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fef18cb3c07dbbb7f314d9cdcfc5aea689; _d=
```











```
GET https://mooc1.chaoxing.com/mooc-ans/multimedia/log/a/285104941/4f754d0465cf1ffd0661cfa42afe8e54?clazzId=104076320&playingTime=0&duration=1143&clipTime=0_1143&objectId=ea91fa51d6d0d9ae8d37c79feddc9fb9&otherInfo=nodeId_888803644-cpi_285104941-rt_d-ds_0-ff_1-be_0_0-vt_1-v_6-enc_29f76df4e27156987b8daa1dccec41c1&courseId=245055799&jobid=1522145068943392&userid=254538083&isdrag=3&view=pc&enc=686ec674e21398ca419c945f5bb3f9b0&rt=0.9&videoFaceCaptureEnc=bbdcd3b0750ca7dc330a0c1c2fb69e4b&dtype=Video&_t=1731836096484&attDuration=1143&attDurationEnc=c891c412273d015656e9c0583cd32c7c HTTP/1.1
Host: mooc1.chaoxing.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
Content-Type: application/json
sec-ch-ua-mobile: ?0
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1101-1842
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
Cookie: k8s=1731507984.504.11251.466485; route=c010ccedb771f8b7c7793c67ee1d2aae; writenote=yes; jrose=6C73372E5B01FC574181B9C20EF627D7.mooc-444288205-mtj7s; lv=3; fid=378; _uid=254538083; uf=94ffe74515793f361e49d59a8d4dc2d6502f9b58d6ec7cb5c4c00161c44cceb60e921afc60c899369b0f8838e43b1493c49d67c0c30ca5047c5a963e85f110998c56b3d3d9060899ce71fc6e59483dd3befdf0dd3f82f3fef18cb3c07dbbb7f314d9cdcfc5aea689; _d=1731829920409; UID=254538083; vc=95EFCA782B78211657973AE5692F481F; vc2=1E20335C0E141E4951C658DE58D7A719; vc3=Dw%2FmdUM9J%2BmQAmgZkVeUhpcsqcYlzT2%2BY2b7chuibjbKX4pHoJ3AsB3yos877suqHbq3CyggG9n19S8EExF3m6lfGPqzg3HH5Ps2XQxiPv4opgekGp733sL1vG8Dl725o8L3p%2Fvc1%2F1MLM52tCTAV5IMSHmSlOms4o1M7TEqbws%3D9d4ebcb2a96330d30f9b22d6ffab1c4e; cx_p_token=fd95d0687421d1c87e36ae0ae317a6be; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTQ1MzgwODMiLCJsb2dpblRpbWUiOjE3MzE4Mjk5MjA0MTAsImV4cCI6MTczMjQzNDcyMH0.tqyPvuYrZSj5yyAPMVtEMKO3OphHEs9ZkyaPRXZ3dLo; xxtenc=21218285d5d4f3a17cb3c0511867d711; DSSTASH_LOG=C_38-UN_164-US_254538083-T_1731829920411; spaceFid=378; spaceRoleId=""; videojs_id=7923664

```

##### 9、js逆向（苦痛之路）

```
object{
    "resourceID": "8d128ee00fa7b354857c8652f6dedced",
    "resourceType": "doc",
    "from": 4,
    "passportUID": "254538083",
    "t": "20241119115046",
    "location": 1,
    "curPage": 1,
    "totalPage": 1,
    "ext": "{\"_from_\":\"245055799_104076320_254538083_e619568b77200ae4e7cc053e489355ba\"}",
    "token": "6602ee604b5eb6cc5d265a5a3f0b681b"
}

_0x50a15c['hXPhh'](a,b) = (a+b)  
function2(a,b) {a(b)}

function1:
t = 20241119115046
function1 setTime(t) {
        t = t + '';
        var time = new Date();
        time['setFullYear'](parseInt(t["substring"](0x0, 0x4)))
        time[‘setMonth'](parseInt(t["substring"](0x4, 0x6))-0x1)
        time['setDate'](parseInt(t["substring"](0x6, 0x8)))
        time['setHours'](parseInt(t["substring"](0x8, 0xa)))
        time['setMinutes'](parseInt(t["substring"](0xa, 0xc)))
        time['setSeconds'](parseInt(t["substring"](0xc, 0xe)))
        return Math['abs'](new Date()['getTime']() - time['getTime']()) <=  0x5*0x3c*0x3c * 0x3e8;
    }

对obejct对象生成一个包含了键的数组array，除了token
array['sort']()，按照字母顺序排序了一遍键名

ori = ""
for(var i=0;i<array['length'];i++){
	ori+= object[array[i]]
}

字符串ori就会包括除了token之外的所有object中的值

ori + "uWrVfLhv#1TW!@QA" (难道是随机的吗)

先encode再unescape，什么用都没有

unescape(encodeURIComponent(ori))

array1[ori['length'] >> 0x2 - 0x1] = undefined (length:38)

num = ori['length']*0x8
for(var i=0;i<num;i+=0x8){
array1[i >> 0x5] |= (ori['charCodeAt'] (i/0x8) & 0xff) << (i%0x20);
}

返回计算出的array1

输入参数为array1和num=ori.length*0x8

array1[num >> 5] |=  0x80 << (num%0x20)
array1[( ( ( num + 0x40) >>> 0x9) << 0x4) + 0xe] = num;

 for (i = 0x0; i< array1.lentgth; i += 0x10)
 
 _0x37b23e = _0x75c801(1732584193, -271733879, -1732584194, 271733878, array1[i], 0x7, -680876936)
 
 _0x75c801:
 ret _0x28fa76( ( (271733878 & -1732584194) | ~(-271733879) & 271733878), 1732584193,-271733879, array1[i], 0x7, -680876936)
 
 _0x28fa76:
 
 
 
 case 4: _0x561ff8
 
 case 6:
 _0x34a2dc =  document['body']['innerText']['trim']()['length']


 var senddata = {
            'r': _0x49e03f['resourceID'],
            't': _0x49e03f['resourceType'],
            'l': _0x49e03f['location'] || 0x1,
            'f': _0x49e03f['from'] || 0x0,
            'p': _0x49e03f['curPage'],
            'tp': _0x49e03f['totalPage'],
            'wc': _0x49e03f['wordCount'] || _0x34a2dc(131),
            'ic': _0x49e03f['imgCount'] || _0x561ff8(47),
            'v': 0x2,
            's': 1(固定值吧，传入的参数),
            'h': _0x3cabab()函数返回值
        };
        
{"resourceID":"8d128ee00fa7b354857c8652f6dedced","resourceType":"doc","from":4,"passportUID":"254538083","t":"20241119172815","location":1,"curPage":1,"totalPage":1,"ext":"{\"_from_\":\"245055799_104076320_254538083_e619568b77200ae4e7cc053e489355ba\"}","token":"68f8a356d96b4077ee3e3ad6f3a3cdd6"}




enc计算
salt:NrRzLDpWB2JkeodIVAn4

ori = d+f+t+u+salt
array1[ori['length'] >> 0x2 - 0x1] = undefined (length:96)
num = ori['length']*0x8
for(var i=0;i<num;i+=0x8){
array1[i >> 0x5] |= (ori['charCodeAt'] (i/0x8) & 0xff) << (i%0x20);
}

40a987adca78cbe83293136f53fb1ddb

_0x5475c0(array1, ori.length * 0x8)
array1[num >> 5] |=  0x80 << (num%0x20)
array1[( ( ( num + 0x40) >>> 0x9) << 0x4) + 0xe] = num;

()(_0x617e8c,()(_0x204160,   
(
_0x617e8c(  _0x617e8c(_0x237a2f, _0x2fa589), _0x617e8c(_0x2ce627, _0x179943)   )     

, _0x1c2624), _0x46d43a);

for (i = 0x0; i< array1.lentgth; i += 0x10)


+  ( + ( >> (_0x4eb3cd, 0x10),  >> (_0x1e99e4, 0x10)), _0x5306aa >> 0x10)

(_0x474951<<_0x51070f)  |  _0x474951 >>> 0x20 - _0x51070f

()(_0x75c801, _0x52e7b2, _0x27f070, _0x37b23e, _0x129cea, _0x218143[_0x20aa22[_0x47c9('0x1c5', 'eAXx')](_0x364794, 0x2)], 0x11, 0x242070db)


wc通过document['body']['innerText']['trim']()['length']得到
ic通过document['getElementsByTagName']('img')['length']得到

-441671929，-1414224366，253055854，-1340170955
```

```
1178302983
-1526007338
-1723893899
-588633733
1725569806
-536520004
-1642772942
-456060027
-1200963872

```

```
receive_studylog需要一个referer才能确定Logid，
```

