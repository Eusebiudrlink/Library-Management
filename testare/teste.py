from domain.entitati import Carte,Client,Imprumut
from bussines.services import ServiceCarti,ServiceClienti,ServiceImprumut
from infrastracture.Carti import RepoCarti
from infrastracture.Clienti import RepoClienti
from infrastracture.Imprumuturi import RepoImprumut
from validation.validator import ValidatorCarte,ValidatorClient,ValidatorImprumut
from erori.exceptii import ValidationError,RepoError


class Teste(object):
    
    def __run_creeaza_carte_test(self):
      #  print("start creeaza carte test...")
        id_carte = 23
        titlu = "Harry"
        descriere = "returnare"
        autor = "Sadoveanu"
        
        carte = Carte(id_carte,titlu,descriere,autor,0)
        
        assert(id_carte == carte.get_id_carte())
        assert(titlu == carte.get_titlu())
        assert(descriere == carte.get_descriere())
        assert(autor == carte.get_autor())
       # print("finish creeaza carte test...")
        
    def __run_creeaza_client_test(self):
      #  print("start creeaza client test...")
        id_client=12
        nume = "Felix"
        cnp = 5020202562457
        
        client = Client(id_client,nume,cnp,0)
        
        assert( client.get_id_client() == id_client)
        assert( client.get_cnp() == cnp)
        assert( client.get_nume() == nume)
        
       # print("finish creeaza client test...")
        
    def __run_adauga_carte_succes(self,srv_carti,id_carte,titlu,descriere,autor):
        assert(srv_carti.no_of_carti() == 0)
        srv_carti.adauga_carte(id_carte,titlu,descriere,autor)
        assert(srv_carti.no_of_carti() == 1)
        
    def __run_adauga_carte_insucces_id_invalid(self,srv_carti,id_carte,titlu,descriere,autor):
        try:
            srv_carti.adauga_carte(id_carte,titlu,descriere,autor)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id invalid!")
            
    def __run_adauga_carte_insucces_all_bad(self,srv_carti,id_carte,titlu,descriere,autor):
        try:
            srv_carti.adauga_carte(id_carte,titlu,descriere,autor)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id invalid!titlu invalid!descriere invalida!autor invalid!")
            
    def __run_adauga_carte_insucces_id_existent(self,srv_carti,id_carte,titlu,descriere,autor):
        try:
            srv_carti.adauga_carte(id_carte,titlu,descriere,autor)
            assert(False)
        except RepoError as re:
            assert(str(re) == "id existent!")

    def __run_adauga_carte_test(self):
       # print("start adauga carte test...")
        id_carte = 1
        titlu = "Minte de milionar"
        descriere = "returnare"
        autor = "Waren Buffet"
        bad_id_carte=-5
        bad_titlu = ""
        bad_descriere = ""
        bad_autor = ""
        valid_carte = ValidatorCarte()
        repo_carti = RepoCarti()
        srv_carti = ServiceCarti(valid_carte, repo_carti)
        
        self.__run_adauga_carte_succes(srv_carti,id_carte,titlu,descriere,autor)
        self.__run_adauga_carte_insucces_id_invalid(srv_carti,bad_id_carte,titlu,descriere,autor)
        self.__run_adauga_carte_insucces_all_bad(srv_carti, bad_id_carte, bad_titlu, bad_descriere, bad_autor)
        self.__run_adauga_carte_insucces_id_existent(srv_carti,id_carte,titlu,descriere,autor)
      #  print("finish adauga carte test")
      
        
    def __run_adauga_client_succes(self,srv_clienti,id_client,nume,cnp):
        assert(srv_clienti.no_of_clienti() == 0)
        srv_clienti.adauga_client(id_client,nume,cnp)
        assert(srv_clienti.no_of_clienti() == 1)
        
    def __run_adauga_client_insucces_id_invalid(self,srv_clienti,id_client,nume,cnp):
        try:
            srv_clienti.adauga_client(id_client,nume,cnp)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id invalid!")
            
    def __run_adauga_client_insucces_all_bad(self,srv_clienti,id_client,nume,cnp):
        try:
            srv_clienti.adauga_client(id_client,nume,cnp)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id invalid!nume invalid!cnp invalid!")
            
    def __run_adauga_client_insucces_id_existent(self,srv_clienti,id_client,nume,cnp):
        try:
            srv_clienti.adauga_client(id_client,nume,cnp)
            assert(False)
        except RepoError as re:
            assert(str(re) == "id existent!")

    def __run_adauga_client_test(self):
       # print("start adauga client test...")
        id_client = 1
        nume= "john"
        cnp = 2301526565213
        bad_id_client=-5
        bad_nume = ""
        bad_cnp = -5
        valid_client = ValidatorClient()
        repo_clienti = RepoClienti()
        srv_clienti = ServiceClienti(valid_client, repo_clienti)
        
        self.__run_adauga_client_succes(srv_clienti,id_client,nume,cnp)
        self.__run_adauga_client_insucces_id_invalid(srv_clienti,bad_id_client,nume,cnp)
        self.__run_adauga_client_insucces_all_bad(srv_clienti, bad_id_client, bad_nume, bad_cnp)
        self.__run_adauga_client_insucces_id_existent(srv_clienti,id_client,nume,cnp)
      #  print("finish adauga client test")
            
        
        
    def __run_valideza_carte(self):
        id_carte = 12
        id_invalid=-1
        titlu = "Colt Alb"
        titlu_invalid=""
        descriere = "exista"
        autor = "Eminescu"
        autor_invalid = ""
        carte=Carte(id_carte,titlu,descriere,autor,0)
        carte_all_invalid = Carte(id_invalid,titlu_invalid,descriere,autor_invalid,0)
        valid_carte= ValidatorCarte()
        valid_carte.valideaza(carte)
        try:
            valid_carte.valideaza(carte_all_invalid)
        except ValidationError as ve:
            assert(str(ve) == "id invalid!titlu invalid!autor invalid!")
    def __run_valideaza_client(self):
        id_client=2
        nume = "Ramona"
        cnp=5020612525654
        id_invalid=-1
        nume_invalid = ""
        cnp_invalid = -5264515114334
        
        valid_client=ValidatorClient()
        client=Client(id_client,nume,cnp,0)
        valid_client.valideaza(client)
        client_invalid=Client(id_invalid,nume_invalid,cnp_invalid,0)
        
        try:
            valid_client.valideaza(client_invalid)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id invalid!nume invalid!cnp invalid!")

    
    def __run_repo_carte_test(self):
        id_carte = 1
        titlu = "Fratii Karamazov"
        descriere ="nu"
        autor = "Dostoiveski"
        carte = Carte(id_carte,titlu,descriere,autor,0)
        repo_carti=RepoCarti()
        assert(len(repo_carti)==0)
        repo_carti.adauga_carte_lista(carte)
        assert(len(repo_carti)==1)
        try:
             repo_carti.adauga_carte_lista(carte)
             assert(False)
        except RepoError as re:
            assert(str(re) == "id existent!")
        assert(len(repo_carti)==1)
            
        
        
        
    
    def __run_repo_clienti_test(self):
        id_client = 8
        nume ="vasile"
        cnp = 1021524311211
        repo_clienti=RepoClienti()
        client=Client(id_client,nume,cnp,0)
        assert(len(repo_clienti)==0)
        repo_clienti.adauga_client_lista(client)
        assert(len(repo_clienti)==1)
        try:
             repo_clienti.adauga_client_lista(client)
             assert(False)
        except RepoError as re:
            assert(str(re) == "id existent!")
        assert(len(repo_clienti)==1)
            
            
    
    def __run_srv_adauga_imprumut_test(self):
        
        
        id_imp=10
        id_carte=1
        id_carte_inexistent=2
        id_client=5
        id_client_inexistent=6
        data="10/15/2002"
        bad_id_imp=-1
        bad_data=""
        
        valid_carte=ValidatorCarte()
        valid_client=ValidatorClient()
        valid=ValidatorImprumut()
        repo_carte=RepoCarti()
        repo_client=RepoClienti()
        repo = RepoImprumut()
        srv_carti=ServiceCarti(valid_carte,repo_carte)
        srv_clienti=ServiceClienti(valid_client,repo_client)
        srv_imp = ServiceImprumut(valid,repo,repo_carte,repo_client)
        
        srv_carti.adauga_carte(id_carte, "ursul", "feroce", "Bear GRILS")
        srv_clienti.adauga_client(id_client, "george", 2154515165)
        try:
            srv_imp.adauga_imprumut(id_imp,id_carte_inexistent,id_client_inexistent,data)
            assert(False)
        except Exception as ex:
            assert(str(ex) == "id carte inexistent!id client inexistent!")
        
        srv_imp.adauga_imprumut(id_imp,id_carte,id_client,data)
        
        try:
            srv_imp.adauga_imprumut(id_imp,id_carte,id_client,data)
        except RepoError as re:
            assert(str(re) == "id imprumut existent!")
               
        try:
            srv_imp.adauga_imprumut(bad_id_imp,id_carte,id_client,bad_data)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id imprumut invalid!data invalida!")
        
        
    
    def __run_repo_imprumut_test(self):
        id_imp=10
        id_carte=1
        id_client=5
        data="10/15/2002"
        
      
        repo = RepoImprumut()
        
        imprumut=Imprumut(id_imp,id_carte,id_client,data)
        
        repo.adauga_imprumut_lista(imprumut)
     
        try:
            repo.adauga_imprumut_lista(imprumut)
            assert(False)
        except RepoError as re:
            assert(str(re) == "id imprumut existent!")
        

    def __run_valideaza_imprumut_test(self):
        id_imp=10
        id_carte=1
        id_client=5
        data="10/15/2002"
        bad_id_imp=-1
        bad_data=""
        
        valid=ValidatorImprumut()
        imprumut=Imprumut(id_imp,id_carte,id_client,data)
        valid.Valideaza(imprumut)
        imprumut=Imprumut(bad_id_imp,id_carte,id_client,bad_data)
        try:
            valid.Valideaza(imprumut)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id imprumut invalid!data invalida!")
            
    def __run_rap_dupa_nume_test(self):
        valid_carte=ValidatorCarte()
     
        valid_imp=ValidatorImprumut()
        valid_client=ValidatorClient()
        
        repo_clienti=RepoClienti()
        repo_carti=RepoCarti()
        repo_imp=RepoImprumut()
        
        srvclient=ServiceClienti(valid_client,repo_clienti)
        srvcarte=ServiceCarti(valid_carte,repo_carti)
        srvimp=ServiceImprumut(valid_imp,repo_imp,repo_carti,repo_clienti)
        
        srvclient.adauga_client(1, "ana", 450)
        srvclient.adauga_client(2,"george",12)
        srvclient.adauga_client(3,"bogdan",56410)
        
        srvcarte.adauga_carte(1, "Colt", "fictiune", "Creanga")
        
        srvimp.adauga_imprumut(1,1,1,1)
        srvimp.adauga_imprumut(2,1,2,1)
        srvimp.adauga_imprumut(3,1,3,1)
        lista_nume=srvclient.rap_dupa_nume()
        assert(lista_nume[0]=="ana")
        assert(lista_nume[1]=="bogdan")
        assert(lista_nume[2]=="george")
        
      
        

    def __run_rap_dupa_cnp_test(self):
        valid=ValidatorClient()
        repo=RepoClienti()
        srv=ServiceClienti(valid,repo)
        srv.adauga_client(1, "ana", 450)
        srv.adauga_client(2,"george",12)
        srv.adauga_client(3,"alex",56410)
        clienti=srv.rap_dupa_cnp()
        assert(clienti[0].get_cnp()==56410)
        assert(clienti[1].get_cnp()==450)
        assert(clienti[2].get_cnp()==12)
    
    
    
    def run_all_teste(self):
        print("start teste")
        self.__run_creeaza_carte_test()
        self.__run_valideza_carte()
        self.__run_adauga_carte_test()
        self.__run_repo_carte_test()
        self.__run_adauga_client_test()
        self.__run_valideaza_client()
        self.__run_creeaza_client_test() 
        self.__run_repo_clienti_test()
        self.__run_repo_imprumut_test()
        self.__run_valideaza_imprumut_test()
        self.__run_rap_dupa_nume_test()
        self.__run_rap_dupa_cnp_test()
        
        
        
        print("finish teste")


