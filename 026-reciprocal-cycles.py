
max_serie = ""
for i in range(1, 1001):
    f = str(1.0 / float(i))[2:]
    serie = ""
    for c in f:        
        serie += c     
        print(f)   
        if f.index(serie) > 0:
            max_serie = serie
            print(serie)
print(max_serie)