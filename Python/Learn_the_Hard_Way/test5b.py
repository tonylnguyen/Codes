
num = 346



units = {1:"one", 2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
teens = {1:'eleven',2:'tewlve',3:'thirteen',4:'forteen',5:'fithteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'ninteen'}
tens = {0:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninty'}
hundreds = {}

numStr = str(num)
u = int(numStr[-1])

def num2words(num):
    print "at1"
    ret = ''
    u = num % 10
    t = (num/10) % 10
    h = (num/100) % 10

    print "at2"
    if t == 1: #teens
        ret = units[h] + ' hundred ' + teens[u]
    else:
        ret = units[h] + ' hundred ' + teens[t]+ ' ' + units[u]
    print "at4"
    return ret, u ,t, h

print (num2words(num))
