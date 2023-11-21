#이름과 과목별로 나누어주는 모듈 파일
class Subject:
    def __init__ (self, name = '', kog = 0, math = 0, eng = 0): #클래스의 name, kog, math, eng 를 붙여주는 함수 생성
        self.name = name
        self.kog = float(kog)
        self.math = float(math)
        self.eng = float(eng)
    
    def getAvearage(self): #평균을 구하는 함수
        avearage = (self.kog + self.math + self.eng) / 3 #국어 영어 수학 평균을 구함
        print(f"{self.name}의 평균점수는 {avearage:.2f}") #사용자에게 평균점수를 출력
