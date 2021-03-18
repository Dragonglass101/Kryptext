def distribute(): #Used to distribute the messages in all_messages.txt into individual chat logs
    lst=[]
    with open(r'./messages/all_messages.txt','r') as lg:
        for msg in lg: #Iterates over the messages in all_messages.txt
            count=0
            for i in lst:
                if(i==msg.split(" ")[2]):
                    count=1
                    break
            if(count==0):
                lst.append(msg.split(" ")[2]) #Here lst becomes a list of the different usernames present in all_messages.txt
    for i in lst: #Iterating over the usernames in lst
        fname=i+"_messages.txt" #Creates a unique chat log file corresponding to each username in all_messages.txt
        with open(r'./messages/'+fname,'w') as indlg:
            indlg.write("This is your chat history with "+i+" :\n\n\n") #Gives a heading to each such unique file

    #Extracting the username from a message in all_messages.txt and putting the message in that user's individual chat log file:
    with open(r'./messages/all_messages.txt','r') as lg:
        for msg in lg: 
            fname=msg.split(" ")[2]+"_messages.txt"
            with open(r'./messages/'+fname,'a') as indlg:
                indlg.write(msg)

if(__name__ == "__main__"):
    distribute()
