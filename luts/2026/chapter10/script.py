while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bab!' * 8)
    else:
        print(int(reply) ** 2)

print('Bye')

S = '40'
T = 'xxx'

print(S.isdigit(), T.isdigit())

while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(num ** 2)

print('Bye')
