input_id = input("아이디를 입력해주세요.\n")
input_pwd = input("비밀번호를 입력해주세요.\n")
real_id = "geeneve"
real_pwd = "dlehdrms"

if real_id == input_id:
    if real_pwd == input_pwd:
        print("Hello!")
    else:
        print("잘못된 비밀번호 입니다.")
else:
    print("사용자 정보가 없습니다.")
