def oldShoeSale(p, l):
    earnings = 0
    count = 0

    for i in l:
        if count < p:
            if i < 0:
                earnings += i
                count += 1
        else:
            break

    print("___TOTAL EARNINGS__\n", -earnings)


          

            
            
    
            
                
       
           
                
           

