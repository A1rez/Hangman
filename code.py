import tkinter as tk

def on_enter(event, button):
    button.invoke()

def forca(screen, n, Shots, pg):
    def confirmar():
        nonlocal palavra
        palavra = entry.get()
        janela.destroy()


    palavra = None
    janela = tk.Tk()
    janela.bind('<Return>', on_enter)
    janela.title("Jogo da forca")

    container1 = tk.Frame(janela)
    container1.pack(pady=10, padx=150)
    label = tk.Label(container1, text="A palavra contem "+ str(n) +" letras!", font = ("Arial", 15))
    label.pack()

    container4 = tk.Frame(janela)
    container4.pack(pady=5, padx=150)
    label = tk.Label(container1, text="Você possui "+ str(Shots) +" chutes", font = ("Arial", 10))
    label.pack()

    container2 = tk.Frame(janela)
    container2.pack(pady=15, padx=150)
    label = tk.Label(container2, text=''.join(screen), font = ("Arial", 50))
    label.pack()

    container5 = tk.Frame(janela)
    container5.pack(pady=5, padx=150)
    label = tk.Label(container1, text= pg, font = ("Arial", 25))
    label.pack()

    # Container 2: Entry
    container2 = tk.Label(janela, text = 'Palpite:',pady=5, font = ("Arial", 25))
    container2.pack()
    entry = tk.Entry(janela, bd=5)
    entry.pack()

    # Container 3: Button
    container3 = tk.Frame(janela)
    container3.pack(pady=10)
    botao_confirmar = tk.Button(container3, text="Confirmar", font = ("Arial", 25), command=confirmar)
    botao_confirmar.pack()

    janela.bind('<Return>', lambda event: on_enter(event, botao_confirmar))

    janela.mainloop()

    return palavra

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
    label = tk.Label(container1, text="Digite a palavra que deve ser adivinhada", font = ("Arial", 25))
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

def correct(ans):
    janela = tk.Tk()
    janela.title("Jogo da forca")

    container1 = tk.Frame(janela)
    container1.pack(pady=10, padx=150)
    label = tk.Label(container1, text="PARABÉNS!!\nVocê acertou :)\nA palavra é "+ str(ans), font=("Arial", 25))
    label.pack()

    janela.mainloop()


def wrong(ans):
    janela = tk.Tk()
    janela.title("Jogo da forca")

    container1 = tk.Frame(janela)
    container1.pack(pady=10, padx=150)
    label = tk.Label(container1, text="ENFORCADO!!\nXp\nA palavra é "+ str(ans), font=("Arial", 25))
    label.pack()

    janela.mainloop()


answer = obter_palavra()
char = len(answer)
pastguess=[]

i = 0
screen = []
while i < char:
    screen.append('-')
    i=i+1

shots = 5

while shots > 0 :
    guess = forca(screen,char,shots, pastguess)
    pastguess.append(guess)
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
        correct(answer)
        break
    elif shots == 0:
        wrong(answer)
