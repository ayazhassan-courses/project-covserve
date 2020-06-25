from tkinter import *

import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

m = Tk()
m.geometry("600x600")
m.title("COVServe Shop")
pic = PhotoImage(file = 'logo.png')
pic = pic.subsample(3,3)
global L
L = Label(m, image = pic)
L.grid()
chck = False
def save_dict_to_file(dic):
    f = open('dict.txt','w')
    f.write(str(dic))
    f.close()
    Label(m, text = 'Your Services have been added/updated.').grid()

def load_dict_from_file():
    f = open('dict.txt','r')
    data=f.read()
    f.close()
    return eval(data)

def send_email(email, mes): 
    message_template = mes

    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login('covserve@outlook.com', '$eRV!ngs0c!etY')

    msg = MIMEMultipart()      

    message = message_template
    print(message)

    msg['From']='covserve@outlook.com'
    msg['To']=email
    msg['Subject']="RECIEPT"

    msg.attach(MIMEText(message, 'plain'))
    
    s.send_message(msg)
    del msg

    s.quit()

def AddProd(Data = [], details = []):
    if chck == True: 
        bt10.destroy()
    L1.destroy()
    L2.destroy()
    L3.destroy()
    L4.destroy()
    L5.destroy()
    L7.destroy()
    a.destroy()
    b.destroy()
    c.destroy()
    d.destroy()
    r.destroy()
    
    global L10
    L10 = Label(m, text = 'Add Product')
    L10.grid(row = 23)
    global x
    x = Entry(m)
    x.grid(row = 23, column = 1)
    if Data != []:
        global L12
        L12 = Label(m, text = 'Add Price')
        L12.grid(row = 24)
        global y
        y = Entry(m)
        y.grid(row = 24, column = 1)
    global bt5
    bt5 = Button(m, text = 'Save', command = lambda : SavProd(Data, details))
    bt5.grid(row = 25)
credit = 0
   
def SavProd(Data, details):
    if credit == 10: 
        bt5.destroy()
        L10.destroy()
        x.destroy()
        print('here 1')
        return
    p = x.get()
    if Data != [] :
        q = y.get() 
        if len(Data[details[0]][1]) == 0:
            Data[details[0]][1].append((p,q))
        else:
            for i in range(len(Data[details[0]][1])):
                if p[0] < Data[details[0]][1][i][0][0]:
                    Data[details[0]][1].insert(i, (p,q))
                    break
                    
                elif i == len(Data[details[0]][1])-1:
                    Data[details[0]][1].insert(i, (p,q))
    else:
        pds.append(x.get())
def addCredit():
    global credit
    credit+=10  
    print('here 0')  

def IfDistributor(details):
    if chck == True:
        L1.destroy()
        L2.destroy()
        L3.destroy()
        L4.destroy()
        L5.destroy()
        L7.destroy()
        a.destroy()
        b.destroy()
        c.destroy()
        d.destroy()
        r.destroy()
        bt2.destroy()
    bt9.destroy()
    L13.destroy()
    L14.destroy()
    L15.destroy()
    L16.destroy()
    L17.destroy()
    aa.destroy()
    bb.destroy()
    cc.destroy()
    dd.destroy()
    Data = load_dict_from_file()
    Data[details[0]] = [[details[1], details[2], details[3]], []]
    global bt4
    bt4 = Button(m, text = 'Add Product?', command = lambda : AddProd(Data, details))
    bt4.grid(row = 7)
    global bt6
    bt6 = Button(m, text = 'Done', command = lambda:save_dict_to_file(Data))
    bt6.grid(row = 7, column = 3)
    bt10.destroy()

def dele():
    #print('ok')
    no.destroy()
def yeschek(val):
    #print('1')
    global L21
    no.destroy()
    print('here')
    L21 = Button(m, text = 'Thank you!', command = lambda:dele())
    L21.grid(row = 25)

