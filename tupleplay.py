your_numbers = input('Please give me a bunch of numbers separated by a comma: ')
numberlist = your_numbers.split(',')
lista = numberlist[::2]
listb = numberlist[1::2]
print (lista)
print (listb)
zippedlist = zip(lista, listb)
print(list(zippedlist))
