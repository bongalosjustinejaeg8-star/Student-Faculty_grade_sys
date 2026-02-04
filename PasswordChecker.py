import string

a = string.punctuation
b = string.digits
c = string.ascii_uppercase
pas = input()
d = 0
e = 0
f = 0

for cr in pas:
    if cr in a:
        d += 1
    elif cr in b:
        e += 1
    elif cr in c:
        f += 1

ea = d>=1
eb = e>=2
ec = e>=1

if ea and eb and ec:
    print ('stronk')
else:
    print ('weak')
    








