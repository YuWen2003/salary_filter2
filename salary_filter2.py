salary=[]
 
for i in range(0,8):
    ss=int(input())
    if ss>=155:
        if ss>1000:
            ss=ss//2;
        salary.append(ss)
 
print(salary)