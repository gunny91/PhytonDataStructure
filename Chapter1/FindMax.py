print('Find Max value from 3 integers')

a = int(input('Type integer a')) 
b = int(input('Type integer b'))
c = int(input('Type integer c'))

max = a                 #Set the temporary max value
if b > max: max = b    # if b value is greater than max, then max =b
if c > max: max = c

print(f'Max is {max}')  #return the max value
