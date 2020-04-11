def datas(name,*type1,**type2):
    print(name)
    # accessing *type1 (*args)
    for i in type1:
        print(i)
    # accessing **type2 (**kwargs)
    for i,j in type2.items():
        print(i,j)


x=datas("Prabin", 1, 2, 3, 4, age=19, city='Butwal')
