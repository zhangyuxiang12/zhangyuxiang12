age=30
count=0
while count<3:
    n=int(input("你有多大了？"))
    if n!=age and count<2:
        print('再来一次')
    else:
        print('666')
        exit()
    count += 1
    