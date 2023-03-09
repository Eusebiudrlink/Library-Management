class Consola(object):

    
    def __init__(self, srv_carti, srv_clienti,srv_imprumut):
        self.__srv_carti = srv_carti
        self.__srv_clienti = srv_clienti
        self.__srv_imprumut = srv_imprumut
   
        
 
    
    def __ui_adauga_carte(self):
        try:
            id_carte=int(input("id_carte:"))
        except ValueError:
            print("id invalid!")
            return 0
        titlu = input("titlu:")
        descriere = input("descriere:")
        autor = input("autor:")
        try:
            self.__srv_carti.adauga_carte(id_carte,titlu,descriere,autor)
            print("carte adaugata cu succes!")
        except Exception as ex:
            print(str(ex))
            return 0
        
        
    def __ui_adauga_client(self):
        try:
            id_client=int(input("id client:"))
        except ValueError:
            print("id invalid!")
            return 0
        nume=input("nume:")
        try:
            cnp = int(input("cnp:"))
        except ValueError:
            print("cnp invalid!")
            return 0
        try:
            self.__srv_clienti.adauga_client(id_client,nume,cnp)    
            print("client adaugat cu succes!")
        except Exception as ex:
            print(str(ex))
            return 0
        
    
    
    def __ui_printeaza_cartile(self):
        carti=self.__srv_carti.get_all_carti()
        for carte in carti:
            print(carte)
        
    
    
    def __ui_printeaza_clientii(self):
        clienti=self.__srv_clienti.get_all_clienti()
        for client in clienti:
            print(client)
    
    
    def __ui_cauta_carte(self):
        titlu=input("Titlu:")
        try:
            carte = self.__srv_carti.cauta_carte(titlu)
            print("Carte cu titlu ",titlu, " de ", carte.get_autor(), " este neinchiriata")
        except Exception as ex:
            print(str(ex))
    
        
    def __ui_cauta_client(self):
        nume = input("nume:")
        try:
            client = self.__srv_clienti.cauta_client(nume)
            print("Clientul cu id-ul", client.get_id_client(), " numele ",nume," si CNP-ul ", client.get_cnp(), "nu a inchiriat nicio carte")
        except Exception as ex:
            print(str(ex))
    
    
    def __ui_maxcarte(self):
        try:
            carte = self.__srv_carti.lungmax()
            print("Cartea cu titlul cel mai lung este ", carte.get_titlu()," de autorul ",carte.get_autor())
        except Exception as ex:
            print(str(ex))
    
    
    def __ui_adauga_imprumut(self):
        try:
            id_imp=int(input("id imprumut:"))
        except ValueError:
            print("id imprumut invalid!")
            return 0
        try:
            id_carte=int(input("id carte:"))
        except ValueError:
            print("id carte invalid!")
            return 0
        try:
            id_client=int(input("id client:"))
        except ValueError:
            print("id client invalid!")
            return 0
        data=input("data imprumutului:")
        try:
            self.__srv_imprumut.adauga_imprumut(id_imp,id_carte,id_client,data)
            print("cartea a fost inchiriata cu succes!")
        except Exception as ex:
            print(str(ex))
            return 0
    
    
    def __ui_printeaza_imprumuturi(self):
        imprumuturi = self.__srv_imprumut.get_all_imprumuturi()
        for imprumut in imprumuturi:
            print(imprumut)
    
    
    def __ui_sterge_carte(self):
        
        try:
            id_carte=int(input("id-ul cartii de sters:"))
        except ValueError:
            print("Valoare invalida pentru id-ul cartii")
        
        try:
            self.__srv_imprumut.sterge_carte_srv(id_carte)
            print("cartea cu id-ul ",id_carte, "si toate imprumuturile asociate ei au fost sterse!")
        except Exception as ex:
            print(str(ex))    
    
    def __ui_sterge_client(self):
        try:
            id_client=int(input("id-ul clientului de sters:"))
        except ValueError:
            print("Valoare invalida pentru id-ul clientului")
        
        try:
            self.__srv_imprumut.sterge_client_srv(id_client)
            print("clientul cu id-ul ",id_client, "si toate imprumuturile asociate lui au fost sterse!")
        except Exception as ex:
            print(str(ex))
    
    
    def __modifica_carte(self):
        try:
            id_carte=int(input("id-ul cartii de modificat:"))
        except ValueError:
            print("Valoare invalida pentru id-ul cartii")
        titlu = input("titlu:")
        descriere = input("descriere:")
        autor = input("autor:")
        
        try:
            self.__srv_carti.modifica_carte(id_carte,titlu,descriere,autor)
            print("detaliile cartii au fost modificate cu succes!")
        except Exception as ex:
            print(str(ex))
    
    
    def __modifica_client(self):
        try:
            id_client=int(input("id-ul clientului de modificat:"))
        except ValueError:
            print("Valoare invalida pentru id-ul clientului")
        nume=input("nume:")
        try:
            cnp = int(input("cnp:"))
        except ValueError:
            print("cnp invalid!")
            return 0   
        try:
            self.__srv_clienti.modifica_client(id_client,nume,cnp)
            print("detaliile clientului au fost modificate cu succes")
        except Exception as ex:
            print(str(ex))
            
    
    def __returneaza_carte(self):
        
        titlu=input("Titlul cartii pe care o returnati:")
        nume=input("numele clientului care a inchiriat-o:")
        try:
            self.__srv_imprumut.sterge_imprumut(titlu,nume)
            print("carte returnata cu succes!")
        except Exception as ex:
            print(str(ex))
            
    
    def __ui_gencarti(self):
        try:
            cmd=int(input("Cate carti sa se genereze?")) 
        except ValueError:
            print("numarul de carti a fost introdus gresit!")
    
        try:
            self.__srv_carti.gencarti(cmd)
            print("Au fost create ",cmd," carti cu succes")
        except Exception as ex:
            assert True
        
    def __ui_genclienti(self):
        try:
            cmd=int(input("Cati clienti sa se genereze?")) 
        except ValueError:
            print("numarul de clienti a fost introdus gresit!")
    
        try:
            self.__srv_clienti.genclienti(cmd)
            print("Au fost creati ",cmd," clienti cu succes")
        except Exception as ex:
            assert True
    def __ui_genimp(self):
        try:
            cmd=int(input("Cate imprumuturi  sa se genereze?")) 
        except ValueError:
            print("numarul de imprumuturi a fost introdus gresit!")
    
        try:
            self.__srv_imprumut.genimprumuturi(cmd)
            print("Au fost create ",cmd," imprumuturi cu succes")
        except Exception as ex:
            assert True 
        
    
    
    
    def __afiseazacomenzi(self):
        print("Comenzile pentru utilizarea aplicatiei biblioteca:")
        print("-add carte ")
        print("-add client ")
        print("-sterge carte ")
        print("-sterge client ")
        print("-modifica carte ")
        print("-modifica client ")
        print("-inchiriaza carte ")
        print("-returneaza carte ")
        print("-search for carte ")
        print("-search for client ")
        print("-cele mai inchiriate ")
        print("-raport dupa titlu ")
        print("-raport dupa numarul de carti")
        print("-raport clienti activi")
        print("-genereaza carti/clienti/imprumuturi(1,2,3)")
        print("-print carti/clienti/inchirieri ")   
        print("-2_criterii - comanda va afisa lista sortata dupa nume si inchirieri") 
    
 
    
    def __ui_raport_cele_mai_inchiriate(self):
        carti=self.__srv_carti.rap_cele_mai_inchiriate()
        print("Cele mai inchiriate carti in ordine descrescatoare sunt:")
        for carte in carti:
            if carte.get_inchirieri()>0:
                print(carte.get_titlu())
     
    def __ui_rap_dupa_nume(self):
        lista_nume=self.__srv_clienti.rap_dupa_nume()
        print("Clientii ordonati dupa nume cu carti inchiriate sunt:")
        for nume in lista_nume:
            print("nume client:",nume)
    

    def __ui_rapo_dupa_nr_carti(self):
        clienti=self.__srv_clienti.rap_dupa_nr_carti()
        print("Clientii ordonati dupa numarul de carti inchiriate sunt: ")
        for client in clienti:
            if client.get_inchirieri()>0:
                print("nume client: ",client.get_nume())
        
    
    def __ui_clienti_activi(self):
        clienti = self.__srv_clienti.rap_dupa_nr_carti()
        lung=len(clienti)//5
        if lung<1 and len(clienti)>0:
            lung =1
        for i in range(lung):
            print("clientul",clienti[i].get_nume()," cu ",clienti[i].get_inchirieri()," de carti inchiriate")
            
    
    
    def __ui_cerinta_noua(self):
        clienti = self.__srv_clienti.rap_dupa_cnp()
        print("Primii 3 clienti cu cnp ul cel mai mare sunt:")
        print(clienti[0])
        print(clienti[1])
        print(clienti[2])
        
        
    
    
    def __douacriterii(self):
        clienti = self.__srv_clienti.douacriterii()
        for client in clienti:
            print(client)
    
    
    def run(self):
        self.__afiseazacomenzi()
        while True:
            cmd = input("comanda:")
            if cmd == "":
                continue
            elif cmd =="exit":
                return 
            elif cmd == "add carte":
                self.__ui_adauga_carte()
            elif cmd == "add client":
                self.__ui_adauga_client()
            elif cmd == "a":
                self.__ui_adauga_imprumut()
            elif cmd== "returneaza carte":
                self.__returneaza_carte()
                
            elif cmd == "search for carte":
                self.__ui_cauta_carte()
            elif cmd == "search for client":
                self.__ui_cauta_client()
                
            elif cmd == "sterge client":
                self.__ui_sterge_client()
            elif cmd == "sterge carte":
                self.__ui_sterge_carte()
            
            elif cmd == "modifica carte":
                self.__modifica_carte()
            elif cmd == "modifica client":
                self.__modifica_client()
                
            elif cmd == "cele mai inchiriate":
                self.__ui_raport_cele_mai_inchiriate()
            elif cmd == "raport dupa titlu":
                self.__ui_rap_dupa_nume()
            elif cmd == "raport dupa numarul de carti":
                self.__ui_rapo_dupa_nr_carti()
            elif cmd == "raport clienti activi":
                self.__ui_clienti_activi()
                
            elif cmd == "print carti":
                self.__ui_printeaza_cartile()
            elif cmd == "print clienti":
                self.__ui_printeaza_clientii()
            elif cmd == "print imprumuturi":
                self.__ui_printeaza_imprumuturi()
                
            elif cmd=="afiseaza cartea maxima":
                self.__ui_maxcarte()
            elif cmd=="1":
                self.__ui_gencarti()
            elif cmd == "2":
                self.__ui_genclienti()
            elif cmd == "3":
                self.__ui_genimp()
                
            elif cmd =="cerinta noua":
                self.__ui_cerinta_noua()
            elif cmd == "2_criterii":
                self.__douacriterii()
            else:
                print("comanda invalida")


