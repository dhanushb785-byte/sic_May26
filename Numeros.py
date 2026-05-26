def numeros(l1,l2):
    l3=[]
    for i in range(len(l2)):
        if l2.count(l2[i]) == 1:
            if l2 [i] not in l1:
                l3.append(l2[i])
        
        if l1.count(l2[i])  != l2.count(l2[i]):
            l3.append(l2[i])
    s1=set(l3)
    print('_______MISSING NUMBERS ARE:______')
    print(sorted(s1))

print('enter 2 list ')
l1=[ int(i) for i in input('').split()]
l2=[ int(i) for i in input('').split()]

numeros(l1,l2)

