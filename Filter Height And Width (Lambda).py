l=[{"Cierra Vega":(6.2,70)},{'Alden Cantrell':(5.9,65)},{'Kierra Gentry':(6.0,68)},{"Pierre Cox":(5.8,66)}]
z=dict(filter(lambda x:x[1][0]>6 and x[1][1]>70,l.items()))
print(z)