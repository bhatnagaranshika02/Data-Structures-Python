def recur_mult(a,b):
    if x<y:
        return recur_mult(b,a)
    if y==0:
        return 0
    else:
        return x+recur_mult(x,y-1)

x = 500
y = 2000

print(x * y)
print(recur_mult, y)
