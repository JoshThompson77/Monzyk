"""Requirements to do anlaysis
Two test tubes
10ml of butanol in one
2ml of butanol and 2 ml of ferric nitrate
add approximately .200 grams of extractant to 10 ml of butanol
mix for 5 minute
take 50 microliters from the new mixture add to the 2ml 2ml mixture test tube
mix for 5 minute
Then use UV vis at 525 nm to get UV number for calculation
"""

from tkinter import *

def moty_calc(UV):
    c = 1066
    moty = UV/(1*c)
    return moty

def weight_calc(UV):
    mw = 230.38
    amount = .00205
    moty = moty_calc(UV)
    weight = mw * moty * amount
    return weight

def dilution_calc(UV):
    weight = weight_calc(UV)
    dilution = weight * 200
    return dilution

def concentration_calc(UV, size):
    global bottom
    global answer

    answer.destroy()

    dilution = dilution_calc(UV)
    concentration = dilution/size * 100
    concentration = round(concentration,2)
    

    answer= Label(bottom, text=str(concentration))
    answer.pack()




