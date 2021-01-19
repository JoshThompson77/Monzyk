
def dilution(lowpercent, highpercent, lowtotalmass, goalpercent):
    percentlow = lowpercent/100
    totalmass = lowtotalmass
    piranhalow = totalmass * percentlow
    percenthigh = highpercent/100
    goal = 0
    addedmass = 0
    while goal < goalpercent:
        addedmass = addedmass + 1
        highpir = addedmass * percenthigh
        totalpir = highpir + piranhalow
        newtotalmass = addedmass + totalmass
        goal = totalpir / newtotalmass * 100
    return newtotalmass - totalmass

print(dilution(30.17, 72.5, 1493.31, 40))

