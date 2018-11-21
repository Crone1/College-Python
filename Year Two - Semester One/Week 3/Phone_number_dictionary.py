print('Enter a name and number, or a name and ? to query (!! to exit)')
command = input()
phone_book = {}

while command != '!!':
    l = command.split(' ')
    
    if l[1] == '?' and not l[0] in phone_book:
        print('Sorry, there is no {}'.format(l[0]))
        
    elif l[1] == '?' and l[0] in phone_book:
        print('{} has number {}'.format(l[0], phone_book[l[0]]))

    elif l[1] != '?' and l[0] and l[1]:
        phone_book[l[0]] = l[1]
    
    command = input()
    
print('Bye')