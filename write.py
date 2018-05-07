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

# test_tx = '''testです。'''
#
# fout = open('test_tx.txt', 'wt')
# print(test_tx, file=fout)
# fout.close()
#
# fout = open('relativity2', 'wt')
# print(poem)
# print(poem, file=fout)
# fout.close()
#
# fout = open('relativity', 'wt')
# size = len(poem)
# offset = 0
# chunk = 100
# while True:
#     if offset > size:
#         break
#     fout.write(poem[offset:offset+chunk])
#     offset += chunk

# fout = open('relativity', 'wt')
# print(poem, file=fout, sep='', end='')
# fout.close()

# fout = open('relativity', 'wt')
# size = len(poem)
# print(size)
# offset = 0
# chunk = 100
# while True:
#     print(offset)
#     if offset > size:
#         break
#     fout.write(poem[offset:offset+chunk])
#     offset += chunk

# fout.close()

# fout = open('relativity', 'xt')

try：
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity lready exists!. Than was a close one.')
    
