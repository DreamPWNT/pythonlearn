if 1:
    print('true')

if not 1:
    print('true')
else:
    print('false')

os, mode = 'Windows', 'mobile'

if os in ['iOS', 'iPhoneIS']:
    print('macOs')
elif mode == 'mobile' and os != 'Windows':
    print('Linux')
else:
    print('unknown?')

os, mode = 'Android', 'mobile'

if mode == 'mobile':
    if os == 'Android':
        print('Linux')
    elif os != 'Windows':
        print('macOS')

choice = 'Windows'

print({
    'macos': 2001,
    'Linux': 1991,
    'Windows': 1985
}[choice])

if choice == 'macos':
    print(2001)
elif choice == 'Linux':
    print(1991)
elif choice == 'Windows':
    print(1985)
else:
    print('Bad choice')
