import mido
import time
import rtmidi
import rtmidi.midiutil
from pychord import Chord

lines = []

p_to_c = {
        'M': 1,
        'A': 2,
        'E': 3,
        'S': 4,
        'L': 5,
        'I': 6,
        'F': 7
}

with open('output.txt', 'rt') as data:
    for line in data:
        if len(line) > 4:
            lines.append(line)
            print(line)

    del lines[0]

print(lines)

def play(n1, n2, n3, n4):
    note_on = [0x90, n1, 120]
    note_off = [0x80, n1, 0]
    midiout.send_message(note_on)
    time.sleep(.2)
    midiout.send_message(note_off)


for poly in lines:
    for protein in poly:
        chord = Chord.from_note_index(note=p_to_c.get(protein, 1), quality="", scale="Cmaj")
        print("Protein: ", protein)
        print("Chord: ", chord)
        print(chord.components())



"""

while True:
    try:
        c = raw_genome[0]
        note = translate.get(c, 60)
        print("Base: ", c, "Playing: ", to_notes.get(note, 'C'))
        note_on = [0x90, note, 120]
        note_off = [0x80, note, 0]
        midiout.send_message(note_on)
        time.sleep(.2)
        midiout.send_message(note_off)
        raw_genome = raw_genome[1:]
    except IndexError:
        del midiout
        
        
        SCALE = {'major': [2, 2, 1, 2, 2, 2, 1], 'natural minor': [2, 1, 2, 2, 1, 2, 2], 'melodic minor': [2, 1, 2, 2, 2, 2, 1],
         'harmonic minor': [2, 1, 2, 2, 1, 3, 1]}
start = 0
notes = []


keys = ['C', 'C#', 'D', 'D#',
        'E', 'F', 'F#', 'G',
        'G#', 'A', 'A#', 'B']

for kind in SCALE:
    scale(choice(keys), notes, kind)








translate = {
        'M': 60,
        'A': 63,
        'E': 65,
        'S': 67
}

to_notes = {
        60: 'C',
        63: 'D#',
        65: 'F',
        67: 'G'
        
        
        
        def scale(root, n, kind):
    global start
    start += 8
    print('\nroot = {} \tkind = {}'.format(root, kind))
    p = m21.pitch.Pitch(root)
    midi = p.midi
    for i in range(8):
        if i < 7:
            print('{},'.format(midi), end=' ')
        else:
            print('{}'.format(midi))
        n.append((midi, start + i, 1, 120))
        midi += SCALE[kind][i % 7]



}

"""