def getAddress(G, di, details, pds):
    #print('hello')
    if credit == 10:
        '''bt5.destroy()
        L10.destroy()
        x.destroy()
        global L10'''
        global L20
        global no 
        global Ent
        L20 = Label(m, text = 'Have you recieved Products?')
        L20.grid(row = 23)
        no = Button(m, text = 'Your order is placed. Will be delivered soon', command = lambda:addCredit())
        no.grid(row = 25)
        Ent = Entry(m)
        Ent.grid(row = 23, column = 1)
        val = Ent.get()
        but = Button(m, text = 'Done', command = lambda:yeschek(val)) 
        but.grid(row = 25, column = 1)

    bt7.destroy()
    bt8.destroy()
    L9.destroy()
    L11 = Label(m, text = "Your Address : ")
    L11.grid(row = 0)
    global v
    v = Entry(m)
    v.grid(row = 0, column = 1)
    bt9 = Button(m, text = 'Proceed to Billing!', command = lambda : generatebill(G, di, details, pds))
    bt9.grid(row = 1)

def generatebill(G, di, details, pds):
    receipt = []
    z = []
    for j in pds:
        #print('j', j)
        flag = False
        for k in di:
            #print('k', k)
            for i in G[k][1]:
                #print('i', i)
                if i[0] == j:
                    #print('matched', z)
                    if i not in receipt:
                        receipt.append(i)
                        flag = True
                        z += [0]
                    else: z[receipt.index(i)] += 1
                    break
            if flag == True: break
        

        if flag == False:
            print(j, 'is not available')
    #print('r', receipt, 'z', z)
    for k in di:
        print(k)
        message0 = 'Prepare order for ' + details[0] + ' Number = ' + details[2] + " Address: " + v.get() + ' email : ' + details[3]
        send_email(G[k][0][2], message0)
    total = 0
    message = ''
    message += ('COVServe Shop \n')
    message += ('Customer name : ' + details[0] + '\n')
    message += ('Product           Price(Per Product)          Quantity\n')
    for i in range(len(receipt)):
        print(str(receipt[i][0]), str(receipt[i][1]), str(z[i]))
        message += (str(receipt[i][0]) + " "*(23-len(receipt[i][0])) + str(receipt[i][1])+ " "*(26+len(receipt[i][0])) + str(z[i])+"\n")
        total += int(receipt[i][1])*int(z[i])
        print(total)
    message += ('-------------------------------------- \n')
    message += ('Total           ' + str(total) + '\n')
    message += 'Thank You for shopping with us! Your order will be delivered in half an hour. \n Regards, \n COVServe Team'
    send_email(details[3], message)

def merging(freqlist, L, M, H):
    temp = []
    for i in range(0, H+1):
        temp.append(freqlist[i])
    i = L
    k = L
    j = M + 1
    while i <= M and j <= H:
        if int(temp[i][1]) <= int(temp[j][1]):
            freqlist[k] = temp[i]
            i += 1
        else:
            freqlist[k] = temp[j]
            j += 1
        k += 1
    
    while i <= M:
        freqlist[k] = temp[i]
        i += 1
        k += 1
    while j <= H:
        freqlist[k] = temp[j]
        j += 1
        k += 1
    return freqlist

def merge(freqlist, L, H):
    if L < H:
        M = int((L+H)/2)
        merge(freqlist, L, M)
        merge(freqlist, M+1 , H)
        merging(freqlist, L, M, H)
    return freqlist     

def IfCustomer(G, details):
    bt9.destroy()
    L13.destroy()
    L14.destroy()
    L15.destroy()
    L16.destroy()
    L17.destroy()
    aa.destroy()
    bb.destroy()
    cc.destroy()
    dd.destroy()
    st = ''
    lst = []
    global pds
    pds = []
    global di
    di = []
    dist = list(G.keys())
    for i in dist:
        if (G[i][0][0]) == details[1]:
            for j in G[i][1]:
                if j not in lst:
                    lst += [j]
                    di.append(i)
    lst = merge(lst, 0, len(lst)-1)
    for i in lst:
        st += (str(i)+ ", ")
    global L9
    L9 = Label(m, text = 'Products : ' + st[0:len(st)-2]) 
    L9.grid(row=11)
    
    global bt7
    bt7 = Button(m ,text = 'Add Product?', command = lambda : AddProd())
    bt7.grid(row = 12)
    global bt8
    Data = load_dict_from_file()
    bt8 = Button(m ,text = 'Done', command = lambda :[addCredit(), SavProd(Data, details), getAddress(G, di, details, pds)])
    bt8.grid(row = 12, column = 1)
    
