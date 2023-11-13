#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Subject:
    def __init__ (self, name = '', kog = 0, math = 0, eng = 0):
        self.name = name
        self.kog = float(kog)
        self.math = float(math)
        self.eng = float(eng)
    
    def getAvearage(self):
        avearage = (self.kog + self.math + self.eng) / 3
        print(f"{self.name}의 평균점수는 {avearage:.2f}")


#파일을 읽어오고 딕셔너리화 하는 함수
def loadData(filename): 
    student_scores = []
    lines = open(filename, "r", encoding = "utf8").readlines() #파일을 읽은 후 리스트에 저장
    for line in lines[1:]: #헤더 {이름, 국어, 수학, 영어} 를 제외한 데이터부터 처리
        tokens = line.replace('\n', '').split(",")
        std_class = Subject(tokens[0], tokens[1], tokens[2], tokens[3])
        student_scores.append(std_class)
    return student_scores 

print("-----학생들의 평균 점수-----")
filename = "students.csv"
students = loadData(filename)

for student in students:
    student.getAvearage()


# In[ ]:





# In[ ]:




