mydata =	{
  "name:": "Paulo",
  "Personality:": "A complete idiot",
  "Age:": 55,
  "Years working:": "Too much"
}

print(mydata)

print('\nEssas são as [keys]')
for x in mydata:
    print(x)

print('\nEssas são os [values]')
for x in mydata:
    print(mydata[x])

print('\nEssas são os [values], chamados de outra forma')
for x in mydata.values():
    print(x)

print('\nEssas é a impressão completa do Dicionário')
for x,y in mydata.items():
    print (x,y)

if "Age:" in mydata:
    print('\nVerifica se uma key está presente no Dic')
    print("Yes, 'Age:' is one of the keys in the mydata dictionary")

if "55," in mydata:
    print('\nVerifica se um value está presente no Dic')
    print("Yes, '55' is one of the values in the mydata dictionary")
