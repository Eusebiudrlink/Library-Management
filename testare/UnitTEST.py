'''
Created on Dec 2, 2021

@author: Eusebiu
'''
import unittest
from validation.validator import ValidatorCarte, ValidatorClient, ValidatorImprumut
from bussines.services import ServiceCarti
from infrastracture.Carti import RepoCarti, CarteRepositoryFile
from erori.exceptii import ValidationError,DuplicatedIdException
from domain.entitati import Carte, Client, Imprumut
from infrastracture.Clienti import RepoClienti,ClientRepositoryFile
from _ast import With
from infrastracture.Imprumuturi import RepoImprumut
from bussines.sortari import Insertion_Sort,Comb_Sort
import random
from encodings.punycode import insertion_sort

class TestCaseCarte(unittest.TestCase):
    
    def test_Create_Carte(self):
        #####test creare carte
       
        carte = Carte(2,"Harry","returnare","Factor",0)
        
        self.assertEqual(carte.get_id_carte(),2)
        self.assertEqual(carte.get_titlu(),"Harry")
        self.assertEqual(carte.get_descriere(),"returnare")
        self.assertEqual(carte.get_autor(),"Factor")
        
        
    def test_validare_carte(self):
        
        carte = Carte(2,"Harry","returnare","Factor",0)
        
        valid = ValidatorCarte()
        valid.valideaza(carte)
        
        carte_invalida= Carte(-1,"","","",0)
        
        with self.assertRaises(Exception) as ex:
            valid.valideaza(carte_invalida)
        
        self.assertEqual(str(ex.exception),"id invalid!titlu invalid!descriere invalida!autor invalid!")
        
    
    def test_adauga_carte(self):
        repo=RepoCarti()
        
        self.assertEqual(repo.__len__(),0)
        carte = Carte(3,"Harry","returnare","Factor",0)
        repo.adauga_carte_lista(carte)
        self.assertEqual(repo.__len__(),1)
        
        with self.assertRaises(Exception) as ex:
            repo.adauga_carte_lista(carte)
        
        self.assertEqual(str(ex.exception), "id existent!")
      
    def test_get_by_id(self):
        path="test_file_carti.txt"
        repo=CarteRepositoryFile(path)
        id_carte=2
        carte_cautata=repo.get_by_id(id_carte,0)
        carte=Carte(2,"mere","multe","creanga",0)
        assert(carte == carte_cautata)
        id_gresit=10
        carte_gresita=repo.get_by_id(id_gresit,0)
        assert(carte_gresita == -1)
        
    
    def test_sterge_carte(self):
        
        repo=RepoCarti()
        
        carte = Carte(1,"Harry","returnare","Factor",0)
        repo.adauga_carte_lista(carte)
        carte = Carte(2,"jack","inchiriat","da",0)
        repo.adauga_carte_lista(carte)
        
        repo.sterge_carte(1)
        
        carti = repo.get_all()
        self.assertEqual(carti[0], carte)

      
        
          
class TestCaseClient(unittest.TestCase): 
     
    def test_create_client(self):
        
        client =Client(1,"stefan",562154,0)
        
        self.assertEqual(client.get_id_client(),1)
        self.assertEqual(client.get_nume(),"stefan")
        self.assertEqual(client.get_cnp(),562154)
        self.assertEqual(client.get_inchirieri(),0)
     
    def test_validare_client(self):
        client = Client(1,"stefan",562154,0)
        
        valid = ValidatorClient()
        valid.valideaza(client)
        
        client_invalid = Client(-1,"",-1,0)
        
        with self.assertRaises(Exception) as ex:
            valid.valideaza(client_invalid)
        
        self.assertEqual(str(ex.exception),"id invalid!nume invalid!cnp invalid!")   
        
    def test_adauga_client(self):
        repo = RepoClienti()
        
        self.assertEqual(repo.__len__(),0)
        client = Client(1,"stefan",562154,0)
        repo.adauga_client_lista(client)
        self.assertEqual(repo.__len__(),1)
        
        with self.assertRaises(Exception) as ex:
            repo.adauga_client_lista(client)
            
        self.assertEqual(str(ex.exception),"id existent!")
    
    def test_get_by_id(self):
        repo = ClientRepositoryFile("test_file_clienti.txt")
        
        id_client=16
        client_cautat=repo.get_by_id(id_client)
        client=Client(16,"pipu",170571416,0)
        assert(client == client_cautat)
      
        id_gresit=15
        client_gresit=repo.get_by_id(id_gresit)
        assert(client_gresit ==-1)
        
        
        
        
        
    
