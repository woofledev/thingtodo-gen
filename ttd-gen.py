import urllib.request, random
with urllib.request.urlopen('https://raw.githubusercontent.com/woofledev/thingtodo-gen/main/list.txt') as res:
    ln=res.read().decode().splitlines()
sel_ln=random.choice(ln[4:])

print('thingtodo-gen')
print('-*-*-*-*-*-*-')
print(sel_ln)
print('Line: '+str(ln.index(sel_ln)-3))