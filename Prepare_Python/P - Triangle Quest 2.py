#You are given integer N
#print a palindromic triangle of size N

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((((10**i) - 1)//9)**2) #palindrome formula

'''    
((10**i) - 1) raises 10 to the power of i, subtracts 1, and returns the result. For example, if i is 3, it calculates (10**3) - 1 = 1000 - 1 = 999.
// 9 performs integer division by 9, resulting in ((10**i) - 1) // 9 = 999 // 9 = 111.
** 2 squares the value obtained from the previous step, giving (((10**i) - 1) // 9) ** 2 = 111 ** 2 = 12321. '''    