from base64 import decode
import requests as rqs
import json
import requests
from requests.structures import CaseInsensitiveDict


def decode(msg):
    text = msg
    list = text.split("-")
    pr = ""
    for n in list :
        if n == "z1":
            pr += "ض"

        if n == "s1":
            pr += "ص"

        if n == "s2":
            pr += "ث"

        if n == "gh1":
            pr += "ق"

        if n == "f1":
            pr += "ف"

        if n == "gh2":
            pr += "غ"

        if n == "a1":
            pr += "ع"

        if n == "h1":
            pr += "ه"

        if n == "kh1":
            pr += "خ"

        if n == "h2":
            pr += "ح"

        if n == "j1":
            pr += "ج"

        if n == "ch1":
            pr += "چ"

        if n == "sh1":
            pr += "ش"

        if n == "s3":
            pr += "س"

        if n == "e1":
            pr += "ی"

        if n == "b1":
            pr += "ب"

        if n == "l1":
            pr += "ل"

        if n == "a2":
            pr += "ا"

        if n == "t1":
            pr += "ت"

        if n == "n1":
            pr += "ن"

        if n == "m1":
            pr += "م"

        if n == "z2":
            pr += "ظ"

        if n == "gh3":
            pr += "گ"

        if n == "k1":
            pr += "ک"

        if n == "t2":
            pr += "ط"

        if n == "z3":
            pr += "ز"

        if n == "r":
            pr += "ر"

        if n == "t3":
            pr += "ذ"

        if n == "d1":
            pr += "د"

        if n == "v1":
            pr += "و"

        if n == "space":
            pr += " "

        if n == "p":
            pr += "پ"

        if n == "<TX>":
            pr += "<TX>"

        if n == "<NX>":
            pr += "<NX>"

        if n == "shch":
            pr += "ژ"

    return pr


class server:

    
    def decode(msg):
        text = msg
        list = text.split("-")
        list.remove("")
        pr = ""
        for n in list :
            if n == "z1":
                pr += "ض"

            if n == "s1":
                pr += "ص"

            if n == "s2":
                pr += "ث"

            if n == "gh1":
                pr += "ق"

            if n == "f1":
                pr += "ف"

            if n == "gh2":
                pr += "غ"

            if n == "a1":
                pr += "ع"

            if n == "h1":
                pr += "ه"

            if n == "kh1":
                pr += "خ"

            if n == "h2":
                pr += "ح"

            if n == "j1":
                pr += "ج"

            if n == "ch1":
                pr += "چ"

            if n == "sh1":
                pr += "ش"

            if n == "s3":
                pr += "س"

            if n == "e1":
                pr += "ی"

            if n == "b1":
                pr += "ب"

            if n == "l1":
                pr += "ل"

            if n == "a2":
                pr += "ا"

            if n == "t1":
                pr += "ت"

            if n == "n1":
                pr += "ن"

            if n == "m1":
                pr += "م"

            if n == "z2":
                pr += "ظ"

            if n == "gh3":
                pr += "گ"

            if n == "k1":
                pr += "ک"

            if n == "t2":
                pr += "ط"

            if n == "z3":
                pr += "ز"

            if n == "r":
                pr += "ر"

            if n == "t3":
                pr += "ذ"

            if n == "d1":
                pr += "د"

            if n == "v1":
                pr += "و"

            if n == "space":
                pr += " "

            if n == "p":
                pr += "پ"

            if n == "<TX>":
                pr += "<TX>"

            if n == "\n":
                pr += "=n"

        return pr

    def get_home_data(version):
        try:

            url = "https://uupload.ir/linkbuild.php"

            headers = CaseInsensitiveDict()
            headers["Host"] = "uupload.ir"
            headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"
            headers["Accept"] = "text/html, */*; q=0.01"
            headers["Accept-Language"] = "en-US,en;q=0.5"
            headers["Accept-Encoding"] = "gzip, deflate"
            headers["Referer"] = f"https://uupload.ir/view/{version}_uvvu.txt/"
            headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
            headers["X-Requested-With"] = "XMLHttpRequest"
            headers["Content-Length"] = "26"
            headers["Origin"] = "https://uupload.ir"
            headers["Alt-Used"] = "uupload.ir"
            headers["Connection"] = "keep-alive"
            headers["Cookie"] = "_ga=GA1.2.856156775.1642632472; _gid=GA1.2.1680185114.1642632472; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_session_token=8de57fcc-0fc1-8af4-9495-0b4433d7acac; analytics_token=7bfaff97-a059-976b-94e4-2b37d1f6d12a; yektanet_session_last_activity=1/20/2022; _yngt_iframe=1; _yngt_match={%22sabavision%22:1}; _yngt=b522fe6f-cbad-4d79-b539-53c2a1f648e7; _gat_gtag_UA_25986871_2=1"
            headers["Sec-Fetch-Dest"] = "empty"
            headers["Sec-Fetch-Mode"] = "no-cors"
            headers["Sec-Fetch-Site"] = "same-origin"
            headers["TE"] = "trailers"
            headers["Pragma"] = "no-cache"
            headers["Cache-Control"] = "no-cache"

            data = f"filename={version}_uvvu.txt"


            resp = requests.post(url, headers=headers, data=data)

            file_Url_server = resp.text.split("value")[1].split('"')[1]

            url = file_Url_server
            r = requests.get(url, allow_redirects=True)
            

            rqs_json = decode(r.text)
            res = rqs_json.split("<NX>")

            return res
        except:
            pass


    def get_info_data(version):
        pass

