puts("아이디를 입력해주세요. \n")
input_id = gets.chomp()

members = ['egoing','dgboy','gang']
for member in members do
    if member == input_id
        puts('Hello!, '+member)
        exit
    end
end
puts('who are you')
