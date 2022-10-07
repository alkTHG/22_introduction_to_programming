shakes = open('shakespeare.txt')
text = shakes.read().split()
print(type(text))
print('number of strings:', len(text))
print('first 20 strings', text[0:10])


#longest word
longest =''
for i in text:
    if len(i) > len(longest):
        longest = i
print('\nlongest word:', longest)


# longest palindrome
longest_palindrome =''
for i in text:
    if i == i[::-1] and len(i) > len(longest_palindrome):
        longest_palindrome = i
print('\nlongest palindrome:', longest_palindrome)

# most common word


def most_common(list):
    counter = 0
    word = list[0]
    for i in list:
        if list.count(i) > counter:
            counter = list.count(i)
            word = i
    return word

# works for nums but not for text
nums = (2, 1, 2, 2, 1, 3, 3, 3 ,3, 3, 4, 5)
print('\nmost common word:', most_common(nums))
# print('\nmost common word:', most_common(text))


def unique(list):
    i = 0
    count = 0
    while i < len(list) - 1:
        if list[i] != list[i + 1]:
            count += 1
            i += 1
        else:
            i += 1
    return count

print('\nnumber of different words', unique(text))
# print('\nnumber of different words', unique(nums))



def single_occurance(list):

    print('\nwords that appear once:')
    for i in list:
        if list.count(i) == 1:
            print(i)


single_occurance(nums)
single_occurance(text)