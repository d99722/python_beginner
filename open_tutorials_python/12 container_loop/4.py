input_id = input("아이디를 입력해주세요.\n")
# real_egoing = "egoing"
# real_dgboy = "dgboy"
members = ['egoing','dgboy','gang']
# if real_egoing == in_str:
#   print("hello, egoing!")
# elif real_dgboy == in_str:
#   print("Good morning, Sir!")
# else:
#   print("Who shat ya!")
for member in members:
    if member == input_id:
        print('Hello!, '+member)
        import sys
        sys.exit()
print('who are you')
