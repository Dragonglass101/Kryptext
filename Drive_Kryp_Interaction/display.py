def distribute():
    lst=[]
    with open('logs.txt','r') as lg:
        for msg in lg:
            count=0
            for i in lst:
                if(i==msg.split(" ")[2]):
                    count=1
                    break
            if(count==0):
                lst.append(msg.split(" ")[2])
    for i in lst:
        fname=i+"_logs.txt"
        with open(fname,'w') as indlg:
            indlg.write("This is your chat history with "+i+" :\n\n\n")
    with open('logs.txt','r') as lg:
        for msg in lg:
            fname=msg.split(" ")[2]+"_logs.txt"
            with open(fname,'a') as indlg:
                indlg.write(msg)
if(__name__ == "__main__"):
    distribute()