def ask(x, y, z, q, h):
    L1.destroy()
    L2.destroy()
    L3.destroy()
    L4.destroy()
    L5.destroy()
    L7.destroy()
    a.destroy()
    b.destroy()
    c.destroy()
    d.destroy()
    r.destroy()
    bt2.destroy()
    bt3.destroy()
    nest = [y, z, q, h]
    f = open('dict.txt','r')
    data=f.read()
    f.close()
    if len(q) == 15 and q[3] == q[7] == " " and q[0] =="+":
        if x == "a" or x == "custumer":
            IfCustomer(eval(data), nest)
        elif x == "b" or x == "distributer":
            IfDistributor(nest)
    else: print("Invalid number.") 

def savedetails():
    x = a.get()
    y = b.get()
    z = c.get()
    q = d.get()
    h = r.get()
    global bt3 
    bt3 = Button(m, text = 'Proceed', width = 10, command = lambda: ask(x,y,z,q,h))
    bt3.grid(row = 7)

def savedetails1():
    global chck
    chck = True
    x = aa.get()
    y = bb.get()
    z = cc.get()
    q = dd.get()
    f = open('dict.txt','r')
    data=f.read()
    f.close()
    Data = eval(data)
    G = Data.keys()
    for i in G:
        if Data[i][0][1] == z:
            #print("hello")
            del Data[i]
            break
    f = open('dict.txt','w')
    f.write(str(Data))
    f.close()
    nest = [x, y, z, q]
    global bt10 
    bt10 = Button(m, text = 'Proceed', width = 10, command = lambda: IfDistributor(nest))
    bt10.grid(row = 22)

def signin():
    L.destroy()
    global L1
    global L2
    global L3
    global L4
    global L5
    global L7
    bt1.destroy()
    L5 = Label(m, text = "SignUp", font = ("Arial Bold", 10), justify = CENTER)
    L5.grid(row = 1)
    L1 = Label(m, text = 'Are you (a) costumer or (b) distributor?')
    L1.grid(row = 2)
    L2 = Label(m, text = 'Enter name:')
    L2.grid(row = 3)
    L3 = Label(m, text = 'Enter Area:')
    L3.grid(row = 4)
    L4 = Label(m, text = 'Enter Number:')
    L4.grid(row = 5)
    L7 = Label(m, text = 'Enter Email: ')
    L7.grid(row = 6)
    M = Label(m, text = " Enter Number in format +92 XXX XXXXXXX. Bill or ordered placed is sent via email.")
    M.grid(row = 15)
    G = load_dict_from_file()
    s = "Service available in :" 
    f = list(G.keys())
    for i in f:
        if G[i][0][0] not in s:
            s += G[i][0][0] + " "
    M2 = Label(m,text = s)
    M2.grid(row = 16)
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

def update():
    global L13
    global L14
    global L15
    global L16
    global L17
    L13 = Label(m, text = "Update information (For Distributors)", font = ("Arial Bold", 10), justify = CENTER)
    L13.grid(row = 17)
    L14 = Label(m, text = 'Enter name:')
    L14.grid(row = 18)
    L15 = Label(m, text = 'Enter Area:')
    L15.grid(row = 19)
    L16 = Label(m, text = 'Enter Number:')
    L16.grid(row = 20)
    L17 = Label(m, text = 'Enter Email: ')
    L17.grid(row = 21)
    global aa
    global bb
    global cc
    global dd
    aa = Entry(m)
    bb = Entry(m)
    cc = Entry(m)
    dd = Entry(m)
    aa.grid(row = 18, column = 1)
    bb.grid(row = 19, column = 1)
    cc.grid(row = 20, column = 1)
    dd.grid(row = 21, column = 1)
    global bt9
    bt9 = Button(m, text = 'Save', width = 10, command = savedetails1)
    bt9.grid(row = 22)
    
bt1 = Button(m, text = 'Start', width = 10, command= lambda:[signin(), update()])
bt1.grid(row = 1)
mainloop()