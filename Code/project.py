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

def save_dict_to_file(dic):
    f = open('dict.txt','w')
    f.write(str(dic))
    f.close()
    Label(m, text = 'Your Services have been added.').grid()

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
    global L10
    L10 = Label(m, text = 'Add Product')
    L10.grid(row = 8)
    global x
    x = Entry(m)
    x.grid(row = 8, column = 1)
    if Data != []:
        global L12
        L12 = Label(m, text = 'Add Price')
        L12.grid(row = 9)
        global y
        y = Entry(m)
        y.grid(row = 9, column = 1)
    global bt5
    bt5 = Button(m, text = 'Save', command = lambda : SavProd(Data, details))
    bt5.grid(row = 10)
    
    
def SavProd(Data, details):
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

def IfDistributor(details):
    Data = load_dict_from_file()
    Data[details[0]] = [[details[1], details[2], details[3]], []]
    global bt4
    bt4 = Button(m, text = 'Add Product?', command = lambda : AddProd(Data, details))
    bt4.grid(row = 7)
    global bt6
    bt6 = Button(m, text = 'Done', command = lambda: save_dict_to_file(Data))
    bt6.grid(row = 7, column = 3)

def getAddress(G, di, details, pds):
    bt5.destroy()
    bt7.destroy()
    bt8.destroy()
    L9.destroy()
    L10.destroy()
    x.destroy()
    L11 = Label(m, text = "Your Address : ")
    L11.grid(row = 0)
    global v
    v = Entry(m)
    v.grid(row = 0, column = 1)
    bt9 = Button(m, text = 'Proceed to Biling!', command = lambda : generatebill(G, di, details, pds))
    bt9.grid(row = 1)

def generatebill(G, di, details, pds):
    receipt = []
    for j in pds:
        flag = False
        for k in di:
            for i in G[k][1]:
                if i[0] == j:
                    receipt.append(i)
                    flag = True
                    break
            break
        
        if flag == False:
            print(j, 'is not available')
    for k in di:
        message0 = 'Prepare order for ' + details[0] + ' Number = ' + details[2] + " Address: " + v.get() + ' email : ' + details[3]
        send_email(G[k][0][2], message0)
    total = 0
    message = ''
    message += ('COVServe Shop \n')
    message += ('Customer name : ' + details[0] + '\n')
    message += ('Product     Price \n')
    for i in receipt:
        message += (i[0] + "      " + i[1]+ " \n")
        total += int(i[1])
    message += ('--------------- \n')
    message += ('Total       ' + str(total) + '\n')
    message += 'Thank You for shopping with us! \n Regards, \n COVServe Team'
    send_email(details[3], message)
        

def IfCustomer(G, details):
    st = ''
    global pds
    pds = []
    global di
    di = []
    dist = list(G.keys())
    for i in dist:
        if (G[i][0][0]) == details[1]:
            st += str(G[i][1])
            di.append(i)
            
    global L9
    L9 = Label(m, text = 'Products : ' + st) 
    L9.grid(row=11)
    global bt7
    bt7 = Button(m ,text = 'Add Product?', command = lambda : AddProd())
    bt7.grid(row = 12)
    global bt8
    bt8 = Button(m ,text = 'Done', command = lambda : getAddress(G, di, details, pds))
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
    M = Label(m, text = " Enter Number in format +92 XXX XXXXXXX")
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
    
bt1 = Button(m, text = 'Start', width = 10, command= signin)
bt1.grid(row = 1)
mainloop()