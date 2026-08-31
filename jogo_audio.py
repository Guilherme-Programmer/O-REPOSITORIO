import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import random
while True:
    palavras = {
    "casa": "house",
    "gato": "cat",
    "cachorro": "dog",
    "janela": "window",
    "escola": "school",
    "cidade": "city",
    "borboleta": "butterfly",
    "biblioteca": "library",
    "conhecimento": "knowledge",
    "Molécula": "molecule",
    "Apreensão": "seizure",
    "Inscrição": "superscription"
}
    print(" 🎙️ Seja bem vindo ao Jogo da Voz! 🎙️")
    print("Escolha a dificuldade:")
    print("1 - 🟢Fácil")
    print("2 - 🟡Médio")
    print("3 - 🔴Difícil")
    print("4 - ⚫Impossível")

    dificuldade = input("Escolha atentamente 😁: ")

    if dificuldade == "1":
        palavras = {
            "casa": "house",
            "gato": "cat",
            "cachorro": "dog"
    }

    elif dificuldade == "2":
        palavras = {
            "janela": "window",
            "escola": "school",
            "cidade": "city"
    }

    elif dificuldade == "3":
        palavras = {
            "borboleta": "butterfly",
            "biblioteca": "library",
            "conhecimento": "knowledge"
    }
          
    elif dificuldade == "4":
        palavras = {
            "Molécula": "molecule",
            "Apreensão": "seizure",
            "Inscrição": "superscription"
    }

    palavra, traducao = random.choice(list(palavras.items()))

    print("\nTraduza a palavra:", palavra)
    print("Fale agora... 🗣️")

    gravacao = sd.rec(
        5 * 44100,
        samplerate=44100,
        channels=1,
        dtype=np.int16
)

    sd.wait()

    wav.write("audio.wav", 44100, gravacao)

    reconhecedor = sr.Recognizer()

    with sr.AudioFile("audio.wav") as arquivo:
        audio = reconhecedor.record(arquivo)

    try:
        resposta = reconhecedor.recognize_google(audio, language="en-US")

        print("Você falou:", resposta)

        if resposta.lower() == traducao:
            print("Correto! Você ganhou! 😁")
        else:
            print("Errado! 😡")
            print("A resposta era:", traducao, " 😊")

    except:
        print("Não consegui entender sua voz. 🤖")
