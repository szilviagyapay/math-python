start = 1
end = 1
isPalindrom = 1
n = 100
m = 100
current = 0
candidate = 0

for n in range(100, 1000):
  for m in range(100, 1000):
    isPalindrom = n*m
    s = str(isPalindrom)
    i = 0
    l = len(s)
    isP = True
    while i<int(l/2):
        if s[i] == s[l-i-1]:
            i += 1
        else:
            i = int(l/2)
            isP = False
    if isP == True:
        print("length = ", l)
        print("number = ", isPalindrom)
        if current < isPalindrom:
            current = isPalindrom
print("Max: ", current)

for n in range(100,1000):
  for m in range(100, 1000):
    isPalindrom = n*m
    candidate = isPalindrom
    end = isPalindrom%10
    if isPalindrom >= 100000:
      start = isPalindrom/100000
      if start == end:
        isPalindrom = isPalindrom - end
        isPalindrom = isPalindrom - 100000*start
        isPalindrom = isPalindrom/10
        end = isPalindrom%10
        start = isPalindrom/1000
        if start == end:
          isPalindrom = isPalindrom - 1000*start
          isPalindrom = (isPalindrom - end)/10
          if isPalindrom%11 == 0:
              print("A Palindrom is found:", n*m)
              if current < candidate:
                  current = candidate
    else:
      start = isPalindrom/10000
      if start == end:
        isPalindrom = isPalindrom - end
        isPalindrom = isPalindrom - 10000*start
        isPalindrom = isPalindrom/10
        end = isPalindrom%10
        start = isPalindrom/100
        if start == end:
          print("A Palindrom is found: ", n*m)
          if current < candidate:
              current = candidate
print("Greatest: ", current)
