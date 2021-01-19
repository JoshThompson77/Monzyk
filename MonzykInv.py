from tkinter import *
import sqlite3
from tkinter import ttk

def orderReport():
    rwin = Toplevel()
    rwin.title('Order List')

    # Connect to Database
    conn = sqlite3.connect("MonzykInv.db")

    # Make a Cursor
    c = conn.cursor()

    # Select items from table in SQL database
    c.execute("SELECT *, oid FROM Orderstatus")
    records = c.fetchall()

    #Create Treeview for report
    myTree = ttk.Treeview(rwin, height=15)

    style = ttk.Style()

    style.theme_use('default')

    # Setting columns for Treeview
    myTree['columns'] = ('barcode', 'name', 'amount', 'lowreorder')

    # Setting column dimensions in Treeview
    myTree.column('#0', width=0, stretch=0)
    myTree.column('barcode', anchor=W, width=140)
    myTree.column('name', anchor=W, width=140)
    myTree.column('amount', anchor=E, width=70)
    myTree.column('lowreorder', anchor=E, width=70)

    # Treeview headings
    myTree.heading('#0', text='')
    myTree.heading('barcode', text='Barcode', anchor=CENTER)
    myTree.heading('name', text='Name', anchor=CENTER)
    myTree.heading('amount', text='Amount', anchor=CENTER)
    myTree.heading('lowreorder', text='Low Inv', anchor=CENTER)

    # Determine if any inventory is low and needs more to be ordered

    for i in range(len(records)):
        if records[i][2] <= records[i][3]:
            myTree.insert(parent='',index='end', iid= i, text='', values=(records[i][0], records[i][1], records[i][2], records[i][3]))

    # Putting Treeview in window

    myTree.pack(pady= 15, padx=15)

    # Save Changes
    conn.commit()

    # Close connection
    conn.close()


def plusInven(barry, number):
    global barcodeE, amountE

    # Connect to Database
    conn = sqlite3.connect("MonzykInv.db")

    # Make a Cursor
    c = conn.cursor()

    # Adds Number to amount in database
    c.execute('''UPDATE Orderstatus SET amount = amount + ?  WHERE barcode=?''', (number, barry))

    # Save Changes
    conn.commit()

    # Close connection
    conn.close()

    # Clearing Entries
    barcodeE.delete(0, END)
    amountE.delete(0, END)



def minusInven(barry, number):
    # Connect to Database
    conn = sqlite3.connect("MonzykInv.db")

    # Make a Cursor
    c = conn.cursor()

    # Subtracts Number to amount in database
    c.execute('''UPDATE orderstatus SET amount = amount - ?  WHERE barcode=?''', (number, barry))

    # Save Changes
    conn.commit()

    # Close connection
    conn.close()

    # Clearing Entries
    barcodeE.delete(0, END)
    amountE.delete(0, END)



def deleteInv(barcode):

    global barcodeE
    # Connect to Database
    conn = sqlite3.connect("MonzykInv.db")

    # Make a Cursor
    c = conn.cursor()

    # Subtracts Number to amount in database
    c.execute('''DELETE FROM Orderstatus WHERE barcode=?''', (barcode,))

    # Save Changes
    conn.commit()

    # Close connection
    conn.close()

    # Clearing Entries
    barcodeE.delete(0, END)


def viewInventory():
    # Opening New Window
    inwin = Toplevel()
    inwin.geometry("600x400")
    inwin.title("Full Inventory")

    conn = sqlite3.connect("MonzykInv.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM Orderstatus")
    records = c.fetchall()

    # Making Treeview to easily view inventory
    myTree =ttk.Treeview(inwin, height=15)

    style = ttk.Style()

    style.theme_use('default')

    myTree['columns'] = ('barcode', 'name', 'amount', 'lowreorder')

    # Setting Treeview columns

    myTree.column('#0', width=0, stretch=0)
    myTree.column('barcode', width=120, anchor=W)
    myTree.column('name', width=120, anchor=W)
    myTree.column('amount', width=120, anchor=E)
    myTree.column('lowreorder', width=120, anchor=E)

    # Setting headings for the treeview

    myTree.heading('#0', text='')
    myTree.heading('barcode', text='Barcode', anchor=CENTER)
    myTree.heading('name', text='Name', anchor=CENTER)
    myTree.heading('amount', text='Amount', anchor=CENTER)
    myTree.heading('lowreorder', text='Low Reorder', anchor=CENTER)

    for i in range(len(records)):
        myTree.insert(parent='', index='end', iid=i, values=(records[i][0], records[i][1], records[i][2], records[i][3]))

    myTree.pack(pady= 10)

    conn.commit()
    conn.close()

