from tools import tools as t

class Route():

    mois=""
    annee=""
    jour=""
    def __init__(self) -> None:
       self.jour=" "
       self.annee=" "
       self.jour=" "
    def traitMois(self,mois,chiffre,text):
        for i in mois:
            if i in text:
                self.mois=i
        for i in chiffre:
            if i in text:
                self.jour=self.jour+" "+i
            
        if self.mois !="":
           return True
        return False

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
        elif (True if self.traitMois(t.mois,t.lettre,text)==True else False):
            return "J'ai compris que vous voulez partir en ,"+self.jour+" "+self.mois
        else:
            return "Je n'ai pas compris votre demande de : ,"+text

