from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
import os
from datetime import datetime
class Krypt:
    def __init__(self):
        pass
    def generate(self):     #Called by user_add(). Creates the public and private keys for the user.
        from Drive_Kryp_Interaction import up_cloud
        with open(r'./txtfiles/sender.txt','r') as u:
            person=u.read()
        #Generating private key (RsaKey object) of key length of 2048 bits
        private_key = RSA.generate(4096)
        #Generating the public key (RsaKey object) from the private key
        public_key = private_key.publickey()
        #Converting the RsaKey objects to string
        private_txt = private_key.export_key().decode()
        public_txt = public_key.export_key().decode()
        #Writing down the private and public keys to '.txt' files
        with open(r'./txtfiles/private_txt.txt','w') as pr:
            pr.write(private_txt)
        with open(r'./txtfiles/public_txt.txt','w') as pu:
            pu.write(public_txt)
        up_cloud.Uploader("public_txt.txt",(person+'_Pu_key')) #Using the Uploader()
        os.remove(r"./txtfiles/public_txt.txt")     #removing the public key stored locally
    def encrypt_message(self):      # Called by user_find(), Encrypts the message to be sent present in message.txt,. Reads, encrypts and passes it on to Uploader()
        from Drive_Kryp_Interaction import up_cloud
        with open(r'./txtfiles/sender.txt','r') as u:
            sender=u.readline()
        with open(r'./txtfiles/message.txt','r') as mes: #Check if message can be sent like:Sender : Recipient : <The message>
            message=mes.readline()
        with open(r'./txtfiles/recipient.txt','r') as rec:
            recipient=rec.readline()
        now = datetime.now() # datetime object containing current date and time
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # format of date and time is dd/mm/YY H:M:S
        Text=sender+' : '+message+' : '+dt_string   # Sender and Recipient information appended to the message
        os.remove(r"./txtfiles/message.txt")
        os.remove(r'./txtfiles/recipient.txt')
        # Call Download_pukey() to get public key of recipient and converting it to the RsaKey object
        from Drive_Kryp_Interaction import down_cloud
        down_cloud.Download_pukey((recipient+"_Pu_key")) #Using the Download_pukey()
        with open(r'./txtfiles/public_txt.txt','r') as putxt:
            pu_key = RSA.import_key(putxt.read())
        os.remove(r"./txtfiles/public_txt.txt")
        #Instantiating PKCS1_OAEP object with the public key for encryption
        cipher = PKCS1_OAEP.new(key=pu_key)
        #Encrypting the message with the PKCS1_OAEP object
        cipher_text = cipher.encrypt(Text.encode())
        fname11="encrypted_"+(dt_string.split(" ")[0].split("/")[0])+(dt_string.split(" ")[0].split("/")[1])+(dt_string.split(" ")[0].split("/")[2])+(dt_string.split(" ")[1])+".txt"
        with open(r"./txtfiles/"+fname11,'wb') as enc:
            enc.write(cipher_text)
        up_cloud.Uploader(fname11,(recipient+"_Received")) #Using the Uploader() to upload encrypted message to Drive
        os.remove(r"./txtfiles/"+fname11)
        log_message="Sent to "+recipient+" on "+dt_string+" =>  "+message+"\n"
        with open(r'./messages/all_messages.txt','a') as l:
            l.write(log_message)    #Storing the non-encrypted message locally in all_messages.txt
        from Drive_Kryp_Interaction import display      #Distributing messages into individual logs
        display.distribute()
        return True     #returning boolean  True in order to display a success message on web page
    def split_dt_string(self,dt_string):        #Used to split a date time string into its individual parts
        dt_lst1=dt_string.split(" ")
        time_lst=(dt_lst1[1]).split(":")
        date_lst=(dt_lst1[0]).split("/")
        dt_lst2=[]
        for i in range(3):
            dt_lst2.append(int(date_lst[i]))
        for i in range(3):                  
            dt_lst2.append(int(time_lst[i]))
        return dt_lst2      #Returns a list containing the individual parts
    def time_delay(self,dt_sent,dt_received):       #Used to calculate the difference between two date time strings
        dt_sent_lst=self.split_dt_string(dt_sent)
        dt_received_lst=self.split_dt_string(dt_received)
        dt_delay=[]
        delay=[]
        for i in range(6):
            dt_delay.append(dt_received_lst[i]-dt_sent_lst[i])
        if(dt_delay[5]>0):
            delay.append(str(round(dt_delay[5],2))+" sec")
        else:
            dt_delay[4]=dt_delay[4]+(dt_delay[5]/60)
        if(dt_delay[4]>0):
            if((dt_delay[4]-int(dt_delay[4]))>0):
                delay.append(str(round((dt_delay[4]-int(dt_delay[4]))*60,2))+" sec")     
            if(int(dt_delay[4])>0):
                delay.append(str(round(int(dt_delay[4]),2))+" mins")          
        else:     
            dt_delay[3]=dt_delay[3]+(dt_delay[4]/60)            
        if(dt_delay[3]>0):        
            if((dt_delay[3]-int(dt_delay[3]))>0):   
                delay.append(str(round((dt_delay[3]-int(dt_delay[3]))*60,2))+" mins")     
            if(int(dt_delay[3])>0):   
                delay.append(str(round(int(dt_delay[3]),2))+" hrs")   
        else:    
            dt_delay[0]=dt_delay[0]+(dt_delay[3]/24)
        if(dt_delay[0]>0):                          
            if((dt_delay[0]-int(dt_delay[0]))>0):   
                delay.append(str(round((dt_delay[0]-int(dt_delay[0]))*24,2))+" hrs")    
            if(int(dt_delay[0])>0): 
                delay.append(str(round(int(dt_delay[0]),2))+" days")   
        else:
            dt_delay[1]=dt_delay[1]+(dt_delay[0]/30)
        if(dt_delay[1]>0):                          
            if((dt_delay[1]-int(dt_delay[1]))>0):    
                delay.append(str(round((dt_delay[1]-int(dt_delay[1]))*30,2))+" days")    
            if(int(dt_delay[1])>0):   
                delay.append(str(round(int(dt_delay[1]),2))+" months")   
        else:    
            dt_delay[2]=dt_delay[2]+(dt_delay[1]/12)                          
        if((dt_delay[2]-int(dt_delay[2]))>0):   
            delay.append(str(round((dt_delay[2]-int(dt_delay[2]))*12,2))+" months") 
        if(int(dt_delay[2])>0):
            delay.append(str(round(int(dt_delay[2]),2))+" years")
        delay_final=" sent this message "
        for i in range(len(delay)):
            j=len(delay)-i-1
            delay_final=delay_final+delay[j]+" "
        delay_final=delay_final+"\bago"
        return delay_final
    def decrypt_message(self,fname1):       # Called by Download_msg(), Used to decrypt the  message
        with open(fname1,'rb') as enc1:
            encrypted_message=enc1.read()   #Obtains the encrypted message from the Download_msg()
        os.remove(fname1)
        with open(r'./txtfiles/private_txt.txt','r') as prtxt:
            pr_key = RSA.import_key(prtxt.read())       #The recipient's private key is needed for decryption
        #Instantiating PKCS1_OAEP object with the private key for decryption
        decrypt = PKCS1_OAEP.new(key=pr_key)
        #Decrypting the message with the PKCS1_OAEP object
        decrypted_message = (decrypt.decrypt(encrypted_message)).decode()       #decrypting
        #Separating and storing the padded information from the, padded decrypted message:
        lt=decrypted_message.split(' : ',1)
        msg_false=lt[1]
        sender=lt[0]
        lt3=msg_false.rsplit(' : ',1)
        msg=lt3[0]
        dts=lt3[1]
        now1 = datetime.now() # datetime object containing current date and time
        dt_string1 = now1.strftime("%d/%m/%Y %H:%M:%S") # format of date and time is dd/mm/YY H:M:S
        tags="    ..."+'('+sender+self.time_delay(dts,dt_string1)+')'
        if(dts==dt_string1):       #Checks if there is no delay
            tags=""     #tags is empty if there is no delay
        log_message1="Received from "+sender+" on "+dt_string1+" =>  "+msg+tags+"\n"    
        with open(r'./messages/all_messages.txt','a') as lg:
            lg.write(log_message1)  #Storing the decrypted message locally in all_messages.txt
        from Drive_Kryp_Interaction import display
        display.distribute()    #Distributing messages into individual logs
