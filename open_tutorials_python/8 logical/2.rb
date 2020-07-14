puts("아이디를 입력해주세요.\n")
input_id = gets.chomp()
puts("비밀번호를 입력해주세요.\n")
input_pwd = gets.chomp()
real_id = "geeneve"
real_pwd = "dlehdrms"

if real_id == input_id
  if real_pwd == input_pwd
    puts("Hello!")
  else
    puts("잘못된 비밀번호 입니다.")
  end
else
  puts("사용자 정보가 없습니다.")
end
