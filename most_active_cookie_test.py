import sys

import unittest
from io import StringIO
import sys
from most_active_cookie import main

# command: python -m unittest .\most_active_cookie_test.py


class Most_Active_Cookie_Test(unittest.TestCase):
    def test_incorrectly_formatted_date(self):
        """
        Test case to check if the script raises a ValueError for incorrectly formatted date input.
        """
        sys.argv = ['most_active_cookie.py', 'cookie_log.csv',
                    '-d', '2021-5-1']  # date should be '2021-05-01'
        with self.assertRaises(ValueError):
            main()

    def test_non_csv_file_input(self):
        """
        Test case to check if the script raises a ValueError for a file_path input that is not a CSV file.
        """
        sys.argv = ['most_active_cookie.py', 'most_active_cookie_test.py',
                    '-d', '2021-05-01']  # CSV file doesn't exist
        with self.assertRaises(ValueError):
            main()

    # NOTE: THE FOLLOWING THREE TESTS PRODUCE SOME SORT OF "ERROR MESSAGE", BUT THAT IS WHAT WE ARE TESTING FOR
    # ALL TESTS PASS!!!

    def test_no_file_input(self):
        """
        Test case to check if the script raises a ValueError for a nonexistant file_path input.
        """
        sys.argv = ['most_active_cookie.py', '-d',
                    '2021-05-01']  # no file given
        with self.assertRaises(SystemExit):
            main()

    def test_no_date_input_one(self):
        """
        Test case to check if the script raises a ValueError for a nonexistant file_path input.
        """
        sys.argv = ['most_active_cookie.py',
                    'cookie_log.csv', '-d']  # no date input (flag inputted)
        with self.assertRaises(SystemExit):
            main()

    def test_no_date_input_two(self):
        """
        Test case to check if the script raises a ValueError for a nonexistant file_path input.
        """
        sys.argv = ['most_active_cookie.py',
                    'cookie_log.csv']  # no date input (flag also not inputted)
        with self.assertRaises(SystemExit):
            main()

    def test_incorrectly_formatted_file_input(self):
        """
        Test case to check if the script raises a FileNotFoundError for a non-existing CSV file.
        """
        sys.argv = ['most_active_cookie.py', 'does_not_exist.csv',
                    '-d', '2021-05-01']  # CSV file doesn't exist
        with self.assertRaises(FileNotFoundError):
            main()

    def test_nonexistent_date_in_csv(self):
        """
        Test case to check if the script raises a ValueError when the specified date does not exist in the CSV file.
        """
        sys.argv = ['most_active_cookie.py', 'cookie_log.csv',
                    '-d', '2021-05-01']  # Date doesn't exist in the file
        with self.assertRaises(ValueError):
            main()

    def test_prints_correct_answer_one(self):
        """
        Test case to check if the script correctly prints the most active cookies for a given date.
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        sys.argv = ['most_active_cookie.py',
                    'cookie_log.csv', '-d', '2018-12-08']
        main()

        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        expected_output = """SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n"""

        self.assertEqual(actual_output, expected_output)

    def test_prints_correct_answer_two(self):
        """
        Test case to check if the script correctly prints the most active cookies for a given date.
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        sys.argv = ['most_active_cookie.py',
                    'cookie_log.csv', '-d', '2018-12-09']
        main()

        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        expected_output = """AtY0laUfhglK3lC7\n"""

        self.assertEqual(actual_output, expected_output)

    def test_prints_correct_answer_three(self):
        """
        Test case to check if the script correctly prints the most active cookies for a given date.
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        sys.argv = ['most_active_cookie.py',
                    'cookie_log.csv', '-d', '2018-12-07']
        main()

        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        expected_output = """4sMM2LxV07bPJzwf\n"""

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
