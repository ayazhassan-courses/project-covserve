def update(G, num):
    for i in G:
        if G[i][0][1] == num:
            global u
            del G[i]
            u = Label(m, text = 'Re-enter information to get things updated')
            global L1
            global L2
            global L3
            global L4
            global L5
            global L7
            L2 = Label(m, text = 'Enter name:')
            L2.grid(row = 3)
            L3 = Label(m, text = 'Enter Area:')
            L3.grid(row = 4)
            L4 = Label(m, text = 'Enter Number:')
            L4.grid(row = 5)
            L7 = Label(m, text = 'Enter Email: ')
            L7.grid(row = 6)
            M = Label(m, text = " Enter Number in format +92 XXX XXXXXXX")
            M.grid(row = 15)
    global a
    global b
    global c
    global d
    global r
    a = Entry(m)
    b = Entry(m)
    c = Entry(m)
    d = Entry(m)
    r = Entry(m)
    a.grid(row = 2, column = 1)
    b.grid(row = 3, column = 1)
    c.grid(row = 4, column = 1)
    d.grid(row = 5, column = 1)
    r.grid(row = 6, column = 1)
    global bt2
    bt2 = Button(m, text = 'Save', width = 10, command = savedetails)
    bt2.grid(row = 7)


            