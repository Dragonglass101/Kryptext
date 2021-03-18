def distribute():
    lst=[]
    with open(r'./messages/all_messages.txt','r') as lg:
        for msg in lg:
            count=0
            for i in lst:
                if(i==msg.split(" ")[2]):
                    count=1
                    break
            if(count==0):
                lst.append(msg.split(" ")[2])
    for i in lst:
        fname=i+"_messages.txt"
        with open(r'./messages/'+fname,'w') as indlg:
            indlg.write("This is your chat history with "+i+" :\n\n\n")
    with open(r'./messages/all_messages.txt','r') as lg:
        for msg in lg:
            fname=msg.split(" ")[2]+"_messages.txt"
            with open(r'./messages/'+fname,'a') as indlg:
                indlg.write(msg)
if(__name__ == "__main__"):
    distribute()