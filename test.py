import assignment4
import unittest

class TestSequence(unittest.TestCase):

    def test_possible(self):
        """
        This function test the count kmers function
        """
        self.assertEqual(assignment4.count_kmers('ATTTGGATT', 2), 8)
        self.assertRaises(ValueError, assignment4.count_kmers,'',2)
        self.assertRaises(ValueError, assignment4.count_kmers,'ATTTGGATT',0)
        self.assertEqual(assignment4.count_kmers('AAAAAAAAA', 2), 8)

    def test_observe(self):
        """
        This function test the count data frame function
        """
        self.assertEqual(len(assignment4.count_df('ATTTGGATT')), 9)
        self.assertEqual(len(assignment4.count_df('')), 0)
        self.assertEqual(assignment4.count_df('AAAAAAAAA')['observed'].sum(), 9)
        self.assertEqual(assignment4.count_df('AAAAAAAAA')['posibility'].sum(),40)

    def test_print_df(self):
        """
        This function test the linguistic_complexity function
        """
        self.assertEqual(assignment4.linguistic_complexity(assignment4.count_df('ATTTGGATT')) ,0.875 )
        self.assertRaises(ValueError, assignment4.linguistic_complexity,assignment4.count_df(''))

    def test_datacheck(self):
        """
        This function test the data check function 
        """
        self.assertEqual(assignment4.datacheck(''), False)
        self.assertEqual(assignment4.datacheck('AWCT'), False)
        self.assertEqual(assignment4.datacheck('ACTG'), True)



if __name__ == '__main__':
    unittest.main()