def addNewItem():
    conn = sqlite3.connect("MonzykInv.db")

    c = conn.cursor()

    sql = "INSERT INTO Orderstatus (barcode, name, amount, low_reorder) VALUES (:barcode, :name, :amount, :lowreorder)"
    val = (barcodeE.get(), nameE.get(), amountE.get(), lowamountE.get())

    try:
        c.execute(sql, val)

    except:
        error = Toplevel()
        error.geometry("300x50")
        mylabel = Label(error, text= "This item already exists")
        mylabel.pack()


    conn.commit()
    conn.close()

    barcodeE.delete(0,END)
    nameE.delete(0, END)
    amountE.delete(0, END)
    lowamountE.delete(0, END)

def addNewItem2(barcode, name, amount, low):
    global barcodeE, nameE, amountE, lowamountE
    conn = sqlite3.connect("MonzykInv.db")

    c = conn.cursor()

    sql = "INSERT INTO Orderstatus (barcode, name, amount, low_reorder) VALUES (:barcode, :name, :amount, :lowreorder)"
    val = (barcode, name, amount, low)

    try:
        c.execute(sql, val)

    except:
        error = Toplevel()
        error.geometry("300x50")
        mylabel = Label(error, text="This item already exists")
        mylabel.pack()


    conn.commit()
    conn.close()

    barcodeE.delete(0, END)
    nameE.delete(0, END)
    amountE.delete(0, END)
    lowamountE.delete(0, END)


def bottomFrameLook(value):

    global action, barcodeE, amountE, nameE, lowamountE

    # Destroy the  existing bottom frame
    action.destroy()
    action = Frame(backlevel, pady=10, relief=RAISED, bd=2)
    action.pack(anchor=S, fill=BOTH, expand=True)

    # Determines how the new bottom Frame Action will build

    # Adding New Item to Inventory
    if value == 0:

        # Making Entries

        barcodeE = Entry(action, width= 17, borderwidth= 3)
        nameE = Entry(action, width =17, borderwidth= 3)
        amountE = Entry(action, width =17, borderwidth= 3)
        lowamountE = Entry(action, width =17, borderwidth= 3)

        # Making Labels for Entries

        barcodel = Label(action, text= 'Barcode', padx= 20)
        namel = Label(action, text= 'Name', padx= 20)
        amountl = Label(action, text= 'Amount', padx= 20)
        lowamountl =Label(action, text= 'Low reorder', padx= 20)

        # Making Buttons

        nextitem = Button(action, text= "Next Item", padx = 50, pady= 10, command= lambda: addNewItem2(barcodeE.get(), nameE.get(), amountE.get(), lowamountE.get()))

        #Object Placements

        barcodel.grid(row=0, column=0, sticky= W)
        namel.grid(row=1, column=0, sticky= W)
        amountl.grid(row=2, column=0, sticky= W)
        lowamountl.grid(row=3, column=0, sticky= W)

        barcodeE.grid(row=0, column=1)
        nameE.grid(row=1, column=1)
        amountE.grid(row=2, column=1)
        lowamountE.grid(row=3, column=1)

        nextitem.grid(row=4, column=1)

    # Add more to existing inventory item

    elif value == 1:

        # Making Entries

        barcodeE = Entry(action, width= 17, borderwidth= 3)
        amountE = Entry(action, width=17, borderwidth= 3)

        # Button

        nextitem = Button(action, text="Next Item", padx=50, pady=10, command= lambda: plusInven(barcodeE.get(), amountE.get()))

        # Making Labels

        barcodel = Label(action, text='Barcode', padx=20)
        amountl = Label(action, text='Amount', padx=20)

        # Object Placement

        barcodeE.grid(row=0, column=1)
        amountE.grid(row=1, column=1)
        barcodel.grid(row=0, column= 0)
        amountl.grid(row=1, column=0)
        nextitem.grid(row=2, column= 1)

    # Decrease from existing inventory

    elif value == 2:
        # Making Entries

        barcodeE = Entry(action, width=17, borderwidth=3)
        amountE = Entry(action, width=17, borderwidth=3)

        # Button

        nextitem = Button(action, text="Next Item", padx=50, pady=10, command= lambda: minusInven(barcodeE.get(), amountE.get()))

        # Making Labels

        barcodel = Label(action, text='Barcode', padx=20)
        amountl = Label(action, text='Amount', padx=20)

        # Object Placement

        barcodeE.grid(row=0, column=1)
        amountE.grid(row=1, column=1)
        barcodel.grid(row=0, column=0)
        amountl.grid(row=1, column=0)
        nextitem.grid(row=2, column=1)

    # Delete Completely From Inventory

    elif value == 3:

        # Making Entries

        barcodeE = Entry(action, width=17, borderwidth=3)

        # Button

        nextitem = Button(action, text="Next Item", padx=50, pady=10, command= lambda: deleteInv(barcodeE.get()))

        # Making Labels

        barcodel = Label(action, text='Barcode', padx=20)

        # Object Placement

        barcodeE.grid(row=0, column=1)
        barcodel.grid(row=0, column=0)
        nextitem.grid(row=1, column=1)

