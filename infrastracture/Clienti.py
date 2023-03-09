'''
Created on Dec 2, 2021

@author: Eusebiu
'''
from erori.exceptii import RepoError
from domain.entitati import Carte,Client
class RepoClienti(object):
    
    
    def __init__(self):
        self._clienti = []
    def __len__(self):
        return len(self._clienti)
    
    def adauga_client_lista(self,client):
        #functie care adauga un client in lista existenta de clienti
        for i in self._clienti:
            if i.get_id_client() == client.get_id_client():
                raise RepoError("id existent!")
                return 0
        self._clienti.append(client)
    
    def get_all(self):
        return self._clienti
    def get_by_id(self,id_client): 
        for i in self._clienti:
            if i.get_id_client() == id_client:
                return i
        return -1
    def sterge_client(self,id_client):
        
        for i in range(len(self._clienti)):
            if self._clienti[i].get_id_client() == id_client:
                del self._clienti[i]
                return 0
        raise Exception("nu exista niciun client cu acest id!")
    
    def modifica_client(self,client):
        
        for i in self._clienti:
            if i.get_id_client()==client.get_id_client():
                i.set_nume(client.get_nume())
                i.set_cnp(client.get_cnp())
                i.set_inchirieri(client.get_inchirieri())
                return 0
            
        raise Exception("nu exista clientul cu acest id")
                

class ClientRepositoryFile(RepoClienti):
    def __init__(self,file_path):
        RepoClienti.__init__(self)
        self.__file_path = file_path
        
    def __read_all_clienti(self):
        with open(self.__file_path,"r") as f:
            self._clienti=[]
            lines = f.readlines()
            for line in lines:
                line=line.strip()
                if len(line)>0:
                    parts = line.split(",")
                    id_client=int(parts[0])
                    nume = parts[1]
                    cnp = parts[2]
                    inchirieri = int(parts[3])
                    client = Client(id_client,nume,cnp,inchirieri)
                    self._clienti.append(client)
    
    def __write_all_clienti(self):
        with open(self.__file_path,"w") as f:
            for client in self._clienti:
                f.write(f"{str(client.get_id_client())},{client.get_nume()},{str(client.get_cnp())},{str(client.get_inchirieri())}\n")
    def __append_client(self,client):
        with open(self.__file_path,"a") as f:
            f.write(f"{str(client.get_id_client())},{client.get_nume()},{str(client.get_cnp())},{str(client.get_inchirieri())}\n")
    
    def adauga_client_lista(self, client):
        self.__read_all_clienti()
        RepoClienti.adauga_client_lista(self, client)
        self.__append_client(client)
    def sterge_client(self, id_client):
        self.__read_all_clienti()
        RepoClienti.sterge_client(self, id_client)
        self.__write_all_clienti()
    def modifica_client(self, client):
        self.__read_all_clienti()
        RepoClienti.modifica_client(self, client)
        self.__write_all_clienti()
    def __len__(self):
        return RepoClienti.__len__(self)
    
    def get_all(self):
        self.__read_all_clienti()
        return RepoClienti.get_all(self)
    
    def get_by_id(self, id_client):
        self.__read_all_clienti()
        return RepoClienti.get_by_id(self, id_client)

