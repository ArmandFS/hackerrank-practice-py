#hackerrank string formatting
#given an integer n. print the following values for I from 1 to n

def print_formatted(number):
    #code goes here
    for num in range(1, number + 1):
        oct_num = oct(num) #convert to octal
        hex_num = hex(num) #convert to hex
        hex_num_upper = hex_num[2:].upper() #convert hex to upperclass
        bin_num = bin(num) #convert to binary
        print(f"{num:2}  {oct_num[2:]:<2}  {hex_num_upper:<2}  {bin_num[2:]:<2}")
    

n = int(input())
print_formatted(n)