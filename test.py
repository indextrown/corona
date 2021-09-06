import requests
import bs4

from bs4 import BeautifulSoup

 
url = "https://www.jinju.go.kr/05190/05641.web"
response = requests.get(url, verify = False)
soup = BeautifulSoup(response.text, 'lxml')







진주날짜 = soup1.select("div.hg1 > p")[0].text
진주계 = soup1.select("span.num2")[0].text
진주완치 = soup1.select("span.num1")[0].text
진주입원중 = soup1.select("span.num1")[1].text
진주사망자 = soup1.select("span.num1")[2].text
진주검사중 = soup1.select("span.num1.ls3")[0].text
진주검사결과 = soup1.select("span.num1.ls3")[1].text
진주자가격리자 = soup1.select("span.num11")[0].text
진주거리두기단계 = soup1.select("div#notice1 > ul > li")[0].text


l = []
##파일을 쓴다
import csv
import json

with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    json.dump(l, f_write, ensure_ascii=False, indent=4)
##파일을 다시 읽는다
data = ""
with open('data.js', "r", encoding="UTF-8-sig") as f:
    line = f.readline()
    while line:
        data += line
        line = f.readline()
#파일에 변수명을 추가하여 다시 쓴다.
final_data = f"var data = {data};"
final_data = f"var 진주날짜 = '{진주날짜}';\n\
var 계 = '{진주계}';\n\
var 완치 = '{진주완치}';\n\
var 입원중 = '{진주입원중}';\n\
var 사망자 = '{진주사망자}';\n\
var 검사중 = '{진주검사중}';\n\
var 검사결과 = '{진주검사결과}';\n\
var 자가격리자 = '{진주자가격리자}';\n\
var 거리두기단계 = '{진주거리두기단계}';\n\
" + final_data
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    f_write.write(final_data) 