class TestCaseImprumut(unittest.TestCase):
    def test_create_imprumut(self):
        imprumut = Imprumut(1,1,1,"23")
        
        self.assertEqual(imprumut.get_id_imp(),1)
        self.assertEqual(imprumut.get_id_carte(),1)
        self.assertEqual(imprumut.get_id_client(),1)
        self.assertEqual(imprumut.get_data(),"23")
        
    def test_validare_imprumut(self):
        
        
        imprumut = Imprumut(1,1,1,"23")
        
        valid = ValidatorImprumut()
        valid.Valideaza(imprumut)
        
        imprumut_invalid = Imprumut(-1,1,1,"")
        
        with self.assertRaises(Exception) as ex:
            valid.Valideaza(imprumut_invalid)
            
        self.assertEqual(str(ex.exception), "id imprumut invalid!data invalida!" )
        
        
    def test_adauga_imprumut(self):
        repo = RepoImprumut()
        
        self.assertEqual(repo.__len__(), 0)
        imprumut = Imprumut(1,1,1,"23")
        repo.adauga_imprumut_lista(imprumut)
        self.assertEqual(repo.__len__(), 1)
        
        with self.assertRaises(Exception) as ex:
            repo.adauga_imprumut_lista(imprumut)
        self.assertEqual(str(ex.exception),"id imprumut existent!")

class TestSortari(unittest.TestCase):

    
    def __insertion_sort_test(self, sorter):
        values = [0,1,2,3,4,5,6,7,8]
        random.shuffle(values)
        sorter.insertion_sort(values)
        assert(values == [0,1,2,3,4,5,6,7,8])
        
        random.shuffle(values)
        sorter.insertion_sort(values,reverse=True)
        assert(values == [8,7,6,5,4,3,2,1,0])
        
        values= ["audi","kiasorentooooo","volkswagen","bmw"]
        random.shuffle(values)
        sorter.insertion_sort(values,key= lambda x : len(x))
        assert(values == ["bmw","audi","volkswagen","kiasorentooooo"])
        
        
    def __combsort_test(self, sorter):
        values = [0,1,2,3,4,5,6,7,8]
        random.shuffle(values)
        sorter.CombSort(values)
        assert(values == [0,1,2,3,4,5,6,7,8])
        
        random.shuffle(values)
        sorter.CombSort(values,reverse=True)
        assert(values == [8,7,6,5,4,3,2,1,0])
        
        values= ["audi","kiasorentooooo","volkswagen","bmw"]
        random.shuffle(values)
        sorter.CombSort(values,key= lambda x : len(x))
        assert(values == ["bmw","audi","volkswagen","kiasorentooooo"])
        
    
    
    def __insertion_sort_2criterii_test(self, sorter):
        path1="store_clienti_test_2criterii.txt"
        repo1= ClientRepositoryFile(path1)
        path2= "store_clienti_test_2criterii_rezultat.txt"
        repo2 = ClientRepositoryFile(path2)
        
        clienti = repo1.get_all()
        clienti_test=repo2.get_all()
        
        sorter.insertion_sort(clienti, cmp = lambda a,b : a.get_nume()< b.get_nume() or (a.get_nume() == b.get_nume() and a.get_inchirieri() < b.get_inchirieri()))
        self.assertEqual(clienti[0] , clienti_test[0])
        self.assertEqual(clienti[1] , clienti_test[1])
        self.assertEqual(clienti[2] , clienti_test[2])
        self.assertEqual(clienti[3] , clienti_test[3])
        self.assertEqual(clienti[4] , clienti_test[4])
        
        
        
    def test_all(self):
        sorter=Insertion_Sort()
        self.__insertion_sort_test(sorter)
        self.__insertion_sort_2criterii_test(sorter)
        sorter=Comb_Sort()
        self.__combsort_test(sorter)
        
        