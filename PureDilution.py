def puredilution(wantedpercent, totalconcentrate, actualpercent):
    percent = actualpercent
    totalmass = totalconcentrate
    pirmass = totalmass * (percent / 100)
    othermass = totalmass - pirmass
    targetpercent = wantedpercent
    totalnewmass = pirmass / (targetpercent / 100)
    decanol = totalnewmass * .05
    kerosene = totalnewmass - pirmass - decanol - othermass
    return kerosene, decanol

print(puredilution(26, 5700, 31))
