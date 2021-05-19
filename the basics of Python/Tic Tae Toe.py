import random

board = [['' for x in range(3)] for y in range(3)]
cnt = 0
while True:
    #게임보드 그리기
    for r in range(3):
        print("   "+board[r][0] + "|" + board[r][1] + "   |" + board[r][2])
        if (r!=2):
            print("---|---|---")
    #사용자 좌표 입력
    x = int(input("다음 수의 x좌표를 입력하세요:"))
    y = int(input("다음 수의 y좌표를 입력하세요:"))
 
    
    #사용자 좌표 검사
    
    if board[x][y] != '':
        print("잘못된 위치입니다.")
        continue
    else:
        board[x][y] = 'X'
        cnt +=1 #게임 카운트 세기
        
    

    #컴퓨터가 놓을 위치 결정, 첫 번째로 발견하는 비어있는 칸에 놓는다
    #컴퓨터가 random하게 위치를 찾아서 말을 놓을 수 있도록 변경해주세요.

    cx = random.randint(0,2)
    cy = random.randint(0,2)
    while True: #중복 위치 방지
        if (board[cx][cy] == 'X') or (board[cx][cy] == 'O'):
            cx = random.randint(0,2)
            cy = random.randint(0,2)
            if cnt == 5: #더이상 놓을 곳이 없을 때 break
                break
        else:
            board[cx][cy] = 'O'
            break
    

    
    #승리자가 있는지 확인하세요
        #가로
    if (board[0][0] == 'X') and (board[0][1] == 'X') and (board[0][2] == 'X'):
        print("당신의 승리입니다")
        break
    elif (board[1][0] == 'X') and (board[1][1] == 'X') and (board[1][2] == 'X'):
        print("당신의 승리입니다")
        break
    elif (board[2][0] == 'X') and (board[2][1] == 'X') and (board[2][2] == 'X'):
        print("당신의 승리입니다")
        break
    
        #세로
    
    elif (board[0][0] == 'X') and (board[1][0] == 'X') and (board[2][0] == 'X'):
        print("당신의 승리입니다")
        break
    elif (board[0][1] == 'X') and (board[1][1] == 'X') and (board[2][1] == 'X'):
        print("당신의 승리입니다")
        break
    elif (board[0][2] == 'X') and (board[1][2] == 'X') and (board[2][2] == 'X'):
        print("당신의 승리입니다")
        break

        #대각선
    
    elif (board[0][0] == 'X') and (board[1][1] == 'X') and (board[2][2] == 'X'):
        print("당신의 승리입니다")
        break
    elif (board[0][2] == 'X') and (board[1][1] == 'X') and (board[2][0] == 'X'):
        print("당신의 승리입니다.")
        break
    elif cnt == 5: # 승패가 나지 않고,
                               #카운트가 5가 되어 더 이상 놓을 곳이 없을때
        print("비겼습니다.")
        break


    #컴퓨터 승리 판정

        #가로
    
    if (board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == 'O'):
        print("당신의 패배입니다")
        break
    elif (board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == 'O'):
        print("당신의 패배입니다")
        break
    elif (board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == 'O'):
        print("당신의 패배입니다")
        break
    
        #세로
    
    elif (board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == 'O'):
        print("당신의 패배입니다")
        break
    elif (board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == 'O'):
        print("당신의 패배입니다")
        break
    elif (board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == 'O'):
        print("당신의 패배입니다")
        break
    
        #대각선
    
    elif (board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == 'O'):
        print("당신의 패배입니다")
        break
    elif (board[0][2] == 'O') and (board[1][1] == 'O') and (board[2][0] == 'O'):
        print("당신의 패배입니다.")
        break
    
    
   
