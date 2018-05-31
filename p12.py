import numpy as np
import itertools

def permutation(s,pref,perms):
  if (len(s)==0):
    perms.append(pref)
    return perms
  else:
    for i in range(len(s)):
      rem = s[0:i]+s[i+1:]
      permutation(rem,pref+s[i],perms)

perms = []

fact_sets = []

for i in range(1,11):
    s = set(itertools.combinations([0,1,2,3,4,5,6,7,8,9],i))
    for s1 in s:
        str1 = ""
        for j in s1:
            str1 = str1 + str(j)
        if not str1 in fact_sets:
            if not str1 == "0":
                fact_sets.append(str1)

members = dict({})

friend_sets = dict({})
count_members = dict({})

for s in fact_sets:
        members[s] = []
        friend_sets[s] = []
        count_members[s] = 0

for key in friend_sets:
    for key1 in friend_sets:
        if not key == key1:
            friends = False
            if 0<len(list(set(key) & set(key1))):
                friend_sets[key].append(key1)

pairs_of_friends = 0

for i in range(1,1000):
    str1 = ''.join(sorted(set(str(i))))
    count_members[str1] += 1

for key in fact_sets:
    mult1 = 0
    for j in friend_sets[key]:
        mult1 += count_members[j]
    pairs_of_friends += mult1 * count_members[key]

print(pairs_of_friends)
