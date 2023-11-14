#!/usr/bin/env python
# coding: utf-8

# In[13]:

#클래스 생성
class Subject:
    def __init__ (self, name = '', kog = 0, math = 0, eng = 0): #클래스의 name, kog, math, eng 를 붙여주는 함수 생성
        self.name = name
        self.kog = float(kog)
        self.math = float(math)
        self.eng = float(eng)
    
    def getAvearage(self): #평균을 구하는 함수
        avearage = (self.kog + self.math + self.eng) / 3 #국어 영어 수학 평균을 구함
        print(f"{self.name}의 평균점수는 {avearage:.2f}") #사용자에게 평균점수를 출력


#파일을 읽어오고 딕셔너리화 하는 함수
def loadData(filename): 
    student_scores = [] #점수를 넣어놓을 리스트 생성
    lines = open(filename, "r", encoding = "utf8").readlines() #파일을 읽은 후 리스트에 저장
    for line in lines[1:]: #헤더 {이름, 국어, 수학, 영어} 를 제외한 데이터부터 처리
        tokens = line.replace('\n', '').split(",") #딘어 쪼개는 변수
        std_class = Subject(tokens[0], tokens[1], tokens[2], tokens[3]) #클래스를 불러온 후 tokens별 위치에 과목 저장
        student_scores.append(std_class)
    return student_scores 

print("-----학생들의 평균 점수-----")
filename = "students.csv" #파일 이름 불러오기
students = loadData(filename) #loadData 함수를 통해 파일 불러오기

for student in students: #조건문을 통해 학생별 평균을 구함!
    student.getAvearage()