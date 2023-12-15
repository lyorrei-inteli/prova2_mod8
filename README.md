# Leitor de texto

## Objetivo
Este projeto consiste em uma aplicação capaz de integrar uma aplicação de text-to-speech (síntese de voz) com o terminal. Seu objetivo principal é receber um texto e converte-lo para áudio.

## Como Funciona
A aplicação opera em linha de comando e aceita como input o texto que o usuário quer reproduzir. Após criar um arquivo de áudio com base nesse texto, a aplicação o reproduz.

## Requisitos
- Python
- Bibliotecas: `gtts`

## Instalação e Execução
1. Instale as dependências necessárias:
   ```
   pip install gtts
   ou
   pip install -r requirements.txt
   ```
2. Execute o script com o seguinte comando:
   ```
   python3 main.py 
   ```

## Explicação do código
Uma explicação detalhada de cada linha de código pode ser encontrada nos comentários acima de cada linha. 