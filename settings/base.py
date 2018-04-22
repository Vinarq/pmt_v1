#Do not turn debug mode on on production!
DEBUG=True
if DEBUG==True:
    from  settings import staging
    settings=staging
elif DEBUG==False:
    from settings import production
    print ("using production settings")
    settings=production
