import unittest
from part2 import shuffle, mod_inverse

class TestProblem22(unittest.TestCase):

    def test_part_1_actual_input(self):

        deck = 10007

        sequence = ['deal with increment 74','deal into new stack','deal with increment 67','cut 6315','deal with increment 15','cut -8049','deal with increment 69','cut 2275','deal with increment 25','cut 4811','deal with increment 47','cut -9792','deal with increment 26','cut -3014','deal with increment 47','cut -1093','deal with increment 39','cut -5322','deal with increment 14','cut -7375','deal with increment 16','cut 9627','deal into new stack','cut 1632','deal into new stack','cut -2904','deal with increment 69','cut -3328','deal with increment 60','cut 7795','deal into new stack','deal with increment 37','cut -4238','deal with increment 19','cut -3170','deal with increment 45','cut 8631','deal with increment 64','cut -2380','deal with increment 59','cut -2802','deal with increment 19','cut -3369','deal with increment 45','deal into new stack','deal with increment 71','cut 5452','deal with increment 73','cut -6609','deal with increment 33','cut 1892','deal with increment 5','cut 1395','deal into new stack','cut -8514','deal with increment 46','deal into new stack','deal with increment 15','cut 3963','deal with increment 2','cut -2965','deal into new stack','cut 640','deal with increment 13','cut 8889','deal with increment 62','cut 8331','deal with increment 49','cut 6169','deal with increment 71','deal into new stack','deal with increment 33','cut 6342','deal with increment 52','cut 2875','deal with increment 39','cut 4283','deal with increment 19','cut 4102','deal with increment 57','deal into new stack','cut -7801','deal with increment 38','cut 4273','deal with increment 58','cut -2971','deal with increment 46','deal into new stack','cut 8043','deal with increment 52','cut -7108','deal with increment 21','cut 507','deal with increment 70','cut -8658','deal with increment 64','cut 7213','deal into new stack','deal with increment 61','cut 9439',]

        expected_position_of_2019 = 3939

        actual_pair = shuffle(deck, sequence)

        current_pos = actual_pair[0]
        i = 0

        while (current_pos != 2019):
            i += 1
            current_pos += actual_pair[1]
            current_pos %= deck

        self.assertEqual(i, expected_position_of_2019)

    def test_try_stuff(self):

        mod = 119315717514047

        sequence = ['deal with increment 74','deal into new stack','deal with increment 67','cut 6315','deal with increment 15','cut -8049','deal with increment 69','cut 2275','deal with increment 25','cut 4811','deal with increment 47','cut -9792','deal with increment 26','cut -3014','deal with increment 47','cut -1093','deal with increment 39','cut -5322','deal with increment 14','cut -7375','deal with increment 16','cut 9627','deal into new stack','cut 1632','deal into new stack','cut -2904','deal with increment 69','cut -3328','deal with increment 60','cut 7795','deal into new stack','deal with increment 37','cut -4238','deal with increment 19','cut -3170','deal with increment 45','cut 8631','deal with increment 64','cut -2380','deal with increment 59','cut -2802','deal with increment 19','cut -3369','deal with increment 45','deal into new stack','deal with increment 71','cut 5452','deal with increment 73','cut -6609','deal with increment 33','cut 1892','deal with increment 5','cut 1395','deal into new stack','cut -8514','deal with increment 46','deal into new stack','deal with increment 15','cut 3963','deal with increment 2','cut -2965','deal into new stack','cut 640','deal with increment 13','cut 8889','deal with increment 62','cut 8331','deal with increment 49','cut 6169','deal with increment 71','deal into new stack','deal with increment 33','cut 6342','deal with increment 52','cut 2875','deal with increment 39','cut 4283','deal with increment 19','cut 4102','deal with increment 57','deal into new stack','cut -7801','deal with increment 38','cut 4273','deal with increment 58','cut -2971','deal with increment 46','deal into new stack','cut 8043','deal with increment 52','cut -7108','deal with increment 21','cut 507','deal with increment 70','cut -8658','deal with increment 64','cut 7213','deal into new stack','deal with increment 61','cut 9439',]

        iterations = 101741582076661

        (offset_diff, increment_mul) = shuffle(mod, sequence)

        # increment_mul is multiple by a constant each time so we can power mod to find the number after the required sequences
        increment = pow(increment_mul, 101741582076661, 119315717514047)

        # offset = offset_diff * (1 + increment_mul + increment_mul**2 + ... + increment_mul**(n-1))
        # geometric series
        offset = offset_diff * (1 - pow(increment_mul, iterations, mod)) * mod_inverse(1 - increment_mul, mod)

        offset = pow(offset, 1, mod)

        ans = offset + (increment * 2020)

        print(pow(ans, 1, mod))


        


        

if __name__ == '__main__':
    unittest.main()