def Downloader(file,folder):
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

    gauth = GoogleAuth()

    # Try to load saved client credentials  #username_Pu_key    #Download_pukey
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
    folderlist=drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for fold in folderlist:
        if (fold['title']==folder):
            foldID=fold['id']
            break
    filelist=drive.ListFile({'q': "'"+foldID+"' in parents and trashed=false"}).GetList()
    for fil in filelist:
        if (fil['title']==file):
            fileID=fil['id']
            break
    file1 = drive.CreateFile({'id': fileID})
    file1.GetContentFile(file)
def Download_pukey(folder):
    Downloader('public_txt.txt',folder)
def Download_msg():
    from Drive_Kryp_Interaction import crypt_implement
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

    gauth = GoogleAuth()

    # Try to load saved client credentials  #username_Pu_key    #Download_pukey
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
    with open('sender.txt','r') as u:
        username=u.read()
    folderlist=drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    x=0
    for fold in folderlist:
        if (fold['title']==username+'_Received'):
            foldID=fold['id']
            x=1
            break
    if x==0:
        folder1= drive.CreateFile({'title' :username+'_Received', 'mimeType' : 'application/vnd.google-apps.folder'})
        folder1.Upload()
        foldID=folder1['id']
    filelist=drive.ListFile({'q': "'"+foldID+"' in parents and trashed=false"}).GetList()
    for fil in filelist:
        fileID=fil['id']
        file1 = drive.CreateFile({'id': fileID})
        file1.GetContentFile(fil['title'])
        file1.Delete()
        crypt_implement.Krypt().decrypt_message(fil['title'])