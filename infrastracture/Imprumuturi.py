'''
Created on Dec 2, 2021

@author: Eusebiu
'''
from erori.exceptii import RepoError
from domain.entitati import Imprumut

class RepoImprumut(object):

    def __init__(self):
        self._imprumuturi = []
      
    def adauga_imprumut_lista(self, imprumut):
        #functie care adauga un imprumut in lista existenta de imprumuturi
        for i in self._imprumuturi:
            if i.get_id_imp()==imprumut.get_id_imp():
                raise RepoError("id imprumut existent!")
        
        self._imprumuturi.append(imprumut)
        
    
    
    def sterge_imp(self,id_carte,id_client):
        lista_noua=[]
        ok=0
        for i in self._imprumuturi:
            if i.get_id_carte()==id_carte:
                if i.get_id_client()==id_client:
                    ok=1
                else:
                    lista_noua.append(i)
            else:
                lista_noua.append(i)
        self._imprumuturi = lista_noua
        if ok==0:
            raise Exception("Titlul sau numele este incorect")
        
            
            
    def get_all(self):
        return self._imprumuturi
    def __len__(self):
        return len(self._imprumuturi)

class ImprumutRepositoryFile(RepoImprumut):
    
    def __init__(self,file_path):
        RepoImprumut.__init__(self)
        self.__file_path=file_path
        
    def __read_all_imprumuturi(self):
        with open(self.__file_path,"r") as f:
            lines = f.readlines()
            self._imprumuturi=[]
            for line in lines:
                line=line.strip()
                if len(line)>0:
                    parts = line.split(",")
                    id_imprumut = int(parts[0])
                    id_carte = int(parts[1])
                    id_client = int(parts[2])
                    data = parts[3]
                    imprumut = Imprumut(id_imprumut,id_carte,id_client,data)
                    self._imprumuturi.append(imprumut)
        
    
    def __write_all_imprumuturi(self):
        with open(self.__file_path,"w") as f:
            for imprumut in self._imprumuturi:
                f.write(f"{str(imprumut.get_id_imp())},{str(imprumut.get_id_carte())},{str(imprumut.get_id_client())},{str(imprumut.get_data())}\n")
    def __append_imprumut(self,imprumut):
        with open(self.__file_path,"a") as f:
            f.write(f"{str(imprumut.get_id_imp())},{str(imprumut.get_id_carte())},{str(imprumut.get_id_client())},{str(imprumut.get_data())}\n")
        
    def adauga_imprumut_lista(self, imprumut):
        self.__read_all_imprumuturi()
        RepoImprumut.adauga_imprumut_lista(self, imprumut)
        self.__append_imprumut(imprumut)
    def sterge_imp(self, id_carte, id_client):
        self.__read_all_imprumuturi()
        RepoImprumut.sterge_imp(self, id_carte, id_client)
        self.__write_all_imprumuturi()
    def get_all(self):
        self.__read_all_imprumuturi()
        return RepoImprumut.get_all(self)
    def __len__(self):
        return RepoImprumut.__len__(self)
        
        
        
