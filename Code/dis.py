di = ['Mubashir', 'Kamran', 'Kamran', 'Salman']
f = open('dict.txt','r')
receipt = [('Gloves', '50'), ('N-95 Mask', '1000')]
z = [2, 1]
data=f.read()
f.close()
data = eval(data) 
def make_dist_list(di, data, receipt):
    dis = []
    ch = []
    for i in di:
        lst = []
        #print(i, data[i][1])
        for j in range(len(receipt)):
            #print(receipt[j]) 
            if receipt[j] in data[i][1] and receipt[j] not in ch:
                lst.append((receipt[j], z[j]))
                ch.append(receipt[j])
        if lst != []:dis.append((i, lst))
    for k in dis:
        print(k)
        message0 = 'Prepare order for ' + " Address: " +' email : '
        #print(k[1][0])
        #print(k[1][0][0][0])
        #print(k[1][0][1])
        if len(k) == 2: message0 += str(k[1][0][0][0]) + " in quantity " + str(k[1][0][1]) + "."
        else:
            for i in range(1, len(k)):
                if i != 1 and i == len(k) -1:
                    message0 += "and " + str(k[i][0][0][0]) + " in quantity " + str(k[i][0][1]) + "."
                else:
                    message0 += str(k[i][0][0]) + " in quantity " + str(k[i][0][1]) + ", "
        print(message0)            

print(make_dist_list(di, data, receipt))
