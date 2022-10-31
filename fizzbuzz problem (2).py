for i in range(1,100):
    if(i%15==0):
        print('fizzbuzz')
        continue
    elif(i%3==0):
        print('fizz')
        continue
    elif(i%5==0):
        print('buzz')
        continue
    else:
        print(i)