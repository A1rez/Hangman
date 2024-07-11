import tkinter as tk


def obter_palavra():
    def confirmar():
        nonlocal palavra
        palavra = entry.get()
        janela.destroy()

    palavra = None
    janela = tk.Tk()
    janela.title("Entrada de Palavra")

    # Container 1: Label
    container1 = tk.Frame(janela)
    container1.pack(pady=10)
    label = tk.Label(container1, text="Digite a palavra que deve ser adivinhada")
    label.pack()

    # Container 2: Entry
    container2 = tk.Frame(janela)
    container2.pack(pady=10)
    entry = tk.Entry(container2)
    entry.pack()

    # Container 3: Button
    container3 = tk.Frame(janela)
    container3.pack(pady=10)
    botao_confirmar = tk.Button(container3, text="Confirmar", command=confirmar)
    botao_confirmar.pack()

    janela.mainloop()

    return palavra





answer = obter_palavra()
char = len(answer)

i = 0
screen = []
while i < char:
    screen.append('-')
    i=i+1

shots = 5
print('A palavra contem ',char,' letras!\n')

while shots > 0 :
    print('Você possui ',shots,' chutes!')
    print(''.join(screen))

    guess = input('\nQual o seu primeiro palpite?\n')

    i = 0
    c = 0
    while i < char:
        if answer[i] == guess:
            screen[i] = guess
            c = c + 1
        i = i + 1
    if c == 0:
        shots = shots - 1
    if ''.join(screen) == answer:
        print('Parabéns, você acertou. A palavra é : ',answer)
        break
    elif shots == 0:
        print('ENFORCADO Xp')
        print('A palavra é : ',answer)
