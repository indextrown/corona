import requests
import bs4

from bs4 import BeautifulSoup

 

response = requests.get("http://xn--19-q81ii1knc140d892b.kr/main/main.do")

soup = BeautifulSoup(response.text, 'lxml')



현재시간 = soup.select("div.top_area > p.exp")[0].text.replace('\t', '').replace('\r', '').replace('\n', '')
입원중 = soup.select("div.situation1_1 p")[1].text.replace('\n', '')
완치 = soup.select("div.situation1_1 p")[2].text.replace('\n', '')
사망자 = soup.select("div.situation1_1 p")[3].text.replace('\n', '')
계 = soup.select("div.situation1_1 p")[4].text.replace('\n', '')

for i in twoStep:
    날짜.append(i.select('td[align="center"] > span')[0].text)
    종가.append(int(i.select('td.num > span')[0].text.replace(',', '')))
    전일비.append(int(i.select('td.num > span.tah.p11')[1].text.strip().replace(',', '')))
    거래량.append(int(i.select('td.num > span')[5].text.replace(',', '')))

l = []

for i in range(len(날짜)):
    l.append({
        '날짜':날짜[i],
        '종가':종가[i],
        '전일비':전일비[i],
        '거래량':거래량[i],

    })
    
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
final_data = f"var 현재시간 = '{시가총액}';\n\
final_data = f"var 입원중 = '{시가총액}';\n\
final_data = f"var 완치 = '{시가총액}';\n\
final_data = f"var 사망자 = '{시가총액}';\n\
final_data = f"var 계 = '{시가총액}';\n\
" + final_data
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    f_write.write(final_data) 
