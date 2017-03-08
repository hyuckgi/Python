# -*- coding: utf-8 -*-

score = raw_input("Input your Score ")

print score
score = int(score) #입력받은 값을 문자로 인식하기 때문에 숫자로 변환

if score > 90:
    print "A"
elif score > 80 and score <= 90:
    print "B"
elif score > 70 and score <= 80:
    print "C"
elif score > 60 and score <= 70:
    print "D"
elif score <= 60:
    print "F"
else:
    print "score is under 100"


# retry
