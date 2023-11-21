#모듈화 시킨 파일 불러오기
import student_grade 
import student

print("-----학생들의 평균 점수-----")
filename = "students.csv" #파일 이름 불러오기
students = student_grade.loadData(filename) #loadData 함수를 통해 파일 불러오기


for student in students: #조건문을 통해 학생별 평균을 구함!
    student.getAvearage() #Student 파일의 getAverage 함수 사용