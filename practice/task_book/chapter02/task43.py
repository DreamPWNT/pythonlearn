A = 440.00
B = 493.88
C = 261.63
D = 293.66
E = 329.63
F = 349.23
G = 392.00

frequency = float(input('Enter musical note frequency: '))

if frequency - 1 <= A <= frequency + 1:
    print('Musical note is A4')
elif frequency - 1 <= B <= frequency + 1:
    print('Musical note is B4')
elif frequency - 1 <= C <= frequency + 1:
    print('Musical note is C4')
elif frequency - 1 <= D <= frequency + 1:
    print('Musical note is D4')
elif frequency - 1 <= E <= frequency + 1:
    print('Musical note is E4')
elif frequency - 1 <= F <= frequency + 1:
    print('Musical note is F4')
elif frequency - 1 <= G <= frequency + 1:
    print('Musical note is G4')
else:
    print('Note is not found')
