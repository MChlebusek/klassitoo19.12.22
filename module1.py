def Kontroll(isikukood:str):
    """Isikukoodi kontroll number
    On vaja isikukood sisestada
    :param str ik: Inimese isikukood
    :rtype: var Märamata tüüp
    """

    ik_list=list(isikukood)
    s=0
    for i in range(0,10):
        s+=(i%9+1)*int(ik_list[i])
        print(f"{i%9}*{int(ik_list[1])}+", end="")
    print(s)
    s=s-(s//11)*11
    print(s)
    if s==int(ik_list[10]):
        print("ok")
    else:
        print("mette ok")
