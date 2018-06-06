def move(n,frm,to,inter):
    if n == 1:
        print(("Move disc {} from {} to {}").format(n,frm,to))
    else :
        move(n-1,frm,inter,to)
        print(('Move disc {} from {} to {} ').format(n,frm,to))
        move(n-1,inter,to,frm)

move(1,'A','C','B')
