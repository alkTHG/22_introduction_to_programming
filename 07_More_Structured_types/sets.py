# declaring a set
a_set = {'a', 'set'}
this_is_a_set = set(['this', 'is', 'a', 'set'])
this_is_another_set = {'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
                       'def',
                       'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
                       'lambda',
                       'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'}

# import shakespeare
shakes = open('shakespeare.txt')
text = shakes.read().split()

# number of unique words in the works of shakespeare
print('\nnumber of unique words in the works of shakespeare', len(set(text)))

# creating a set with a for loop or with a single line
punctuation = {',', '.', ';', ':', '?'}
non_punc = list()
for word in text:
    if word not in punctuation:
        non_punc.append(word)
print('\nnumber of non-punctuation unique words in the works of shakespeare', len(set(non_punc)))

print('\nnumber of non-punctuation unique words in the works of shakespeare',
      len({word for word in text if word not in punctuation}))

# membership
print('\nis the word mongoose in the works of shakespeare?', 'mongoose' in text)
print('\nis the word mongoose NOT in the works of shakespeare?', 'mongoose' not in text)

# adding and deleting
punctuation.add('&')
print('\n',punctuation)
punctuation.remove('&')
print('\n',punctuation)

# logical set operations
s1, s2 = {1, 2, 3, 4, 5}, {4, 5, 6, 7, 8}
s1.intersection(s2)         # => {4, 5}
s1.union(s2)                # => {1, 2, 3, 4, 5, 6, 7, 8}
s1.difference(s2)           # => {1, 2, 3}
s1.symmetric_difference(s2) # => {1, 2, 3, 6, 7, 8}


