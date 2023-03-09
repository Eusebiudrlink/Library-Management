from erori.exceptii import ValidationError
class ValidatorCarte(object):
    def valideaza(self,carte):
        erori=""
        if carte.get_id_carte() < 0:
            erori+="id invalid!"
        if carte.get_titlu()=="":
           erori+="titlu invalid!"
        if carte.get_descriere()=="":
            erori+="descriere invalida!"
        if carte.get_autor() == "":
           erori+="autor invalid!"
        if len(erori) > 0:
            raise ValidationError(erori)

class ValidatorClient(object):
    def valideaza(self,client):
        erori=""
        if client.get_id_client() < 0:
            erori+="id invalid!"
        if client.get_nume()=="":
           erori+="nume invalid!"
        if client.get_cnp() < 0:
           erori+="cnp invalid!"
        if len(erori) > 0:
            raise ValidationError(erori)


class ValidatorImprumut(object):
    def Valideaza(self,imprumut):
        erori=""
        if imprumut.get_id_imp()<0:
            erori += "id imprumut invalid!"
        if imprumut.get_data() =="":
            erori +="data invalida!"
        if len(erori) > 0:
            raise ValidationError(erori)
            


