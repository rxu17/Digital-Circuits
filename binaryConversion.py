#This algorithm will (attempt) to convert regular numbers to binary numbers

import re 

ct2 = 0

def int_to_binary(integer):
    res = integer
    binary = ""
    while(res > 0):
        power2 = largest_power_of_2(integer)
        res -= power2
        binary += "1"
        while (ct2 - 1) > 1:
            binary += "0"
            ct2 -= 1
    return int(binary)
      

print("Please enter a binary number")
binary = input(">")
# catching cases when the entered value is not what we want
while binary.isnumeric() != True and bool(re.match('^[10]+$', binary)) != True:
    print("Please enter a binary number")
    binary = input(">")
    

def largest_power_of_2(num):
    s = 2
    while(s < num):
        s *= 2
        ct2 += 1
    return s/2   
        
def binary_to_int(binary):
    string = str(binary)
    integer = 0
    count = len(string)
    while count > 0:
        if string[count-1] == "1":
            integer += 2^(count-1)
            count -= 1
        elif string[count-1] == "0":   
            count -= 1      
        else:
            print("This is not a binary number. Try again")
            break   
    return integer
    
print(binary_to_int(binary))

        
