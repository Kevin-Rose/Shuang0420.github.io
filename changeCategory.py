import os
files = os.listdir(os.getcwd())
for name in files:
    if not name.endswith('.md'):
        continue
    f = open(name, 'r')
    l = f.readlines(10)
    sub = ''
    subindex = ''
    for index, str in enumerate(l):
        if str.startswith('categories: Search Engines'):#and str.endswith(']\n'):
            print str
            sub = 'categories: [NLP,Search Engines] \n'
            subindex=index
            break
    if subindex:
        lines = open(name, 'r').readlines()
        fw = open(name,'w')
        lines[subindex]=sub
        fw.write(''.join(lines))
        fw.close()
