import argparse
import csv


class Most_Active_Cookie:
    """
    A class to represent a data structure that can print the most active cookies for a given day
    """

    def __init__(self):
        """
        Constructs necessary attributes for the Most_Active_Cookie object. 
        Note: self.cookies, self.dates, and self.times correspond with each other
        based on indices. For example, self.cookies[0], self.dates[0], and self.times[0]
        all correspond with each other, as will be described in the load_data class method.

        Parameters:
            self.cookies (list[str]): list of cookies, which is a 16 character string
            self.dates (list[str]): list of dates, which is in the format YYYY-MM-DD
            self.times (list[str]): list of times, which is in the format HH:MM:SS+00:00 (timezone UTC)
        """
        self.cookies = []
        self.dates = []
        self.times = []  # Note: not utilized in current implementation, may be used in expansion

    @staticmethod
    def check_file_csv(file_path: str) -> None:
        """
        Raises an error if the file provided by the inputted file_path is NOT a CSV file.

        Args:
            file_path (str): string representing the path to a CSV file

        Raises:
            ValueError: if file provided by inputted file_path is NOT a CSV file.
        """

        if file_path[-4:] != ".csv":
            raise ValueError("Provided file_path is not a CSV file.")

    @staticmethod
    def check_valid_date(target_date: str) -> bool:
        """ 
        Returns True if the input string is a valid date, False otherwise.
        A valid date is a string with the format YYYY-MM-DD. 

        Args:
            date_str (str): A valid input is a string with the format YYYY-MM-DD.
            The function recognizes correct leap year dates. 

        Returns:
            bool: True if string input is a valid date. False otherwise.
        """
        try:
            year, month, day = target_date.split('-')

            # ensure length of year, month, and day match YYYY-MM-DD
            # for example: ensures no YYYY-M-D -> consistency
            if len(year) != 4 or len(month) != 2 or len(day) != 2:
                return False

            year, month, day = int(year), int(month), int(day)

            # April, June, September, November
            months_with_30_days = {4, 6, 9, 11}

            if month < 1 or month > 12:
                return False

            if day < 1:
                return False

            if month in months_with_30_days and day > 30:
                return False

            # February -> leap years
            if month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # leap year rule
                    if day > 29:
                        return False
                else:
                    if day > 28:
                        return False

            # Rest: months with 31 days
            if month not in months_with_30_days and day > 31:
                return False

            return True  # passed all checks, return True

        # deals with erroneous inputs not handled by above logic (alphabetical inputs, for example)
        except (ValueError, IndexError):
            return False

    def binary_search_indices(self, target_date: str) -> (int, int):
        """
        Looks for target_date in sorted_dates using binary search. Returns the 
        range of indices at which the target date appears in the list

        Args:
            target_date (str): The date string you want to search for within the list

        Returns:
            (int, int): Range of indices at which the target date appears in sorted_dates. Returns (-1, -1)
                if target date doesn't appear in sorted_dates.
        """
        left, right = 0, len(self.dates) - 1
        start_index, end_index = -1, -1

        # binary search
        while left <= right:
            # find midpoint and corresponding middle date
            mid = (right + left) // 2
            mid_date = self.dates[mid]

            # found target date
            if mid_date == target_date:
                start_index = mid
                end_index = mid

                # find the occurrences to the right
                while start_index > 0 and self.dates[start_index - 1] == target_date:
                    start_index -= 1

                # find the occurrences to the left
                while end_index < len(self.dates) - 1 and self.dates[end_index + 1] == target_date:
                    end_index += 1

                return start_index, end_index  # return the range of indices

            # did not find target date
            elif mid_date < target_date:
                right = mid - 1
            else:
                left = mid + 1

        return -1, -1  # Target date not found in the list

    def load_data(self, file_path: str) -> None:
        """
        Loads the data from CSV file and stores it into class attributes. Each row
        of the CSV contains a cookie, date, and time data, and they are stored in their
        respective class attributes. Hence, self.cookies, self.dates, and self.times 
        correspond with each other based on indices

        Args:
            file_path (str): string representing the path to a CSV file
        """

        # check if input file_path is a CSV file
        Most_Active_Cookie.check_file_csv(file_path)

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.cookies.append(row['cookie'])

                # split timestamp into date and time
                date, time = row['timestamp'].split('T')
                self.dates.append(date)
                self.times.append(time)  # not used currently

    def find_active_cookie(self, target_date: str) -> None:
        """
        Find the most active cookie(s) on the given target date in the class attribute data

        Args:
            target_date (str): string representing a date in the YYYY-MM-DD format

        Raises:
            ValueError: ValueError: If target_date cannot be found in file provided by file_path

        Returns:
            None: prints each cookie that appears the most line by line            
        """
        Most_Active_Cookie.check_valid_date(target_date)

        start, end = self.binary_search_indices(target_date)

        if start == -1:  # could not find target_date in sorted_dates
            raise ValueError("Input date cannot be found in log.")

        # cookie_frequency dictionary: key -> cookie ID, value -> number of occurances
        cookie_frequency = {}
        for i in range(start, end + 1):  # end + 1 because inclusive
            if self.cookies[i] in cookie_frequency:
                cookie_frequency[self.cookies[i]] += 1
            else:
                cookie_frequency[self.cookies[i]] = 1

        # calculate which cookies had max occurances
        output = []
        max = 0
        for key, value in cookie_frequency.items():
            if value > max:
                max = value
                output = [key]
            elif value == max:
                output.append(key)

        # print final results
        for i in output:
            print(i)


def main():
    """
    Command-Line Argument Parser
    file_path: required. path to CSV file containing cookie data
    -d or --date: required. date in YYYY-MM-DD format. Target_date to find in file provided by file_path
    """
    parser = argparse.ArgumentParser(
        description="Find the most active cookies on a specific date.")
    parser.add_argument("file_path", type=str,
                        help="Path to the CSV file containing cookie data.")
    parser.add_argument("-d", "--date", type=str,
                        required=True, help="Date in YYYY-MM-DD format.")

    args = parser.parse_args()

    cookie_finder = Most_Active_Cookie()
    cookie_finder.load_data(args.file_path)
    cookie_finder.find_active_cookie(args.date)


if __name__ == "__main__":
    main()
