from datetime import *
from module1 import *
while True:
    ik=input("Isikukood: ")
    if len(ik)==11:
        try:
            ik_list=list(ik)
            if int(ik_list[0]) in [1,2,3,4,5,6]:
                if int(ik_list[0]) in [1,2]:
                    a=1800
                elif int(ik_list[0]) in [2,3]:
                    a=1900
                else:
                    a=2000
                aasta=a+int(ik_list[1]+ik_list[2])
                kuu=int(ik_list[3]+ik_list[4])
                paev=int(ik_list[5]+ik_list[6])
                if datetime(aasta,kuu,paev):
                    vastus=Kontroll(ik)
                ik3=int(ik[7:10])
                if ik>1 and ik3<=10:
                    haigla="Kuressaare Haigla"
                elif ik3>10 and ik3<=19:
                    haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
                elif ik3>21 and ik3<=220:
                    haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
                elif ik3>221 and ik3<=270:
                    haihla=" Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
                elif ik3>270 and ik3<=370:
                    haihla=" Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
                elif ik3>371 and ik3<=420:
                    haihla=" Narva Haigla"
                elif ik3>421 and ik3<=470:
                    haihla=" Pärnu Haigla"
                elif ik3>471 and ik3<=490:
                    haihla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
                elif ik3>491 and ik3<=520:
                    haihla="Järvamaa Haigla (Paide)"
                elif ik3>521 and ik3<=570:
                    haihla="Rakvere, Tapa haigla"
                elif ik3>571 and ik3<=600:
                    haihla="Valga Haigla"
                elif ik3>601 and ik3<=650:
                    haihla="Viljandi Haigla"
                elif ik3>651 and ik3<=700:
                    haihla="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
                else:
                    print("viga")


            else:
                print("esimene sumbol/arv on vale")
        except:
            print("admetuup on vale, on vaja numbreid sisestada")
    else:
        print("sumbolite arv peab 11 olema")
