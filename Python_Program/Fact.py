a=int(raw_input())
factorial=1
if a < 0:
    print "factorial does not exit"
elif a == 0:
    print "factorial is 0"
else:
    for i in range(1,a+1):
       factorial=factorial*i
    print factorial

