def maxmin(lista, nmax,nmin):
    if(nmin+nmax)<=len(lista):
        lista.sort(reverse=True)
        list_max= lista[0:nmax]
        list_min= lista[-nmin:-1]
    return list_max+list_min
