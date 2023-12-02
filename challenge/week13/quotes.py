import re
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

wordlst = [] #단어를 모두 저장 할 리스트
word_dict = dict() #단어 빈도 수 저장 딕셔너리

url = 'https://quotes.toscrape.com/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
quotes = soup.find_all('div', {"class": "quote"})

#웹 크롤링
for quote in quotes:
    quote_texts = quote.find_all('span', {"class": "text"})
    for quote_text in quote_texts:
        words = re.findall(r'\b\w+\b', quote_text.text.lower())
        wordlst.extend(words)

#단어 빈도수 계산 2
for word in wordlst: #wordlst 에서  단어 하나씩 꺼냄
    word = word.lower() #소문자로 정리
    if word not in word_dict: #word 가 딕셔너리에 없는 경우 딕셔너리 추가
        word_dict[word] = 1
    else: #word 가 딕셔너리게 있는 경우 빈도 올림
        word_dict[word] += 1

count = 1 #랭킹을 셀 변수 생성
for word in sorted(word_dict, key = word_dict.get, reverse = True): #word딕셔너리에서 단어 순위 정렬렬
    print(f"{word} : {word_dict[word]}회")
    count += 1 #1위부터 순위 올림
    if count > 5: #5위까지 추출
        break



