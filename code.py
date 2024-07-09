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

    before = screen
    print(before)

    i = 0
    while i < char:
        if answer[i] == guess:
            screen[i] = guess
        i = i + 1
    if screen == before:
        print('A palavra não contem ',guess)
        shots = shots - 1
        if shots == 0:
            print('ENFORCADO XP')
    elif ''.join(screen) == answer:
        print('Parabéns, você acertou. A palavra é : ',answer)
        break
