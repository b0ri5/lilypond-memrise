import lilypond
import os
import unittest

class UnitTests(unittest.TestCase):
  def test_lilypond_run(self):
    lilycontents = lilypond.single_note_template('c') 
    print lilycontents
    self.assertEqual(0, lilypond.run(lilycontents, "testout"))
    self.assertTrue(os.path.exists("testout.pdf"))
