file = open("C:\\Users\\я\\eclipse-workspace\\workspace\\Parsing_Investing_Information\\src\\main\\dataForCriptoNeyroStudy.txt","r")
data = file.read().split("\n")[::-1]
file.close()
res = ""
inp = ""
outp = ""
for i in range(0,len(data)-10):
    outp+=str(float(data[i])*(1/3500)-(2/7))+";"
    for j in range(i+1, i+11):
        inp+=str(data[j])+","
    inp = inp[:-1]
    inp+= ";"
inp = inp[:-1]
inp = inp[:-1]
outp = outp[:-1]
res+= inp + "_" + outp
file = open("C:\\Users\\я\\eclipse-workspace\\workspace\\Parsing_Investing_Information\\src\\main\\dataForCriptoNeyroStudyConverted.txt","w")
file.write(res)
file.close()
