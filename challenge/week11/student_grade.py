#!/usr/bin/env python
# coding: utf-8

# In[13]:
#파일을 읽어오는 모듈파일
import student

#파일을 읽어오고 딕셔너리화 하는 함수
def loadData(filename): 
    student_scores = [] #점수를 넣어놓을 리스트 생성
    lines = open(filename, "r", encoding = "utf8").readlines() #파일을 읽은 후 리스트에 저장
    for line in lines[1:]: #헤더 {이름, 국어, 수학, 영어} 를 제외한 데이터부터 처리
        tokens = line.replace('\n', '').split(",") #딘어 쪼개는 변수
        std_class = Student.Subject(tokens[0], tokens[1], tokens[2], tokens[3]) #클래스를 불러온 후 tokens별 위치에 과목 저장
        student_scores.append(std_class)
    return student_scores 
