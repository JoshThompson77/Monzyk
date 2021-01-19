from tkinter import *

class uv_vis_calc:
    """docstring for uv_vis_calc"""
    def __init__(self):
        super(uv_vis_calc, self).__init__()

    def moty_calc(self, UV, size):

        global bottom
        global answer

        answer.destroy()


        constant = 1066
        moty = UV/(1*constant)
        
        mw = 230.38
        amount = .00205
        weight = mw * moty * amount

        dilution = weight * 200
        
        concentration = dilution/size * 100
        concentration = round(concentration,2)

        answer= Label(bottom, text=str(concentration) + ' %', pady = 30)
        answer.grid(row=3, column=1)




class PureDilution(object):
    """docstring for Pure"""
    def __init__(self):
        super(PureDilution, self).__init__()
        

    def pdilution(self, wantedpercent, totalconcentrate, actualpercent):

        percent = actualpercent
        totalmass = totalconcentrate
        pirmass = totalmass * (percent / 100)
        othermass = totalmass - pirmass
        targetpercent = wantedpercent
        totalnewmass = pirmass / (targetpercent / 100)
        decanol = round(totalnewmass * .05, 2)
        kerosene = round(totalnewmass - pirmass - decanol - othermass, 2)


        anframe=Frame(bottom)
        anframe.grid(row=4, column=1)

        answer = Label(anframe, text=str(decanol) + ' grams of Decanol' , pady = 10)
        answer.pack()

        answer2 = Label(anframe, text=str(kerosene) + ' grams of kerosene', pady= 10)
        answer2.pack()



class mixedDilution(object):
    """docstring for mixedDilution"""
    def __init__(self):
        super(mixedDilution, self).__init__()

    def dilution(self, lowpercent, highpercent, lowtotalmass, goalpercent):
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
        

        added = newtotalmass - totalmass


        answer= Label(bottom, text=str(added) + ' grams', pady = 30)
        answer.grid(row=5, column=1)
            
        


an = uv_vis_calc()
an1 = PureDilution()
an2 = mixedDilution()




def bottomFrame(value):
    global bottom

    bottom.destroy()

    bottom = Frame(backlevel, relief=RAISED, bd =2, pady= 20, padx = 40)
    bottom.pack(anchor=N, fill=BOTH, expand=True)

    if value == "Piranha Analysis":

        # Make Labels
        uvvisl = Label(bottom, text= "UV vis")
        amountl = Label(bottom, text='Extractant')

        # Make Entries
        uvvisE = Entry(bottom, width= 17, bd = 3)
        amountE = Entry(bottom, width=17, bd=3)

        # Making Button
        doit = Button(bottom, text="Calculate", padx= 20, pady=10, command= lambda: an.moty_calc(float(uvvisE.get()), float(amountE.get())))

        # Object Placement
        uvvisl.grid(row=0, column=0)
        amountl.grid(row=1, column=0)
        uvvisE.grid(row=0, column=1)
        amountE.grid(row=1, column=1)
        doit.grid(row=2, column=1)

    elif value == "Pure Dilution":

        # Making Labels

        goall = Label(bottom, text="Goal")
        totall = Label(bottom, text='Total Conentrate')
        actuall = Label(bottom, text='Actual Piranha')
        gel = Label(bottom, text='%')
        tel = Label(bottom, text='grams')
        ael = Label(bottom, text='%')

        # Making Entries

        goalE = Entry(bottom, width= 17, bd=3)
        totalE = Entry(bottom, width=17, bd=3)
        actualE = Entry(bottom, width=17, bd=3)

        # Making Button

        doit = Button(bottom, text="Calculate", padx=50, pady=10, command= lambda: an1.pdilution(float(goalE.get()), float(totalE.get()), float(actualE.get())))

        #Object placement

        goall.grid(row=0, column=0, sticky=W)
        totall.grid(row=1, column=0, sticky=W)
        actuall.grid(row=2, column=0, sticky=W)
        goalE.grid(row=0, column=1)
        totalE.grid(row=1, column=1)
        actualE.grid(row=2, column=1)
        gel.grid(row=0, column=2)
        tel.grid(row=1, column=2)
        ael.grid(row=2, column=2)
        doit.grid(row=3, column=1, pady=10)

    elif value == "Mixed Dilution":

        # Make Labels

        highl = Label(bottom, text='High')
        lowl = Label(bottom, text='Low')
        massll = Label(bottom, text='Low Mass')
        wantedl = Label(bottom, text='Wanted')
        hel = Label(bottom, text='%')
        lel = Label(bottom, text='%')
        mel = Label(bottom, text='grams')
        wel = Label(bottom, text='%')

        # Make Entries

        highE = Entry(bottom, bd=3, width=17)
        lowE = Entry(bottom, bd=3, width=17)
        massE = Entry(bottom, bd=3, width=17)
        wantedE = Entry(bottom, bd=3, width=17)

        # Make Button

        doit = Button(bottom, text="Calculate", padx=50, pady=10, command= lambda: an2.dilution(float(lowE.get()), float(highE.get()), float(massE.get()), float(wantedE.get())))

        # Object Placement

        highl.grid(row=0, column=0, sticky=W)
        lowl.grid(row=1, column=0, sticky=W)
        massll.grid(row=2, column=0, sticky=W)
        wantedl.grid(row=3, column=0, sticky=W)
        highE.grid(row=0, column=1)
        lowE.grid(row=1, column=1)
        massE.grid(row=2, column=1)
        wantedE.grid(row=3, column=1)
        hel.grid(row=0, column=2)
        lel.grid(row=1, column=2)
        mel.grid(row=2, column=2)
        wel.grid(row=3, column=2)
        doit.grid(row=4, column=1, pady= 20)



root = Tk()
root.title('Common Calculations')
root.geometry("400x500")

backlevel = Frame(root, padx= 10, pady=10)
backlevel.pack(anchor=N, fill=BOTH, expand=True)


top = Frame(backlevel, relief=SUNKEN, bd=2)
top.pack(anchor=CENTER, fill=X, ipady = 10)

global bottom

bottom = Frame(backlevel)
bottom.pack(anchor= N)

global answer
answer = Label(bottom, text='')
answer.pack()

options = [
    "Piranha Analysis",
    "Pure Dilution",
    "Mixed Dilution"
]

var = StringVar()
var.set("Piranha Analysis")

drop = OptionMenu(top, var, *options)
drop.pack(anchor=CENTER, pady =10)

show = Button(top, text= "Show Calculation", padx= 10, pady= 5, command= lambda: bottomFrame(var.get()))
show.pack(anchor=CENTER)


root.mainloop()