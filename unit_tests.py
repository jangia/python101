from unittest import TestCase

from functions import args_to_dict


class TestArgsToDict(TestCase):

    def setUp(self):
        pass

    def test_args_to_dict(self):
        x1 = 2
        x2 = 5
        y1 = 1
        y2 = 4

        a = (2, 1)
        b = (5, 1)
        c = (5, 4)
        d = (2, 4)
        w = 3
        h = 3
        pl = 9
        ob = 12

        rectangle = args_to_dict(x1, x2, y1, y2)

        self.assertIsInstance(rectangle, dict)
        self.assertIn('A', rectangle)
        self.assertIn('pl', rectangle)
        self.assertEqual(rectangle['A'], a)
        self.assertEqual(rectangle['B'], b)
        self.assertEqual(rectangle['C'], c)
        self.assertEqual(rectangle['D'], d)
        self.assertEqual(rectangle['width'], w)
        self.assertEqual(rectangle['height'], h)
        self.assertEqual(rectangle['pl'], pl)
        self.assertEqual(rectangle['ob'], ob)
