'''
Created on Dec 2, 2021

@author: Eusebiu
'''
from erori.exceptii import RepoError
from domain.entitati import Carte,Client

class RepoCarti(object):
    
    
    def __init__(self):
        self._carti = []
    def __len__(self):
        return len(self._carti)
    
    def adauga_carte_lista(self,carte):
        #functie care adauga o carte in lista existenta de carti
        for i in self._carti:
            if i.get_id_carte() == carte.get_id_carte():
                raise RepoError("id existent!")
                return 0
            
        self._carti.append(carte)
    
    def sterge_carte(self,id_carte):
        for i in range(len(self._carti)):
            if self._carti[i].get_id_carte() == id_carte:
                del self._carti[i]
                return 0
        raise Exception("Nu exista nicio carte cu acest id!")
    
    def modifica_carte(self,carte):
        
        for i in self._carti:
            if i.get_id_carte()==carte.get_id_carte():
                i.set_titlu(carte.get_titlu())
                i.set_descriere(carte.get_descriere())
                i.set_autor(carte.get_autor())
                i.set_inchirieri(carte.get_inchirieri())
                return 0
            
        raise Exception("nu exista cartea cu acest id")            
            
                
                
    def get_all(self):
        return self._carti
    def get_by_id(self,id_carte,ind):
       
        if  ind == len(self._carti):
            return -1
        elif self._carti[ind].get_id_carte() == id_carte:
            return self._carti[ind]
        else:
            return self.get_by_id(id_carte,ind+1)
        
class CarteRepositoryFile(RepoCarti):
    def __init__(self,file_path):
        RepoCarti.__init__(self)
        self.__file_path= file_path
        
    def __len__(self):
        return RepoCarti.__len__(self)
    def __read_all_from_file(self):
        with open(self.__file_path,"r") as f:
            self._carti=[]
            lines=f.readlines()
            for line in lines:
                line=line.strip()
                if len(line)>0:
                    parts = line.split(",")
                    id_carte = int(parts[0])
                    titlu = parts[1]
                    descriere = parts[2]
                    autor = parts[3]
                    inchirieri = int(parts[4])
                    carte=Carte(id_carte,titlu,descriere,autor,inchirieri)
                    self._carti.append(carte)
                    

                    
    
    def __write_all_to_file(self):
        with open(self.__file_path,"w")as f:
            for carte in self._carti:
                f.write(f"{str(carte.get_id_carte())},{carte.get_titlu()},{carte.get_descriere()},{carte.get_autor()},{str(carte.get_inchirieri())}\n")
               

    def __append_to_file(self,carte):
        with open(self.__file_path,"a") as f:
            f.write(f"{str(carte.get_id_carte())},{carte.get_titlu()},{carte.get_descriere()},{carte.get_autor()},{str(carte.get_inchirieri())}\n")

            
    def adauga_carte_lista(self,carte_noua):
        self.__read_all_from_file()
        RepoCarti.adauga_carte_lista(self, carte_noua)
        self.__append_to_file(carte_noua)
    def sterge_carte(self,id_carte):
        self.__read_all_from_file()
        RepoCarti.sterge_carte(self, id_carte)
        self.__write_all_to_file()
    def modifica_carte(self,carte):
        self.__read_all_from_file()
        RepoCarti.modifica_carte(self, carte)
        self.__write_all_to_file()
    def get_all(self):
        self.__read_all_from_file()
        return RepoCarti.get_all(self)
    def get_by_id(self,id_carte,ind):
        self.__read_all_from_file()
        return RepoCarti.get_by_id(self, id_carte,ind)
            