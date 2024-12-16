def Pyramid():
    num = int(input('Give me a irregular number(e.g. 1,3,5,7,9)'))
    test = num // 2 
    test1 = num % 2 
    test2 = test+1
    for x in range(1, test+1):
        #test = num // 2 
        print('x'*x)
    if test1 == 1:
        print('x'*test2)
    for x in range(test,0, -1 ):
        print('x'*x)

def Tree ():
    length = int(input('How big does this tree need to be : '))
    end = length
    for x in range(1,length+1):
            if x % 3 == 0:
                testAmount = 'x'*(x-1)
                pretty = 'x'*((x-1)//2)
                realAmount = pretty + 'o' +pretty +'o'+ pretty +'o'+pretty
                if x %2 == 1:
                    print(' '*length,realAmount[:-2])
                else: 
                    print(" "*length,realAmount)
                length -= 1
            else :
                testAmount = 'x'*x
                realAmount = testAmount + 'x'*(x-1)
                print(" "*length,realAmount)
                length -= 1
    if end%2 ==1:
        print(' '*end,'x')
    else :
        end = end -1
        print(' '*end,'x'*2)

        
Tree()