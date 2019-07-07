'''Given the following list of strings:
names = ['alice', 'bertrand', 'charlene']
produce the following lists: (1) a list of all upper case names; (2) a list of
capitalized (first letter upper case);'''

names = ['alice', 'bertrand', 'charlene']

upNames =[x.upper() for x in names]
print(upNames)

cNames = [x.title() for x in names]
print(cNames)