respostas = {
    "plástico": {
        "categoria": "plástico/embalagens",
        "reciclavel": "Sim",
        "destino": "Coleta seletiva da sua cidade",
        "dica": "Esvazie a garrafa antes do descarte."
    },

    "aluminio": {
        "categoria": "metal/latas",
        "reciclavel": "Sim",
        "destino": "Coleta seletiva da sua cidade",
        "dica": "Feche/Lacre bem antes do descarte."
    },
      
    "vidro": {
        "categoria": "vidro/garrafas",
        "reciclavel": "Sim",
        "destino": "Coleta seletiva da sua cidade",
        "dica": "Cuide bem antes de fazer o descarte. Pode acabar ouvendo acidentes."
    },
    
    "papel": {
        "categoria": "papel/papelão",
        "reciclável": "Não",
        "destino": "Coleta seletiva da sua cidade",
        "dica": "Separe o lixo não reciclável do que é reciclável!"
    },
    
    "resíduos animais": {
        "categoria": "resíduos/fezes",
        "reciclável": "não",
        "destino": "Coleta seletiva da sua cidade",
        "dica": "Embale bem as fezes/resíduos antes de colocar no lixo."
        
    } 
        
    }

while True:
        
        print("♻️ IA DE RECICLAGEM")
        print("Seja bem vindo!")
        print("--------------------")

        material = input("O que você gostaria de reciclar?").lower()

        if material in respostas:
            informacao = respostas[material]

            print()
            print("Material:", material)
            print("Categoria:", informacao["categoria"])
            print("Reciclável:", informacao["reciclável"])
            print("Destino:", informacao["destino"])
            print("Dica:", informacao["dica"])
        
            
        else:
            print()
            print("Ainda não conheço esse material...")

        if material == "nada":
            print("Beleza então, tenha um ótimo dia!")
            break
