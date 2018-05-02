x = int(input('Pick a number between 2 and 10'))
if x == 1 or x > 10:
    print('That is not what I asked.')
else:
    print('Please hold while I calculate...')
    while x < 10:
        x += 1
        print (str(x) + ' ...')
        
