word = input()
croa_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croa_alp:
    word = word.replace(i, '*')

print(len(word))
