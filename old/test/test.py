import sys

a = sys.path[0].split('\\')
a = a[:len(a)-1]
a.append('config.ini')
print('/'.join(a))
