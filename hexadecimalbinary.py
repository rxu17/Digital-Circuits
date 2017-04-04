#This method is used to convert binary number to hexadecimal 
hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']      

def binary_to_hex(bin_num):
    hex_num = ''
    count = 0
    number = 0
    string = str(bin_num)
    #print len(string)
    print(string)
    #for digit in string:
    while(count < 4 and count < len(string)): 
        if(string[count] == '1'):
            number += (2^count)
            print string[count]
            print number 
            count += 1
        else:
            count += 1
    hex_num += hex_list[number]
    return hex_num
        
print(binary_to_hex(1010))
            
