{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "2ef46c94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-----학생들의 평균 점수-----\n",
      "실바의 평균 점수는 73.67입니다.\n",
      "산토스의 평균 점수는 86.93입니다.\n",
      "맥그리거의 평균 점수는 85.70입니다.\n",
      "알도의 평균 점수는 85.43입니다.\n",
      "로우지의 평균 점수는 83.10입니다.\n",
      "누네스의 평균 점수는 85.93입니다.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "filename = \"students.csv\"\n",
    "\n",
    "#파일을 읽어오고 딕셔너리화 하는 함수\n",
    "def loadData(filename): \n",
    "    student_scores = {} \n",
    "    lines = open(filename, \"r\", encoding = \"utf8\").readlines() #파일을 읽은 후 리스트에 저장\n",
    "    for line in lines[1:]: #헤더 {이름, 국어, 수학, 영어} 를 제외한 데이터부터 처리\n",
    "        elements = line.split(',') # 받은 줄을 쉼표로 구부해서 리스트에 저장\n",
    "        name = elements[0] # 학생 이름은 각각 의 줄의 첫 번째 요소\n",
    "        scores = [] #각 학생의 성적을 담을 빈 리스트를 생성\n",
    "        for element in elements[1:]: #학생의 성적을 처리하는 조건문\n",
    "            scores.append(float(element)) #문자열 --> 실수로 변환하여 리스트에 추가\n",
    "            student_scores[name] = scores #학생이름 :key 성적리스트 : value 로 딕셔너리에 저장\n",
    "    return student_scores \n",
    "\n",
    "#성적의 평균을 구하는 함수\n",
    "def getAvearage (Avgdic):\n",
    "    for name, scores in Avgdic.items(): #dic에서 학생 이름과 성적 리스트를 가져옴\n",
    "        total = sum(scores) #성적 리스트의 총합 계산\n",
    "        average = total / len(scores) #socre의 길이를 통해 total의 평균을 계산\n",
    "        print(f\"{name}의 평균 점수는 {average:.2f}입니다.\")\n",
    "    return 0;\n",
    " \n",
    "    \n",
    "print(\"-----학생들의 평균 점수-----\")\n",
    "#각 함수들을 호출\n",
    "student_dic = loadData(filename)\n",
    "getAvearage(student_dic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a9eb735",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fe6f022",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
