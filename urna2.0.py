branco=[]
jair=[]
aline=[]
luiz=[]
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
    x=int(input("digite em quem vc quer votar "))
    if x==40:
        a=0
        a=a+1
        aline.append(a) 
        print("obg pelo seu voto ")
    elif x==22:
        c=0
        c=c+1
        jair.append(c) 
        print("obg pelo seu voto ")
    elif x==13:
        f=0
        f=f+1
        luiz.append(f) 
        print("obg pelo seu voto ")
    elif x==00:
        g=0
        g=g+1
        branco.append(g) 
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

