import unittest
from part1 import shuffle

class TestProblem22Part1(unittest.TestCase):


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

    def test_part_1_actual_input(self):

        deck = list(range(0, 10007))

        sequence = ['deal with increment 74','deal into new stack','deal with increment 67','cut 6315','deal with increment 15','cut -8049','deal with increment 69','cut 2275','deal with increment 25','cut 4811','deal with increment 47','cut -9792','deal with increment 26','cut -3014','deal with increment 47','cut -1093','deal with increment 39','cut -5322','deal with increment 14','cut -7375','deal with increment 16','cut 9627','deal into new stack','cut 1632','deal into new stack','cut -2904','deal with increment 69','cut -3328','deal with increment 60','cut 7795','deal into new stack','deal with increment 37','cut -4238','deal with increment 19','cut -3170','deal with increment 45','cut 8631','deal with increment 64','cut -2380','deal with increment 59','cut -2802','deal with increment 19','cut -3369','deal with increment 45','deal into new stack','deal with increment 71','cut 5452','deal with increment 73','cut -6609','deal with increment 33','cut 1892','deal with increment 5','cut 1395','deal into new stack','cut -8514','deal with increment 46','deal into new stack','deal with increment 15','cut 3963','deal with increment 2','cut -2965','deal into new stack','cut 640','deal with increment 13','cut 8889','deal with increment 62','cut 8331','deal with increment 49','cut 6169','deal with increment 71','deal into new stack','deal with increment 33','cut 6342','deal with increment 52','cut 2875','deal with increment 39','cut 4283','deal with increment 19','cut 4102','deal with increment 57','deal into new stack','cut -7801','deal with increment 38','cut 4273','deal with increment 58','cut -2971','deal with increment 46','deal into new stack','cut 8043','deal with increment 52','cut -7108','deal with increment 21','cut 507','deal with increment 70','cut -8658','deal with increment 64','cut 7213','deal into new stack','deal with increment 61','cut 9439',]

        expected_position_of_2019 = 3939

        shuffled_deck = shuffle(deck, sequence)
        actual_position_of_2019 = shuffled_deck.index(2019)

        self.assertEqual(actual_position_of_2019, expected_position_of_2019)

if __name__ == '__main__':
    unittest.main()