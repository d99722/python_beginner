puts("아이디를 입력해주세요\n")
input = gets.chomp()
real_egoing = "11"
real_dongroot = "ab"


if real_egoing == input
  puts("hello, egoing!")
elsif real_dongroot == input
  puts("hello, dongroot!")
else
  puts("침입자다!")
end
