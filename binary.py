bdata = bytes(range(0, 256))
len(bdata)

fout = open('bfile', 'wb')
fout.write(bdata)

fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    print(fout.write(bdata[offset:offset+chunk]))
    offset += chunk

fout.close()

fin = open('bfile', 'rb')
bdata = fin.read()
len(bdata)

fin.close
