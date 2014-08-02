import os
import lilypond

class Note(object):
  def __init__(self, lily, english):
    self.lily = lily
    self.english = english


def main():
  octaves = [('', '3'), ("'", '4'), ("''", '5')]
  notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
  if not os.path.exists('single-notes'):
    os.makedirs('single-notes')
  for note in notes:
    for octave in octaves:
      n = Note(note + octave[0], note.upper() + octave[1])
      name = os.path.join('single-notes', n.english)
      contents = lilypond.single_note_template(n.lily)
      lilypond.run(contents, name)

if __name__ == '__main__':
  main()
