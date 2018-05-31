def permutation(s,pref,perms):
  if (len(s)==0):
    perms.append(pref)
    return perms
  else:
    for i in range(len(s)):
      rem = s[0:i]+s[i+1:]
      permutation(rem,pref+s[i],perms)

perms = []

permutation("1234","",perms)
print(perms)
