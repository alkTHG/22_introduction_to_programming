from collections import Counter, defaultdict, namedtuple

# import shakespeare
shakes = open('shakespeare.txt')
text = shakes.read().split()


# find instances in text
punctuation = {',', '.', ';', ':', '?'}

wordcount = Counter([word.lower() for word in text if word not in punctuation])
print('\ninstances of "hamlet:"', wordcount['hamlet'])
print('\ninstances of "the:"', wordcount['the'])


# populating a list with a tab delimited file
people_file = open("people.txt")

people = []
for line in people_file:
    record = line.rstrip().split('\t')
    people.append(record)

print('\n', people)
print('\n', people[0])
print('\n', people[0][2])

# defaultdict is a type of dict which will use a default value for a key which is not present in the dict

# named tuple

Colour = namedtuple('Colour', ['red', 'green', 'blue'])
tomato = Colour(255,99,71)
chartreuse = Colour(127,255,0)
print('\n', chartreuse.green)
print('\n', tomato.green)

# enumerate allows indexing with a for loop
for i, word in enumerate(punctuation):
    if i % 2 == 0:
        print(i, word)

