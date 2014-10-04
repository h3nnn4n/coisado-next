#!/usr/bin/python

def rating(ra,rb,pa):
    k=20
    maxval=400

    pb=1-pa

    dr=rb-ra
    if dr>=0 :
        if(dr>maxval) :
            dr=maxval
    else:
        if dr<0 :
            dr=-maxval

    ea=1/(1+k**(dr/400))
    eb=1-ea
    print(ea)

    nra=ra+k*(pa-ea)
    nrb=rb+k*(pb-eb)

    print('%.1f %.1f' % (nra,nrb))

rating(1500,1500,1)
