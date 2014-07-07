import os
import subprocess

def single_note_template(replacement):
  with open('single-note-template.ly') as f:
    return f.read() % replacement

def run(contents, name):
  lilyfile = name + '.ly'
  with open(lilyfile, 'w') as f:
    f.write(contents)

  exitcode = subprocess.call(["lilypond", "--output", name, lilyfile])
  if exitcode:
    return exitcode

  exitcode = subprocess.call(['convert',
                              '-density', '400',
                              '-trim', '+repage',
                              name + '.pdf', name + '.png'])

  if exitcode:
    return exitcode

  os.remove(name + '.pdf')
  return exitcode
