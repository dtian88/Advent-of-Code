state = {1: {'SG', 'SM', 'PG', 'PM'}, 2: {'TG', 'RG', 'RM', 'CG', 'CM'}, 3: {'TM'}, 4: set()}

m = {'SM', 'PM', 'RM', 'CM', 'TM'}
g = {'SG', 'PG', 'RG', 'CG', 'TG'}

def children(s):
  c = []
  for i in s:
    if i[1] == 'M':
      c.append(i)
    else:
      if not i[0] + 'M' in s:
        c.append(i)
      else:
        g.remove(i)
        if not len(s.intersection(g)):
          c.append(i)
        g.add(i)
  return c

def recur(s, level):
  pass

print(children(state[4]))