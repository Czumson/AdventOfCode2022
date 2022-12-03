import string

alphabet = list(string.ascii_letters)
priority = list(range(1, len(alphabet)+1))

value = dict(zip(alphabet, priority))
result = 0

'''
#first task

with open("data3.txt") as f:
    lines = f.read().splitlines()
    for line in range(len(lines)):
        slice_ind = int(len(lines[line])/2)
        set1 = list(lines[line][:slice_ind])
        set2 = list(lines[line][slice_ind:])
        
        common = list(set(set1).intersection(set2))[0]
        result = result + value[common]

'''
#second task

with open("data3.txt") as f:
    lines = f.read().splitlines()
    for line in range(len(lines))[::3]:
        common = set(lines[line]) & set(lines[line+1]) & set(lines[line+2])        
        result = result + value[common.pop()]
        
print(result)