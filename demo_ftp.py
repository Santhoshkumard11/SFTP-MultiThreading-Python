import pysftp


server_host = "demo.wftpserver.com"
username = "demo"
password = "demo"

with pysftp.Connection(server_host, username=username, password=password,port=2222)as sftp:


    print(sftp.pwd)

    # with sftp.cd('public'):             # temporarily chdir to public

    # sftp.put('/my/local/filename')  # upload file to public/ on remote

    # sftp.get('remote_file')         # get a remote file
    