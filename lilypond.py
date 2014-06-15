import os
import subprocess
import tempfile

def single_note_template(replacement):
  with open('single-note-template.ly') as f:
    contents = f.read()
  return contents % replacement

def run(contents, outpath):
  _, tmppath = tempfile.mkstemp()
  with open(tmppath, 'w') as f:
    f.write(contents)

  exitcode = subprocess.call(["lilypond", "--output", outpath, tmppath])
  if exitcode:
    return exitcode

  exitcode = subprocess.call(['convert', '-density', '400', '-trim', '+repage', outpath + '.pdf', outpath + '.png'])
  if exitcode:
    return exitcode

  os.remove(outpath + '.pdf')
  return exitcode
