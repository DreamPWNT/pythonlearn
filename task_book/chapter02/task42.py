A = 440.00
B = 493.88
C = 261.63
D = 293.66
E = 329.63
F = 349.23
G = 392.00

note = input('Enter musical note with octave (for example: A5): ')

note_index = note[0]
octave_index = int(note[1])

if note_index == 'A':
    result = A / (pow(2, 4 - octave_index))
if note_index == 'B':
    result = B / (pow(2, 4 - octave_index))
if note_index == 'C':
    result = C / (pow(2, 4 - octave_index))
if note_index == 'D':
    result = D / (pow(2, 4 - octave_index))
if note_index == 'E':
    result = E / (pow(2, 4 - octave_index))
if note_index == 'F':
    result = F / (pow(2, 4 - octave_index))
if note_index == 'G':
    result = G / (pow(2, 4 - octave_index))

print(f'Frequency of note {note} = {round(result, 2)}')
