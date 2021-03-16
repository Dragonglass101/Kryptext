def Uploader(file,folder):
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
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    x=0
    for fold in fileList:
        if(fold['title'] ==folder):
            folderID = fold['id']
            x=1
            break
    if(x==0 and folder=='root'):
        folderID='root'
    elif(x==0):
        folder1= drive.CreateFile({'title' :folder, 'mimeType' : 'application/vnd.google-apps.folder'})
        folder1.Upload()
        folderID=folder1['id']
    file1=drive.CreateFile({'parents': [{'id': folderID}]})
    file1.SetContentFile(file)
    file1.Upload()