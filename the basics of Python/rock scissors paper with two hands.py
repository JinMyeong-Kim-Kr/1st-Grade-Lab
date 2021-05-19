import random
print("***가위바위보 게임***")
print("가위, 바위, 보>>>")
r_user = input("오른손에 무엇을 내겠습니까?>>")
l_user = input("왼손에 무엇을 내겠습니까?>>")

cplist = ["가위","바위","보"]
r_cp = cplist[random.randint(0,2)]
l_cp = cplist[random.randint(0,2)]

cph = [l_cp, r_cp]
cphand = cph[random.randint(0,1)]

print("*상대가 낸 것*")
print("왼손>>",l_cp,"오른손>>",r_cp)
print("어느 손을 내겠습니까?>>>왼손, 오른손:")

user_hand = input()
if user_hand == "오른손":
    if r_user == cphand:
        print("비겼습니다")
    elif r_user == "가위":
        if cphand == "바위":
            print("당신의 패배입니다.")
            print("상대가 낸 것>",cphand)
        else:
            print("당신의 승리입니다.")
            print("상대가 낸 것>",cphand)

    elif r_user == "바위":
        if cphand == "보":
            print("당신의 패배입니다.")
            print("상대가 낸 것>",cphand)
        else:
            print("당신의 승리입니다.")
            print("상대가 낸 것>",cphand)
        
    elif r_user == "보":
        if cphand == "가위":
            print("당신의 패배입니다")
            print("상대가 낸 것>",cphand)
        else:
            print("당신의 승리입니다.")
            print("상대가 낸 것>",cphand)
else:
    if l_user == cphand:
        print("비겼습니다")
    elif l_user == "가위":
        if cphand == "바위":
            print("당신의 패배입니다.")
            print("상대가 낸 것>",cphand)
        else:
            print("당신의 승리입니다.")
            print("상대가 낸 것>",cphand)

    elif l_user == "바위":
        if cphand == "보":
            print("당신의 패배입니다.")
            print("상대가 낸 것>",cphand)
        else:
            print("당신의 승리입니다.")
            print("상대가 낸 것>",cphand)
        
    elif l_user == "보":
        if cphand == "가위":
            print("당신의 패배입니다")
            print("상대가 낸 것>",cphand)
        else:
            print("당신의 승리입니다.")
            print("상대가 낸 것>",cphand)
    
