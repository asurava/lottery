from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

html = urlopen("https://www.dhlottery.co.kr/gameResult.do?method=index720")
bsObject = BeautifulSoup(html, "html.parser")

current_round = int(bsObject.body.find("select",{"id":"edDrwNo"}).find("option",{"selected":""}).text) # 총 시행횟수 (최신 회차)

print("current_round : ", current_round)

data = []

for i in range(2,8,1):#웹페이지 상에서 2 = 십만단위 / 3 = 만단위 / 4 = 천단위 / 5 = 백단위 / 6 = 십단위 / 7 = 일단위

    tmp_data = bsObject.body.find_all("tbody")[i].text.split()

    for item in tmp_data: # 웹페이지에서 그래프 그려주는 % element 제거하고, 숫자랑 각 숫자가 몇 번 나왔는지만 남겨놓기
        if "%" in item:
            tmp_data.pop(tmp_data.index(item))

    tmp_dic = {}
    for j in range(0,len(tmp_data),2): # dictionary로 변환
        tmp_dic[tmp_data[j]]=tmp_data[j+1]

    sorted_list = sorted(tmp_dic.items(),key=(lambda x:x[1]), reverse=True) # desc 정렬

    data.append(sorted_list) # index 0 ~ 5 = 십만단위 ~ 일단위

    print(i-2," : ",sorted_list) # index 0 ~ 5 = 십만단위 ~ 일단위

most_high = []
most_low = []

for items in data:

    most_high.append(items[0])
    most_low.append(items[-1])

print("most high :", most_high)
print("most low :", most_low)