from pykeepass import PyKeePass
kp = PyKeePass('Passwords.kdbx', password='')
group = kp.find_groups(name = 'почты', first = True)

def get_entry(dolboeb):
    entry = kp.find_entries(title=dolboeb, regex=True, first=True)
    output2 = 'Title: ' + entry.title  + '\n' + \
              'Url: ' + entry.url +  '\n' + \
              'Username: ' + entry.username +  '\n' + \
              'Password: ' + entry.password
    return output2



while True:
    find = input('введите имя записи ')
    print(get_entry(find))
