from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

html = urlopen("https://dhlottery.co.kr/gameResult.do?method=statByNumber")
bsObject = BeautifulSoup(html, "html.parser")

theory_rate = 7/45 # 이론상 숫자가 나올 확률
current_round = int(bsObject.body.find("select",{"id":"edDrwNo"}).find("option",{"selected":""}).text) # 총 시행횟수 (최신 회차)
theory_pop_count = int(current_round * theory_rate) # 이론상 숫자가 나와야 하는 횟수

data = bsObject.body.find_all("tbody")[-1].text.split()
Pop_count = {} # 실제 숫자가 나온 횟수를 담을 딕셔너리
num = 1

for i in range(2,len(data),3):
    Pop_count[ num ] = int(data[i])
    num += 1

sorted_Pop = sorted(Pop_count.items(),key=(lambda x:x[1]), reverse=True)

most_high = sorted_Pop[:6]
most_low = sorted_Pop[-6:]
middle = sorted_Pop[ (int(len(sorted_Pop)/2)) - 3 : (int(len(sorted_Pop)/2)) + 3 ]

print("most high :", most_high)
print("most low :", most_low)

random_seq = most_high + most_low
random.shuffle(random_seq)

random_seq = random_seq[:6]
random_seq.sort()

print("shuffled :", random_seq)