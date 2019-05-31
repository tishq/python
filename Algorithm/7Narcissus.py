nar = []
for i in range(0,9):
    for j in range(0,9):
        for k in range(0,9):
            if (i*i*i+j*j*j+k*k*k)==(i*100+j*10+k):
                if i != 0:
                   nar.append(i*100+j*10+k)
print(nar)