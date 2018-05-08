your_numbers = input("Please give me a series of numbers separated by a dash: ")
split_numbers = your_numbers.split('-')
squared_dictionary = {}
for item in split_numbers:
    valuepair = int(item) ** 2
    squared_dictionary[item] = valuepair
#{squared_dictionary: squared_dictionary ** 2 for squared_dictionary in true_numbers}
for k,v in squared_dictionary.items():
    print (k, v)
