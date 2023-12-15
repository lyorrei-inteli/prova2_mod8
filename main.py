# Importação das bibliotecas
from gtts import gTTS
import os

# Função que faz a conversão de texto para voz
def text_to_speech(text, lang="pt"):
    
    # Instância a classe da lib de Google Text To Speech passando o texto e a linguagem (faz a conversão de texto para voz)
    tts = gTTS(text=text, lang=lang)

    # Nome do arquivo de áudio que deve ser salvo
    audio_file = "audio.mp3"

    # Salva o arquivo de áudio na root do repositório
    tts.save(audio_file)

    # Executa o arquivo de áudio
    os.system(
        f"open {audio_file}"
    )  # 'start' para Windows, use 'open' para MacOS ou 'xdg-open' para Linux

    # Prints para mostrar no terminal que o arquivo de áudio está sendo executado
    print("O texto está sendo reproduzido...")
    print("---------------")


# Função principal do sistema, responsável por todos os processos
def main():
    
    # Loop para manter o 
    while True:
        # Convertendo texto traduzido para áudio
        user_input = input("Insira a frase que deseja reproduzir (preencha \"sair\" caso deseje encerrar): ")

        # Parar o loop caso o usuário digite "sair"
        if (user_input == "sair"):
            break
        
        # Executa a função que faz a conversão de texto para voz
        text_to_speech(user_input)


# Executa a função principal do sistema quando o script é iniciado
if __name__ == "__main__":
    main()
