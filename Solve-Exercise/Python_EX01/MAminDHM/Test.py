#s = input("input : \n \t")

#s = s.replace(' ', '')
#print(set(s))

#d = {'a':1, 'b':2}
#print(list(d.keys()))
#print(list(d.values()))
#t = (1, 2, 3)
#s = {'a','b','a'} #error

#a = [2,2,2,1,1,3]
#a = set(a)
#print(a)
columns = ['Name', 'Frequency']
print('+' + 8 * '-' + '+' + 13 * '-' + '+')
print(f"|  {columns[0]:^5} |  {columns[1]:^10} |")
print('+' + 8 * '=' + '+' + 13 * '=' + '+')

#def function(arg1, arg2, ..., arg100):
#  return h

#a = [1,2, ...., 100]

#g  = function(*a) = function(1,2,3,4,..., 100)

a = ['a', 'b']
b = [1, 2]

for i , j in zip(a,b):
    print(i, j)

