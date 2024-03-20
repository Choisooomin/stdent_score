def calculate_total(scores):        # 총점을 계산하는 함수
  return sum(scores)

def calculate_average(scores):      # 평균을 계산하는 함수
  return sum(scores) / len(scores)

def calculate_grade(scores):        # 학점을 계산하는 함수
  ave = sum(scores) / len(scores) # 평균 점수 계산
  if ave >= 90:
      return "A"
  elif ave >= 80:
      return "B"
  elif ave >= 70:
      return "C"
  elif ave >= 60:
      return "D"
  else:
      return "F"

def calculate_rank(students):
  students.sort(key=lambda x: calculate_average(x['scores']), reverse=True)
  # 등수를 계산하여 각 학생에게 할당
  for i, student in enumerate(students):
      student['average_rank'] = i + 1
  return students

students = [] # 학생 정보를 저장하기 위한 students 리스트
for i in range(5): # 학생이 5명이기에 5번 반복
  name = input(f"학생 {i+1}의 이름을 입력하세요: ")
  scores = []
  for subject in ['영어', 'C언어', '파이썬']: # 3과목을 입력하기 위해 반복
      score = float(input(f"{name} 학생의 {subject} 점수를 입력하세요: "))
      scores.append(score)
  students.append({'name': name, 'scores': scores}) # 학생의 이름과 과목점수 기록하기 위해 저장
  print()

# 등수 계산
students_with_rank = calculate_rank(students)

for student in students_with_rank: # 학생 정보 출력하기
  total_score = calculate_total(student['scores'])
  average_score = calculate_average(student['scores'])
  grade = calculate_grade(student['scores'])
  rank = student['average_rank']  # 등수 정보를 가져옴
  print(f"{student['name']} 학생의 총점 {total_score}, 평균 {average_score:.2f}, 학점 {grade}, 등수 {rank}입니다.")