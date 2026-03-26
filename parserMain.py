from subprocess import check_output
from subprocess import CalledProcessError
res1 = ""
#res2 = ""


#       1 is include      but 2 isnt include
for j in range(1,13):
    for i in range(1,28):
        try:
            a=check_output("curl rate.sx/eth@" + str(i) + "."+str(j)+".2023", shell=True).decode("utf-8")
            a=a.split("[2m // [0m[2mend:")
            a = a[0].split("[2mbegin:[0m ")[1]
            a=a.split(" ")[0]
            a=a.replace("$","")
            res1 += a+ "\n"
            #b=check_output("curl rate.sx/alt@" + str(i) + "."+str(j)+".2024", shell=True).decode("utf-8")
            #b=b.split("[2m // [0m[2mend:[0m ")
            #b = b[0].split("[2mbegin:[0m ")[1]
            #b=b.split(" ")[0]
            #b=b.replace("$","")
            #res2 += b+ "\n"
            print(".")
        except IndexError:
            print(str(i)+ "   " + str(j) + " 2023")
        except CalledProcessError :
            print(str(i)+ "   " + str(j)+ " 2023")
    print("..")
    
for j in range(1,13):
    for i in range(1,28):
        try:
            a=check_output("curl rate.sx/eth@" + str(i) + "."+str(j)+".2024", shell=True).decode("utf-8")
            a=a.split("[2m // [0m[2mend:")
            a = a[0].split("[2mbegin:[0m ")[1]
            a=a.split(" ")[0]
            a=a.replace("$","")
            res1 += a+ "\n"
            #b=check_output("curl rate.sx/alt@" + str(i) + "."+str(j)+".2024", shell=True).decode("utf-8")
            #b=b.split("[2m // [0m[2mend:[0m ")
            #b = b[0].split("[2mbegin:[0m ")[1]
            #b=b.split(" ")[0]
            #b=b.replace("$","")
            #res2 += b+ "\n"
            print(".")
        except IndexError:
            print(str(i)+ "   " + str(j)+ " 2024")
        except CalledProcessError :
            print(str(i)+ "   " + str(j)+ " 2024")
    print("..")
file = open("C:\\Users\\я\\eclipse-workspace\\workspace\\Parsing_Investing_Information\\src\\main\\actions.txt" , "w")
#file.write("eth: " +"\n"+ res1+"alt: " +"\n" + res2)
file.write("eth: " +"\n"+ res1)
file.close()
print("finish")



