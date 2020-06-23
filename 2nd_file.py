# a = int(input("숫자를 입력하세용용용"))
# if(a<0):
#     print("정수정수입력행");
# elif(a==5):
#     print("a는 ",a,"입니당.")
# else:
#     print("너무크다아앙ㅇ")

# if(a%2==0):
#     print(a,"짝")
# else:
#     print(a,"홀")

# def mysum(a,b):
#     c=a+b;
#     return c;
# def myminus(a,b):
#     d=a-b;
#     return d;

# a=int(input("a"))
# b=int(input("b"))

# print(mysum(a,b))
# print(myminus(a,b))

class NS5: #class 공통 변수
    body="강화합금"
    def run(self): #class 탄생하는 객체가 가지는 공통 기능
            print("나는 달립니다.")
    
NS5_1=NS5()
NS5_2=NS5()
print(NS5_1.body)
NS5_2.run()
NS5_2.sense="happy"
print(NS5_2.sense)