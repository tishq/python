n = int(input('input a number：'))
m=0
q=0
o=0
p=int(n/2+1)
for q in range(0,p):
        if n%2==0:
          if o==0:
              m=m
              o=o+2
          else:
           m=m+1/o
           o = o + 2
        else :
          m=m+1/(o+1)
          o=o+2
print(m)

