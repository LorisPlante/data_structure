import unittest
from unittest.mock import patch
from io import StringIO
import random
from exos.exo8 import deviner_nombre


class TestDevinerNombre(unittest.TestCase):
    @patch('sys.stdin', StringIO('50\n'))
    @patch('sys.stdout', new_callable=StringIO)
    def test_devine_nombre_trop_grand(self, mock_stdout, mock_input):
        random.seed(0)
        deviner_nombre()
        self.assertEqual(mock_stdout.getvalue(), "Devinez le nombre mystère entre 1 et 100. Vous avez 5 tentatives.\nLe nombre mystère est plus grand.\nLe nombre mystère est plus petit.\nLe nombre mystère est plus grand.\nLe nombre mystère est plus petit.\nBravo ! Vous avez deviné le nombre mystère, c'était 33.\n")

    @patch('sys.stdin', StringIO('50\n75\n63\n56\n59\n'))
    @patch('sys.stdout', new_callable=StringIO)
    def test_devine_nombre_trop_petit(self, mock_stdout, mock_input):
        random.seed(1)
        deviner_nombre()
        self.assertEqual(mock_stdout.getvalue(), "Devinez le nombre mystère entre 1 et 100. Vous avez 5 tentatives.\nLe nombre mystère est plus petit.\nLe nombre mystère est plus petit.\nLe nombre mystère est plus grand.\nLe nombre mystère est plus grand.\nBravo ! Vous avez deviné le nombre mystère, c'était 59.\n")


if __name__ == '__main__':
    unittest.main()
