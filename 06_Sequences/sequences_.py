# immutable
tuple = (1, 'tuple')
print(type(tuple))

# mutable
list = [1, 'list', (1, 'tuple')]
print(type(list))

# item in list?
print(1 in list)
print('tuple' in list)

# for loop
print('\nfor loop:')
for i in list:
    print(i)

# range (start, end (exclusive), increment)
print('\nrange:')
for i in range(2, 11, 2):
    print(i)

# append
print('\nappend:')
list.append('end item')
print(list)

# pop
print('\npop:')
print(list.pop(3))
print(list)

# change at index
print('\nchange at index:')
list[0] = 2
print(list)

# extend list (iterable - append would add a list, extend adds each item sequentially)
print('\nextend:')
list.extend(('an', 'extension'))
print(list)

#slicing
odds = [0, 3, 5, 7, 9, 11]
odds[0] #=> 1
odds[1:3] #=> [3, 5]
odds[:3] #=> [1, 3, 5]
odds[3:] #=> [7, 9, 11]

#sum
print('\nsum:')
print(sum(odds))

# min and max
print('\nmin and max:')
print(min(odds))
print(max(odds))

# all (no false or 0) and any (any true or 1)
print('\nall and any:')
print(all(odds))
print(any(odds))

# strings
print('\nstrings:')
str = 'string'
multi_str = """i am 
a
multiline
string"""
print(multi_str)
print('length of string:', len(str))
print('third character:', str[2])
print('range of string:', str[:3], str[3:5], str[5:])
for i in str:
    print(i)
print('ring' in str)

# dictionaries
print('\ndictionaries')
numerals = {'I': 1, 'V': 5, 'X': 10}
print(numerals['V'])
print('V' in numerals)
for key in numerals:
    print(key, "=>", numerals[key])

# curl https://inst.EECS.Berkeley.EDU//~cs61a/fa11/shakespeare.txt > shakespeare.txt

