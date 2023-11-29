user = input("이름을 입력하세요.")
pw = input("비밀번호를 입력하세요.")

f = open("./member.txt", "r")
flag =0
while f:
    data = f.readline()
    if flag == 0 and data.find(user) != -1:
        flag = 1
    if flag == 1 and data.find(pw) != -1:
        flag = 2
        break
    if data == " " :
        break

f.close()
if flag == 2 :
    print("로그인 성공")
else : print("로그인 실패")