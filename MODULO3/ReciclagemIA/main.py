respostas = {
    "plástico": {
        "categoria": "Plástico",
        "reciclavel": "Sim",
        "destino": "Coleta seletiva da sua cidade",
        "dica": "Esvazie a garrafa antes do descarte."
    },

    "aluminio": {
        "categoria": "Metal",
        "reciclavel": "Sim",
        "destino": "Coleta seletiva da sua cidade",
        "dica": "Esvazie o conteúdo antes do descarte."
    },
      
    "vidro": {
        "categoria": "Vidro",
        "reciclavel": "Sim",
        "destino": "Coleta seletiva da sua cidade",
        "dica": "Esvazie o conteúdo antes do descarte."
    }
    
    
}

while True:
        
        print("♻️ IA DE RECICLAGEM")
        print("--------------------")

        material = input("O que você gostaria de descartar? ").lower()

        if material in respostas:
            informacao = respostas[material]

            print()
            print("Material:", material)
            print("Categoria:", informacao["categoria"])
            print("Reciclável:", informacao["reciclavel"])
            print("Destino:", informacao["destino"])
            print("Dica:", informacao["dica"])

        else:
            print()
            print("Ainda não conheço esse material.")

        if material == "nada":
            print("Beleza então, tenha um ótimo dia!")
            break
