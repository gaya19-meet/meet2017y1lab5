#making the function

def add_numbers (start, end, skip):
    #write the body of this
    #function, similar to the block
    #of code we just saw. hint:
    #don't forget to use return
    c = 0
    for number in range (start, end+1,skip):
        #print (number)
        c = c + number
    
    return (c)
    
##################################################

# USing the function

print(add_numbers(0,100,5))

