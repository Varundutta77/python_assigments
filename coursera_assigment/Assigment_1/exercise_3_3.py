score=float(input('Enter your CGPA Score : '))
if score>1:
    print('Out of Range')
elif score>= 0.9:
    print("Congratulation!! you got 'A' Grade")
elif score>= 0.8:
    print("Well Done !! you got 'B' Grade")
elif score>= 0.7:
    print("Good!! you got 'C' Grade")
elif score>= 0.6:
    print("You need to practice!! you got 'D' Grade")
elif score < 0.6:
    print("You need to practice hard , you got 'F' Grade" )
else:
    print('Wrong Input')
