poem = '''There was a young lady named Bright,
    Whose speed was far faster than light;
    She started one day
    In a relative way,
    And returned on the previous night.'''
# print(len(poem))
#
# fout = open('relative', 'wt')
# fout.write(poem)
# fout.close()

fout = open('relativity', 'wt')
print(poem)
print(poem, file=fout)
fout.close()

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
