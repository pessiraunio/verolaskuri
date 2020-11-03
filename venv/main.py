numb = 1000

while numb > 994:
    string = str(numb)
    numb = numb - 1
    print(string)

test = ('kivaaa'+string)

for i in test:
    print(i)


setti = 'Kaliaa ja köisää -vitttu öisää löisää köissää köisää saaatanaperkele'

haku = 'tana'

count = 0

for letter in setti:

    count = count + 1
    if letter == '-':
        if (setti[count:]) == 'vitttu saaatanaperkele':
            print('good')
        break
    else:
        continue



sp = 'köisää'
sana = ''

for i in sp:
    if i in sp:
        sana = sana + i
    else:
        continue

print(sana)