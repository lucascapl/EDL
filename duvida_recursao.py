new_list = []


def my_filter(func,lista):
    global new_list
    if not lista:
        return lista
    else:
        if func(lista[0]):
            new_list.append(lista[0])
            my_filter(func, lista[1:])
        else:
            my_filter(func, lista[1:])
    return new_list

def regra(item):
    if item>6 :
        return True
    else:
        return False
 
    

seq=[1,2,3,4,5,6,7,8,9,10]
print(my_filter(regra,seq))
