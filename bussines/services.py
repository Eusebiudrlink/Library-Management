from validation.validator import ValidatorCarte
from domain.entitati import Carte,Client,Imprumut
from erori.exceptii import ValidationError
import random
from bussines.sortari import Insertion_Sort, Comb_Sort

class ServiceCarti(object):
    
    
    def __init__(self, valid_carte, repo_carti):
        self.__valid_carte = valid_carte
        self.__repo_carti = repo_carti
    
    
    def no_of_carti(self):
        return len(self.__repo_carti)
    def adauga_carte(self,id_carte,titlu,descriere,autor):
        #functie care care creeaza,valideaza si adauga in lista de carti o carte
        carte = Carte(id_carte,titlu,descriere,autor,0)
        self.__valid_carte.valideaza(carte)
        self.__repo_carti.adauga_carte_lista(carte)
    def get_all_carti(self):
        return self.__repo_carti.get_all()
    def cauta_carte(self,titlu):
        carti=self.__repo_carti.get_all()
        for carte in carti:
            if carte.get_titlu() == titlu:
                return carte
        
        raise Exception("Carte inexistenta in biblioteca!")
    def modifica_carte(self,id_carte,titlu,descriere,autor):
        inchirieri = 0
        carte=Carte(id_carte,titlu,descriere,autor,inchirieri)
        self.__repo_carti.modifica_carte(carte)
        
    def rap_cele_mai_inchiriate(self):
        #functie care ordoneaza descrescator,dupa numarul de inchirieri, lista de carti
        carti=self.__repo_carti.get_all()
        """for i in range(len(carti)):
            for j in range(len(carti)):
                if carti[i].get_inchirieri() > carti[j].get_inchirieri():
                    aux=carti[j] 
                    carti[j]=carti[i]
                    carti[i]=aux """
        
        #carti.sort(key=lambda x: x.get_inchirieri(), reverse = True)
        sorteaza=Insertion_Sort()
        sorteaza.insertion_sort(carti, key=lambda x:  x.get_inchirieri(), reverse = True)
        
        return carti      
        
    def lungmax(self):
        carti=self.__repo_carti.get_all()
        lungmax=0
        for idx,carte in enumerate(carti):
            if len(carte.get_titlu()) > lungmax:
                lungmax = len(carte.get_titlu())
                cartemax = carte
        if lungmax > 0:
            return cartemax
        else:
            raise Exception("nu exista carti adaugate")
    def gencarti(self,nrcarti):
        # functie care genereaza un numar de  nrcarti noi cu valori random valide
        alfabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","u","r","z"]
        if nrcarti==0:
            return 0
        ok=0
        while ok==0:
            id_carte=random.randint(1,100)
            lungtitlu=random.randint(4,7)
            lungdescriere=random.randint(4,6)
            lungautor=random.randint(4,7)
            titlu=""
            descriere=""
            autor=""
            for i in range(lungtitlu):
                litera=random.choice(alfabet)
                titlu+=litera
            for i in range(lungdescriere):
                litera=random.choice(alfabet)
                descriere+=litera
            for i in range(lungautor):
                litera=random.choice(alfabet)
                autor+=litera
            carte = Carte(id_carte,titlu,descriere,autor,0)
            try:
                self.__valid_carte.valideaza(carte)
                self.__repo_carti.adauga_carte_lista(carte)
                ok=1  
            except Exception:
                ok=0 
        self.gencarti(nrcarti-1)
                    
                
class ServiceClienti(object):
    
    
    def __init__(self, valid_client, repo_clienti):
        self.__valid_client = valid_client
        self.__repo_clienti = repo_clienti
        
    def no_of_clienti(self):
        return len(self.__repo_clienti)
    def adauga_client(self,id_client,nume,cnp):
        #functie care care creeaza,valideaza si adauga in lista de clienti un client
        client=Client(id_client,nume,cnp,0)
        self.__valid_client.valideaza(client)
        self.__repo_clienti.adauga_client_lista(client)
    def get_all_clienti(self):
        return self.__repo_clienti.get_all()
    def cauta_client(self,nume):
        clienti = self.__repo_clienti.get_all()
        for client in clienti:
            if client.get_nume() == nume:
                return client
        
        raise Exception("Client inexistent in baza de date!")
    
    def modifica_client(self,id_client,nume,cnp):
        inchirieri=0
        client=Client(id_client,nume,cnp,inchirieri)
        self.__repo_clienti.modifica_client(client)
    
    def rap_dupa_nume(self):
        clienti=self.__repo_clienti.get_all()
        lista_nume=[]
        for i in range(len(clienti)):
            if clienti[i].get_inchirieri()>0:
                lista_nume.append(clienti[i].get_nume())
        sorteaza=Comb_Sort()
        sorteaza.CombSort(lista_nume) 
        return lista_nume
    def rap_dupa_nr_carti(self):
        clienti=self.__repo_clienti.get_all()
        sorter=Insertion_Sort()
        sorter.insertion_sort(clienti,key=lambda x: x.get_inchirieri(),reverse=True)
        return clienti     
    def rap_dupa_cnp(self):
        clienti=self.__repo_clienti.get_all() 
        clienti.sort(key=lambda x: x.get_cnp(), reverse = True)
        return clienti     
    def genclienti(self,nrclienti):
        # functie care genereaza un numar de  nrclienti noi cu valori random valide
        if nrclienti == 0:
            return 0
        else:
            alfabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","u","r","z"]
            ok=0
            while ok==0:
                id_client=random.randint(1,100)
                lungnume=random.randint(4,7)
                cnp=random.randint(3221134,214423332)
                nume=""
                
                for i in range(lungnume):
                    litera=random.choice(alfabet)
                    nume+=litera
                client= Client(id_client,nume,cnp,0)
                try:  
                    self.__valid_client.valideaza(client)
                    self.__repo_clienti.adauga_client_lista(client)
                    ok=1  
                except Exception as ex:
                    print(ex)
                    
        self.genclienti(nrclienti-1)
           
    def douacriterii(self):
        clienti=self.__repo_clienti.get_all()
        sorter=Insertion_Sort()
        sorter.insertion_sort(clienti, cmp = lambda a,b : a.get_nume()< b.get_nume() or
                               (a.get_nume() == b.get_nume() and a.get_inchirieri() < b.get_inchirieri()))
        return clienti

