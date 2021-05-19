


def readFile(friends):
    try:
        infile = open("HW5_input.txt", "r")
    
        for line in infile:
            line = line.rstrip()
            line = line.split(":")
            friends[line[0]] = line[1] #읽어들인 파일을 딕셔너리로 변환
            
        for key,value in friends.items():
            print(key,':',value)
            
        infile.close()
    except:
        print("잘못된 파일 입니다.")

def addFile(friends,name, contact):
    try:
        outfile = open("HW5_input.txt", "a")
        outfile.write(name+":"+contact+"\n")
        outfile.close()
    except:
        print("없는 파일 입니다.")

def writeFile(friends):
    try:
        outfile = open("HW5_input.txt", "w")
        for value, key in friends.items():
            outfile.write(value+":"+key + "\n")
        outfile.close()
    except:
        print("없는 파일 입니다")

menu = 0
friends = {}
readFile(friends)
while menu != 9:
    print("--------------------")
    print("1. 연락처 리스트 출력")
    print("2. 연락처 추가")
    print("3. 연락처 삭제")
    print("4. 이름 변경")
    print("9. 종료")
    menu = int(input("메뉴를 선택하시오: "))
    
    if menu == 1:
        readFile(friends)
        
    elif  menu== 2:
        name = input("이름을 입력하시오: ")
        contact = input("연락처를 입력하세요: ")
        addFile(friends, name, contact) #append 모드로 파일 열고 새입력값  넣기
        readFile(friends) 
        
    elif  menu == 3:
        try:
            del_name = input("삭제하고 싶은 이름을 입력하시오:  ")
            del friends[del_name]
            writeFile(friends) #file에 변경된 friends를 다시 파일에 씀 
        except:
            print("이름이 발견되지 않았음")
            
    elif  menu == 4:
        old_name = input("변경하고 싶은 이름을 입력하시오: ")
        if old_name in friends.keys():
            new_name = input("새로운 이름을 입력하시오: ")
            friends[new_name] = friends[old_name] #새 이름의 key와 옛 value 생성
            del friends[old_name] # 옛 이름을 가진 key,value 삭제
            writeFile(friends) #file에 변경된 friends를 다시 파일에 씀 
        else:
            print("이름이 발견되지 않았음")
            
    elif menu == 9:
        break
    else:
        print("올바른 숫자를 입력하세요.")
        continue
