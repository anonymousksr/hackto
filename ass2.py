dict={}
f=open('C:/Users/Sarveswara Rao K/Documents/Dlithe/new.txt','a')
for i in range(1,11):
    name=input("Enter the Name of the candidate")
    degree=input("Enter the degree of the candidate")
    dict[name]=degree
    f.write(str(i)+") ""Name "+name+" Degree "+degree+"\n")
f.close()
print("The candidates are")
for a,b in dict.items():
    print(a,b)
