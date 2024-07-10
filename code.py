answer = input('Digite a palavra que deve ser adivinhada: ')
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
