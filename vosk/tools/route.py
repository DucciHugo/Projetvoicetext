from tools import tools as t

class Route():

    mois=""
    nb=" "
    jour=" "
    dest=" "
    ville=" "
    adulte=""
    enfant=""
    bebe=""
    def __init__(self) -> None:
       self.jour=" "
       self.nb= " "
       self.jour=" "
       self.mois="0"
       self.enfant="0"
       self.bebe="0"
       self.adulte="0"
    def traitMois(self,mois,chiffre,text):
        for i in mois:
            if i.lower() in text:
                self.mois=i
        for i in chiffre:
            if i in text:
                self.jour=self.jour+" "+i
            
        if self.mois !="0":
           return True
        return False

    def traitDest(self,dest,text):
        for i in dest:
           if i in text:
               self.dest=i
               return True
   
    def traitNb(self,lettre,text):
         for i in lettre:
            if i in text:
                self.nb=i
    def traitVille(self,ville,text):
        for i in ville:
            if i.lower() in text:
                  self.ville=i
                  return True
        return False
    def traitDevis(self,lettre,text):
          for i in lettre:
             if ((i in text)and("adulte" in text)and(self.adulte=="0")):
                  self.adulte=i
             elif ((i in text)and("enfant" in text)and(self.enfant=="0")and(self.adulte!="0")):
                  self.enfant=i
             elif ((i in text)and("bébé" in text)and(self.bebe=="0")and(self.adulte!="0")and(self.enfant!="0")):
                  self.bebe=i
    def transcription(self,text):
        if "complète" in text:
            return "J'ai compris que vous voulez une ,pension-complète"
        elif "déjeuner" in text:
            return "J'ai compris que vous voulez un supplément, petit-déjeuner"
        elif "hébergement" in text:
            return "J'ai compris que vous voulez rester sur des ,hébergements seul"
        elif "pension" in text:
            return "J'ai compris que vous voulez mettre les hôtels en ,demi-pension"
        elif "tous inclus" in text:
            return "J'ai compris que vous voulez une formule ,tous inclus"
        elif "hall" in text:
            return "J'ai compris que vous metez les hôtels en ,all inclusive"
        elif "inclusifs" in text:
            return "J'ai compris que vous metez les hôtels en ,all inclusive"
        elif "inclusive" in text:
            return "J'ai compris que vous metez les hôtels en ,all inclusive"
        elif "conditions" in text:
            return "J'ai compris que vous voulez avoir des information sur les ,conditions d'annulation"
        elif "annulation" in text:
            return "J'ai compris que vous voulez avoir des information sur les ,conditions d'annulation"
        elif "contre" in text:
            return "J'ai compris que vous voulez une ,contre-proposition"
        elif "proposition" in text:
            return "J'ai compris que vous voulez une ,contre-proposition"
        elif (True if self.traitMois(t.mois,t.lettre,text) else False) and (("adulte" not in text) or ("enfant" not in text) or ("bébé" not in text)):
             return "J'ai compris que vous voulez partir le ,"+self.jour+" "+self.mois
        elif (True if self.traitDest(t.destination,text)==True else False):
            if self.dest=="séchelles":
                  self.dest="seychelles"
            return "J'ai compris que vous voulez faire un devis pour ,"+self.dest
        elif "nuit" in text:
             self.traitNb(t.lettre,text)
             return "Vous avez mis ,"+self.nb+" nuit"
        elif (True if self.traitVille(t.ville,text)==True else False):
             return "J'ai compris que vous partez de ,"+self.ville
        elif "adulte" in text  and "enfant" in text and "bébé" in text:
              self.traitDevis(t.lettreDes,text)
              return "J'ai compris que vous voulez un devis pour ,"+self.adulte+" adulte "+self.enfant+" enfant "+self.bebe+" bébé"
        elif "adulte" in text and "enfant" in text:
             return  "j'ai compris que vous voulez un devis pour ,adulte enfant"
        elif "adulte" in text and "bébé" in text:
              return "J'ai compris que vous voulez un devis pour ,adulte bébé"
        elif "enfant" in text:
              return "J'ai compris que vous voulez un devis pour ,enfant"
        elif "bébé" in text:
              return "J'ai compris que vous voulez un devis pour ,bébé"
        elif "adulte" in text:
              return "J'ai compris que vous voulez un devis pour ,adulte"
        else:
            return "Je n'ai pas compris votre demande de : ,"+text

