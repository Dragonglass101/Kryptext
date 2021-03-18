def user_add():
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

    gauth = GoogleAuth()

    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")

    if gauth.credentials is None:
        # Authenticate if they're not there

        # This is what solved the issues:
        gauth.GetFlow()
        gauth.flow.params.update({'access_type': 'offline'})
        gauth.flow.params.update({'approval_prompt': 'force'})

        gauth.LocalWebserverAuth()

    elif gauth.access_token_expired:

        # Refresh them if expired

        gauth.Refresh()
    else:

        # Initialize the saved creds

        gauth.Authorize()

    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)
    with open(r'./txtfiles/sender.txt','r') as u:
        username=u.read()
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    x=0
    for fold in fileList:
        if(fold['title']=='User_list'):
            foldID=fold['id']
            x=1
            break
    if x==0:
        folder1= drive.CreateFile({'title' :'User_list', 'mimeType' : 'application/vnd.google-apps.folder'})
        folder1.Upload()
        foldID=folder1['id']       
    file1=drive.CreateFile({'title': username+'.txt', 'parents': [{'id': foldID}]})
    file1.Upload()
    from Drive_Kryp_Interaction import crypt_implement
    crypt_implement.Krypt().generate()
def user_find():
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

    gauth = GoogleAuth()

    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")

    if gauth.credentials is None:
        # Authenticate if they're not there

        # This is what solved the issues:
        gauth.GetFlow()
        gauth.flow.params.update({'access_type': 'offline'})
        gauth.flow.params.update({'approval_prompt': 'force'})

        gauth.LocalWebserverAuth()

    elif gauth.access_token_expired:

        # Refresh them if expired

        gauth.Refresh()
    else:

        # Initialize the saved creds

        gauth.Authorize()

    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)
    with open(r'./txtfiles/recipient.txt','r') as rec:
        username=rec.readline()
    folderList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for fold in folderList:
        if(fold['title']=='User_list'):
            foldID=fold['id']
            break
    filelist=drive.ListFile({'q': "'"+foldID+"' in parents and trashed=false"}).GetList()
    y=0
    for fil in filelist:
        if (fil['title']==username+'.txt'):
            fileID=fil['id']
            y=1
            break
    if y==1:
        from Drive_Kryp_Interaction import crypt_implement
        return(crypt_implement.Krypt().encrypt_message())
    elif(y==0):
        import os
        os.remove(r'./txtfiles/message.txt')
        os.remove(r'./txtfiles/recipient.txt')
        return False