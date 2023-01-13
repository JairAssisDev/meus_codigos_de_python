branco=[]
brancoN=[]
jair=[]
jairN=[]
aline=[]
alineN=[]
luiz=[]
luizN=[]
while True:
    print(""" 
                                     |--------------------------|
                                     |40=aline                  |
                                     |--------------------------|
                                     |22=jair                   |
                                     |--------------------------|           
                                     |13=luiz                   |
                                     |--------------------------|            
                                     |00=branco                 |
                                     |--------------------------|            
                                     
             """)
    h=str(input("qual seu nome"))         
    x=int(input("digite em quem vc quer votar "))
    if x==40:
        a=0
        a=a+1
        aline.append(a) 
        alineN.append(h)
        print("obg pelo seu voto ")
    elif x==22:
        c=0
        c=c+1
        jair.append(c)
        jairN.append(h) 
        print("obg pelo seu voto ")
    elif x==13:
        f=0
        f=f+1
        luiz.append(f) 
        luizN.append(h)
        print("obg pelo seu voto ")
    elif x==00:
        g=0
        g=g+1
        branco.append(g) 
        brancoN.append(h)
        print("obg pelo seu voto ")
    elif x==94111511:
        break
if jair>aline and jair>luiz:
    print("jair ganhou com",sum(jair),"votos")
    print("aline ficou com a quantidade de voto de",sum(aline))
    print("luiz ficou com a quantidade de voto de",sum(luiz))
    print("a quandidade de pessoas que votou branco foi ",sum(branco))
elif luiz>aline and luiz>jair:
    print("luiz ganhou com",sum(luiz),"votos")
    print("aline ficou com a quantidade de voto de",sum(aline))
    print("jair ficou com a quantidade de voto de",sum(jair))
    print("a quandidade de pessoas que votou branco foi ",sum(branco))
elif aline>jair and aline>luiz:
    print("aline ganhou com",sum(aline),"votos")
    print("jair ficou com a quantidade de voto de",jair)
    print("luiz ficou com a quandtidade de voto de",sum(luiz))
    print("a quandidade de pessoas que votou branco foi ",sum(branco))
while True:
    print("vc quer consutar os quem votol em cada candidato ")
    u=str(input("s =sim n=não"))
    if u=="s":
        print(jairN)
        print(alineN)
        print(luizN)
        print(brancoN)
    else:
        break
