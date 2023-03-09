'''
Created on Nov 9, 2021

@author: Eusebiu
'''
from prezentare.user_interface import Consola
from bussines.services import ServiceCarti, ServiceClienti,ServiceImprumut
from infrastracture.Carti import RepoCarti,CarteRepositoryFile
from infrastracture.Clienti import RepoClienti,ClientRepositoryFile
from infrastracture.Imprumuturi import RepoImprumut,ImprumutRepositoryFile
from validation.validator import ValidatorCarte, ValidatorClient,ValidatorImprumut
from testare.teste import Teste
import unittest

if __name__ == '__main__':
    
    valid_carte = ValidatorCarte()
    valid_client = ValidatorClient()
    valid_imprumut = ValidatorImprumut()
    
   
    path_carti = "store_carti.txt"
    repo_carti_file = CarteRepositoryFile(path_carti)
    path_clienti = "store_clienti.txt"
    repo_clienti_file = ClientRepositoryFile(path_clienti)
    path_imprumuturi = "store_imprumuturi.txt"
    repo_imprumut_file = ImprumutRepositoryFile(path_imprumuturi)
    
    srv_carti = ServiceCarti(valid_carte, repo_carti_file)
    srv_clienti = ServiceClienti(valid_client, repo_clienti_file)
    srv_imprumut = ServiceImprumut(valid_imprumut,repo_imprumut_file,repo_carti_file, repo_clienti_file)
    
    ui = Consola(srv_carti, srv_clienti,srv_imprumut)
    
    teste=Teste()
    teste.run_all_teste()
    
    ui.run()
    