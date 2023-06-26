#Given an Integer, n and ns pace, integers as input
#Create tuple T
#N Integers
#Compute and print result of hash(t)


if __name__ == '__main__':
   n = int(raw_input())
   integer_list = map(int, raw_input(). split())
   t = tuple(integer_list)
   print(hash(t))