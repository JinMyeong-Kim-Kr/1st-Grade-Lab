#20181599 김진명
n = int(input("초를 입력하세요"))
day = 0
hour = 0
min = 0
sec = 0
print("현재 시간은 ")
if n >= 86400:
    day = n // 86400
    n = n%86400
    hour = n//3600
    n = n%3600
    min = n//60
    n = n%60
    sec = n

elif n>=3600:
    hour = n//3600
    n = n%3600
    min = n//60
    n = n%60
    sec = n
elif n>= 60:
    min = n//60
    n = n%60
    sec = n

else:
    sec = n

print(day,"일",hour,"시",min,"분",sec,"초")