root = Tk()
root.title('Monzyk Innovations Chemical Inventory')
root.geometry("400x425")

conn = sqlite3.connect("MonzykInv.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS orderstatus (
        barcode text unique, 
        name text, 
        amount integer,
        low_reorder integer
        )""" )



# Window Frame

backlevel = Frame(root, padx= 5, pady = 5)
backlevel.pack( anchor = N, fill= BOTH, expand= True)

# Frame Top

selector = Frame(backlevel, bd = 2, relief= SUNKEN, pady= 25, padx = 110)
selector.pack(anchor= N, fill= BOTH, expand= True)

# Build Radio Buttons

var = IntVar()

newItem = Radiobutton(selector, text= 'New Item', variable = var, value= 0, command= lambda: bottomFrameLook(var.get()))
addMore = Radiobutton(selector, text= 'Add Number',variable = var, value= 1, command= lambda: bottomFrameLook(var.get()))
decItem = Radiobutton(selector, text= 'Decrease Number', variable= var, value= 2, command= lambda: bottomFrameLook(var.get()))
remove = Radiobutton(selector, text= 'Erase from Inventory', variable= var, value= 3, command= lambda: bottomFrameLook(var.get()))

# Button

viewinv = Button(selector, text = "View Inventory", padx =20, pady= 10, command= viewInventory)
report = Button(selector, text='Order Report', padx =25, pady=10, command=orderReport)
# Place Radio Buttons

newItem.pack(anchor= W)
addMore.pack(anchor= W)
decItem.pack(anchor= W)
remove.pack(anchor= W)
viewinv.pack(anchor=W)
report.pack(anchor=W)

# Bottom Frame when program first opened

global action
action = Frame(backlevel, relief= RAISED, bd=2, pady= 10)
action.pack(anchor= CENTER, fill= BOTH, expand= True)

barcodeE = Entry(action, width=17, borderwidth=3)
nameE = Entry(action, width=17, borderwidth=3)
amountE = Entry(action, width=17, borderwidth=3)
lowamountE = Entry(action, width=17, borderwidth=3)

# Making Labels for Entries
barcodel = Label(action, text='Barcode', padx=20)
namel = Label(action, text='Name', padx=20)
amountl = Label(action, text='Amount', padx=20)
lowamountl = Label(action, text='Low reorder', padx=20)

# Making Buttons
nextitem = Button(action, text="Next Item", padx=50, pady=10, command= addNewItem)

# Object Placements
barcodel.grid(row=0, column=0, sticky=W)
namel.grid(row=1, column=0, sticky=W)
amountl.grid(row=2, column=0, sticky=W)
lowamountl.grid(row=3, column=0, sticky=W)

barcodeE.grid(row=0, column=1)
nameE.grid(row=1, column=1)
amountE.grid(row=2, column=1)
lowamountE.grid(row=3, column=1)

nextitem.grid(row=4, column=1)

conn.commit()
conn.close()

root.mainloop()






