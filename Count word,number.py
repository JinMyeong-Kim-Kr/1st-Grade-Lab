word = ""
number = ""
while True:
    s = input("아무거나 입력하세요>>")
    for i in s:
        if i.isalpha():
            word += i
        if i.isdigit():
            number += i
    print("입력 받은 문자 =",s)
    print("문자는",word)
    print("숫자는",number)
    answer = input("계속하시겠습니까?>(yes or no)>")
    if answer == "yes":
        word = ""
        number = ""
        continue
    if answer == "no":
        break
