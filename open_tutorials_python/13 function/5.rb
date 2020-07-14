puts("아이디를 입력해주세요. \n")
input_id = gets.chomp()

def login(_id)
  members = ['egoing','dgboy','gang']
  for member in members do
      if member == _id
          return true
      end
  end
  return false
end

if login(input_id)
  puts('Hello!, '+input_id)
else
  puts('Who shot ya?')
end
