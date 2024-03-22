import requests
import json

number = input(' number : ')
url = 'https://www.instagram.com/api/v1/web/accounts/check_phone_number/'

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Length": "30",
    "Content-Type": "application/x-www-form-urlencoded",
#    "Cookie": "ig_did=5015468C-1CDE-4FDD-A8AF-80E4A2CBBF74; ig_nrcb=1; dpr=1.8937500715255737; mid=ZfQOpgABAAEoKoMH7DzD-tuqxh_9; ps_l=0; ps_n=0; datr=pg70ZR6plDXUrLePg-G-1Jtn; shbid=\"19962\\05440419872563\\0541742288659:01f786a32f0ea122de2c11bd0062696ed8713414c4957b8bf4d16b1379534089ec65add5\"; shbts=\"1710752659\\05440419872563\\0541742288659:01f7a5c64027b6c1d7f7ab99df74f9775b90692054df7296a4fa356c5340ff565bea26e6\"; rur=\"LDC\\05440419872563\\0541742288659:01f75eae521c8b8f2fc8e8d70d458e190d6ba58030b9efc871e4ddad4a630cd0db1ccbd0\"; csrftoken=ZbAcfZNV3SzYBNQOzbNgnWME9zGRGjJh",
    "Dpr": "1.89375",
    "Origin": "https://www.instagram.com",
    "Referer": "https://www.instagram.com/accounts/signup/phone/",
    "Sec-Ch-Prefers-Color-Scheme": "dark",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
    "Sec-Ch-Ua-Full-Version-List": "\"Not_A Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"120.0.6099.116\"",
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Model": "\"Infinix X6816\"",
    "Sec-Ch-Ua-Platform": "\"Android\"",
    "Sec-Ch-Ua-Platform-Version": "\"11.0.0\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Viewport-Width": "381",
    "X-Asbd-Id": "129477",
    "X-Csrftoken": "ZbAcfZNV3SzYBNQOzbNgnWME9zGRGjJh",
    "X-Ig-App-Id": "1217981644879628",
    "X-Ig-Www-Claim": "hmac.AR11Lp1WxYoSiDmrZwVbH1NbCVp5_8SIwKCqC8oS6hMejoXy",
    "X-Instagram-Ajax": "1012117012",
    "X-Requested-With": "XMLHttpRequest"
}

data = {
    'phone_number': number,
}
re = requests.post(url, headers=headers, data=data).text
re_json = json.loads(re)
if 'status' in re_json and re_json['status'] == 'ok': 
    print('Good')
else:
    print('Error')