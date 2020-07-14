#-*-coding=utf-8-*-
print("python's favorite food is perl")
print('"python is very easy."he says')

multiline1 = "Life is too short\nYou need python"
multiline2 = '''
life is too short
you need python
'''
print(multiline1)
print(multiline2)

#문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head+tail)

#문자열 곱하기
a="python "
print(a*4)
print("="*50)
print("My program")
print("="*50)

a="Life is too short, You need Python"
print(a[3])
print(a[0:4])
print(a[9:11])

#슬라이싱 활용
a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]

"I eat %d apples." % 3 #숫자 바로 대입
"I eat %s apples." % "five" #문자 바로 대입
number=3
"I eat %d apples." % number #숫자변수 대입
number=10
day="three"
"I ate %d apples. for %s days" % (number,day) #두개 이상의 값 넣기

"%10s" % "hi" #10길이 문자열 오른쪽정렬
"%-10sjane" % "hi" #10길이 문자열 왼쪽정렬

"%0.4f" % 3.42134234 #소수점 4자리까지 표시
"%10.4f" % 3.42134234 #소수점 4자리 + 10길이문자열 오른쪽 정렬

#문자갯수세기
a='hobby'
a.count('b') #2

#위치 알려주기
a.find('b') #가장 처음 등장한 위치... 등장 안했으면 -1 리턴)

#위치 알려주기2
a.index('b') #위와 같으나 등장 안할 시 오류

#문자열 삽입
a=","
a.join('abcd') #abcd문자열 사이에 변수 a = , 삽입

#소문자를 대문자로
a="hi"
a.upper()
a.lower()소문자로

#공백지우기
a="      hi     "
a.lstrip() #왼쪽 (연속된) 공백
a.rstrip() #오른쪽 (연속된) 공백
a.strip() #양쪽 공백

#문자열 바꾸기
a = "Life is too short"
a.replace("Life","your leg") #Your leg is too short

#문자열 나누기
a="Life is too short"
a.split() #공백을 기준으로 문자열 나눔 > ['Life','is',...]
a='a:b:c:d'
a.split(:) #:를 기준으로 문자열 나눔 > ['a','b',...]

#숫자 바로 대입
"I eat {0} apples.".format(3)

#문자열 바로 대입
"I eat {0} apples".format("five")

#숫자값을 가진 변수로 대입
number=3
"I eat {0} apples".format(number)

#2개 이상의 값 넣기
number=10
day="three"
"I ate {0} apples, {1}days".format(number, day)

#이름으로 넣기
"I ate {number} apples, {day}days".format(number=10, day=3)

#인덱스와 이름 혼용
"I ate {0} apples, {day}days".format(10, day=3)

#정렬 (화살표 방향 생각)
"{0:<10}".format("hi") #왼쪽정렬
"{0:>10}".format("hi") #오른쪽정렬
"{0:^10}".format("hi") #가운데정렬

#공백채우기
"{0:=^10}".format("hi") #====hi==== 가운데 정률 후 채우기
"{0:!<10}".format("hi") #hi!!!!!!! 왼쪽 정렬 후 채우기

#소수점 표현하기
y=3.4234123
"{0:0.4f}".format(y) #4자리까지
"{0:10.4f}".format(y) #10칸,우측정렬 4자리

#{, } 표현하기
"{{and}}".format() # '{and}' 2개연속 사용
