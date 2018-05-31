i = 9876
found = False

def isDifferent(k):
    s = []
    for l in range(0,len(k)):
        if not (k[l] in s):
            s.append(k[l])
    print("i = ", k, "set: ", s)
    if len(s) == 4:
        return True
    else:
        return False

def isPandigital(k):
    s = []
    isZeroIn = False
    for l in range(0,len(k)):
        if not(k[l] in s):
            s.append(k[l])
            if k[l] == "0":
                isZeroIn = True
    if len(s) == 9:
        if isZeroIn == False:
            return True
        else:
            return False
    else:
        return False

result = 0
while (9122<i):
  j = 2*i
  if isDifferent(str(i)):
      print(i)
      if isPandigital(str(i)+str(j)):
          found = True
          result = i
  if found:
      i = 9120
  i = i - 1
print(result)
