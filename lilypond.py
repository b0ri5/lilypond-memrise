import subprocess
import tempfile

def single_note_template(replacement):
  with open('single-note-template.ly') as f:
    contents = f.read()
  return contents % replacement

def run(contents):
  _, tmppath = tempfile.mkstemp()
  with open(tmppath, 'w') as f:
    f.write(contents)

  return subprocess.call(["~/lilypond/lilypond", tmppath])
