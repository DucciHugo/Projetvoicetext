def transcription(text):
    if "pension" in text:
        return "J'ai compris que vous voulez mettre les hôtels en ,demi-pension"
    elif "déjeuner" in text:
        return "J'ai compris que vous voulez un supplément, petit-déjeuner"
    elif "hébergement" in text:
        return "J'ai compris que vous voulez rester sur des ,hébergements seul"
    elif "complète" in text:
        return "J'ai compris que vous voulez une ,pension complète"
    elif "tous inclus" in text:
        return "J'ai compris que vous voulez une formule ,tous inclus"
    elif "hall" in text:
        return "J'ai compris que vous metez les hôtels en ,all inclusive"
    elif "inclusifs" in text:
       return "J'ai compris que vous metez les hôtels en ,all inclusive"
    elif "inclusive" in text:
        return "J'ai compris que vous metez les hôtels en ,all inclusive"

    else:
        return "Je n'ai pas compris votre demande de : ,"+text
