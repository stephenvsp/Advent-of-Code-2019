import unittest
from part1 import shuffle

class TestProblem22(unittest.TestCase):

    def test_deal_into_new_stack(self):
        deck = list(range(0, 10))

        sequence = ['deal into new stack']

        expected_shuffle = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        actual_shuffle = shuffle(deck, sequence)

        self.assertEqual(actual_shuffle, expected_shuffle)

    def test_cut_N_cards(self):

        deck = list(range(0, 10))

        sequence = ['cut 3']

        expected_shuffle = [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
        actual_shuffle = shuffle(deck, sequence)

        self.assertEqual(actual_shuffle, expected_shuffle)

    def test_cut_negative_N_cards(self):

        deck = list(range(0, 10))

        sequence = ['cut -4']

        expected_shuffle = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
        actual_shuffle = shuffle(deck, sequence)

        self.assertEqual(actual_shuffle, expected_shuffle)

    def test_increment_N(self):

        deck = list(range(0, 10))

        sequence = ['deal with increment 3']

        expected_shuffle = [0, 7, 4,1,8,5,2,9,6,3]
        actual_shuffle = shuffle(deck, sequence)

        self.assertEqual(actual_shuffle, expected_shuffle)

    def test_given_one(self):

        deck = list(range(0, 10))

        sequence = ['deal with increment 7','deal into new stack','deal into new stack']

        expected_shuffle = [0,3,6,9,2,5,8,1,4,7]
        actual_shuffle = shuffle(deck, sequence)
        self.assertEqual(actual_shuffle, expected_shuffle)

    def test_given_two(self):

        deck = list(range(0, 10))

        sequence = ['cut 6','deal with increment 7', 'deal into new stack']

        expected_shuffle = [3,0,7,4,1,8,5,2,9,6]
        actual_shuffle = shuffle(deck, sequence)
        self.assertEqual(actual_shuffle, expected_shuffle)

    def test_given_three(self):

        deck = list(range(0, 10))

        sequence = ['deal with increment 7', 'deal with increment 9', 'cut -2']

        expected_shuffle = [6,3,0,7,4,1,8,5,2,9]
        actual_shuffle = shuffle(deck, sequence)
        self.assertEqual(actual_shuffle, expected_shuffle)

    def test_given_four(self):

        deck = list(range(0, 10))

        sequence = ['deal into new stack', 'cut -2', 'deal with increment 7', 'cut 8', 'cut -4', 'deal with increment 7', 'cut 3', 'deal with increment 9', 'deal with increment 3', 'cut -1']

        expected_shuffle = [9,2,5,8,1,4,7,0,3,6]
        actual_shuffle = shuffle(deck, sequence)
        self.assertEqual(actual_shuffle, expected_shuffle)

if __name__ == '__main__':
    unittest.main()