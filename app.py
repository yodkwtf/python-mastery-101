d = dict(a=1,b=2)

# NORMAL WAY
print(d['a']) # 1
print(d['c']) # KeyError

# USING GET METHOD
print(d.get('a')) # 1
print(d.get('c')) # None