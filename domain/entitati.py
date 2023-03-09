class Carte(object):

    
    def __init__(self, id_carte, titlu, descriere, autor,inchirieri):
        self.__id_carte = id_carte
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor
        self.__inchirieri = inchirieri

    def get_id_carte(self):
        return self.__id_carte


    def get_titlu(self):
        return self.__titlu


    def get_descriere(self):
        return self.__descriere


    def get_autor(self):
        return self.__autor


    def set_titlu(self, value):
        self.__titlu = value


    def set_descriere(self, value):
        self.__descriere = value
    def get_inchirieri(self):
        return self.__inchirieri
    def set_inchirieri(self,value):
        self.__inchirieri=value

    def set_autor(self, value):
        self.__autor = value
    def __str__(self):
        return "id:"+str(self.__id_carte)+"  titlu:"+self.__titlu+"  descriere:"+ self.__descriere + "  autor:"+ self.__autor+ "  inchirieri: "+str(self.__inchirieri)
    def __eq__(self,carte):
        if carte ==-1:
            return 0
        return carte.get_id_carte()==self.__id_carte and carte.get_titlu() == self.__titlu and carte.get_descriere()== self.__descriere and carte.get_autor()== self.__autor


class Client(object):   
    
    
    def __init__(self, id_client, nume, cnp,inchirieri):
        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp
        self.__inchirieri=inchirieri

    def get_id_client(self):
        return self.__id_client

    def get_nume(self):
        return self.__nume


    def get_cnp(self):
        return self.__cnp
    def get_inchirieri(self):
        return self.__inchirieri

    def set_nume(self, value):
        self.__nume = value


    def set_cnp(self, value):
        self.__cnp = value
    def set_inchirieri(self,value):
        self.__inchirieri=value
    
    def __str__(self):
        return "id:"+ str(self.__id_client)+ "  nume:"+self.__nume+"  cnp:"+str(self.__cnp)+"  inchirieri:" + str(self.__inchirieri)
    
    
    def __eq__(self,client):
        if client == -1:
            return 0

        return client.get_id_client()==self.__id_client and client.get_nume()==self.__nume
        



class Imprumut(object):
    
    
    def __init__(self, id_imp, id_carte, id_client, data):
        self.__id_imp = id_imp
        self.__id_carte = id_carte
        self.__id_client = id_client
        self.__data = data

    def get_id_imp(self):
        return self.__id_imp


    def get_id_carte(self):
        return self.__id_carte


    def get_id_client(self):
        return self.__id_client


    def get_data(self):
        return self.__data


    def set_id_carte(self, value):
        self.__id_carte = value


    def set_id_client(self, value):
        self.__id_client = value


    def set_data(self, value):
        self.__data = value
        
    def __str__(self):
        return "id imprumut: "+ str(self.__id_imp)+ " id carte: "+str(self.__id_carte)+"  id client: "+str(self.__id_client)+" data: "+str(self.__data)
    
    



