'''Functions to shift row inside round'''
import copy


def shiftrows(block_list):
    wbl = copy.deepcopy(block_list)
    # partiamo dalla prima riga... ah non gli si fa nulla

    # andiamo alla seconda riga, in cui tutto è spostato a sx di uno
    temp = wbl[0][1]
    for i in range(3):
        wbl[i][1] = wbl[i+1][1]
    wbl[3][1] = temp

    # andiamo alla terza riga, in cui tutto è spostato a sx di due
    # qui dobbiamo in sostanza scambiare 0 <-> 2 e 1 <-> 3
    for i in range(2):
        temp = wbl[i][2]
        wbl[i][2] = wbl[i+2][2]
        wbl[i+2][2] = temp

    # finiamo con la quarta riga, in cui tutto è spostato a sx di tre
    # qui dobbiamo in sostanza spostare di uno a dx
    temp = wbl[3][3]
    for i in range(3, 0, -1):
        wbl[i][3] = wbl[i-1][3]
    wbl[0][3] = temp

    return wbl
