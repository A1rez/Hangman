# Jogo da Forca em Python

Este projeto implementa um jogo da forca usando a biblioteca `tkinter` para criar uma interface gráfica. O jogador deve adivinhar a palavra correta dentro de um número limitado de tentativas.

## Requisitos

- Python 3.x
- Biblioteca `tkinter` (geralmente incluída na instalação padrão do Python)

## Estrutura do Código

O código é dividido em várias funções principais:

1. **`forca(screen, n, Shots, pg)`**: Função principal do jogo, que exibe a interface gráfica para o jogador fazer suas tentativas.
2. **`obter_palavra()`**: Função para obter a palavra que deve ser adivinhada.
3. **`correct(ans)`**: Função chamada quando o jogador adivinha a palavra corretamente.
4. **`wrong(ans)`**: Função chamada quando o jogador esgota suas tentativas sem adivinhar a palavra.

## Como Jogar

1. **Obtenção da Palavra**: A função `obter_palavra()` é chamada para o usuário inserir a palavra a ser adivinhada.
2. **Configuração Inicial**: A palavra é convertida em uma lista de caracteres e o número de tentativas (chutes) é definido.
3. **Loop Principal**:
   - O jogador faz uma tentativa usando a função `forca()`.
   - As tentativas são verificadas e o número de tentativas restantes é atualizado.
   - O jogo termina quando o jogador adivinha a palavra ou esgota todas as tentativas.