class ServiceImprumut(object):
    
    
    def __init__(self, valid_imprumut, repo_imprumut,repo_carti,repo_clienti):
        self.__valid_imprumut = valid_imprumut
        self.__repo_imprumut = repo_imprumut
        self.__repo_carti = repo_carti
        self.__repo_clienti = repo_clienti
        

    
    def adauga_imprumut(self, id_imp, id_carte, id_client, data):
        #functie care adauga in lista de imprumuturi un nou imprumut daca aceste este valid
        imprumut= Imprumut(id_imp, id_carte, id_client, data)
        self.__valid_imprumut.Valideaza(imprumut)
        erori=""
        x=0
        if self.__repo_carti.get_by_id(id_carte,x) == -1:
            erori+="id carte inexistent!"
        if self.__repo_clienti.get_by_id(id_client) == -1:
            erori+="id client inexistent!"
            print(erori)
        if len(erori)>0:
            raise Exception(erori)
        else:
            self.__repo_imprumut.adauga_imprumut_lista(imprumut)
            
            i=self.__repo_carti.get_by_id(id_carte,0)
            nr_inchirieri=i.get_inchirieri()+1
            i.set_inchirieri(nr_inchirieri)
            self.__repo_carti.modifica_carte(i)
                    
            i=self.__repo_clienti.get_by_id(id_client)
            nr_inchirieri=i.get_inchirieri()+1
            i.set_inchirieri(nr_inchirieri)
            self.__repo_clienti.modifica_client(i)
       
            
    
    def sterge_carte_srv(self,id_carte):
        self.__repo_carti.sterge_carte(id_carte)
        #self.__repo_imprumut.sterge_carte(id_carte)
    def sterge_client_srv(self,id_client):
        self.__repo_clienti.sterge_client(id_client)
        #self.__repo_imprumut.sterge_client(id_client)
        
    def sterge_imprumut(self,titlu,nume):
        id_carte=-1
        id_client=-1
        carti = self.__repo_carti.get_all()
        for i in carti:
            if i.get_titlu() == titlu:
                id_carte = i.get_id_carte()
                
        clienti=self.__repo_clienti.get_all()
        for j in clienti:
            if j.get_nume() == nume:
                id_client=j.get_id_client()
        print(id_carte,id_client)
        if id_carte !=-1 and id_client != -1:
            self.__repo_imprumut.sterge_imp(id_carte,id_client)
        else:
            raise Exception("Numele clientului sau titlul cartii este incorect")
        
    def genimprumuturi(self,nrimprumuturi):
        # functie care genereaza un numar de  nrcarti noi cu valori random valide
        
        for imprumuturi in range(nrimprumuturi):
            ok=0
            while ok==0:
                id_imprumut=random.randint(1,100)
                carti=self.__repo_carti.get_all()
                clienti=self.__repo_clienti.get_all()
                
                nrcarti=len(carti)-1
                nrclienti = len(clienti)-1
                
                i = random.randint(0,nrcarti-1)
                j = random.randint(0,nrclienti)
                
                id_carte = carti[i].get_id_carte()
                id_client=clienti[j].get_id_client()
                
                data=random.randint(1,30)
                
                imprumut = Imprumut(id_imprumut,id_carte,id_client,data)
                try:    
                    self.__valid_imprumut.Valideaza(imprumut)
                    self.__repo_imprumut.adauga_imprumut_lista(imprumut) 
                    
                    nrinchirieri=carti[i].get_inchirieri()+1
                    carti[i].set_inchirieri(nrinchirieri)
                    carte=carti[i]
                    self.__repo_carti.modifica_carte(carte)

                    client=clienti[j]
                    nrinchirieri=client.get_inchirieri()+1
                    client.set_inchirieri(nrinchirieri)
                    self.__repo_clienti.modifica_client(client)
                    
                    ok=1  
                except Exception as ex:
                    assert True 
                    ok=0
        
    def get_all_imprumuturi(self):
        return self.__repo_imprumut.get_all()
        
    
    



