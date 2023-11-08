# Quantcast_Coding_Task
Quantcast SWE Internship Summer 2024 Coding Task

The coding task is written in Python. The main program is written in the file called `most_active_cookie.py`. The testing file, `most_active_cookie_test.py`, has ten tests evaluating incorrect formatting, non-existent files, correct solutions, and more. 

### My Thinking Process

I created a class called `Most_Active_Cookie` because I wanted to abstract away most of the underlying code and make it easy and intuitive for others to use. First, you make a `Most_Active_Cookie` object and load a CSV file into the object with `object_name.load_data(file)`. Then, we can find the most active cookie for a specified day by doing `object_name.find_active_cookie(target_date)`. 

By having a `load` method, we can continue to use the same object when doing computation, instead of making a new one every time we want to analyze a different CSV file. The `load` method first checks if the input file is a CSV file, then stores the data from the CSV file into the class attributes. We can do this because the instructions state that we have enough memory to store the contents of the whole file. 

The `find_active_cookie` method uses binary search to find all the indices that have their date equal to that of the target date. We use binary search because the log file is sorted by timestamp, which means our search takes $O(\log n)$, instead of iterating throughout the entire log file, which takes $O(n)$. With binary search, our memory usage is also constant, $O(1)$, as we don't use any data structure to store duplicate data. We could use hashmaps to store which ID appears the most often, but we still need to iterate through the items in the hashmap to find the highest frequency (and it takes up more memory), so it's better to stick with binary search when looking for the target date within the log file. 

Currently, the directions suggest that we are looking up only one date. We have to load the data, which takes $O(n)$ plus an additional $O(\log n)$ to do binary search and look for the date in the log. So, the final time complexity for looking up **one date** after loading is:
$$O(n + \log n)$$

Now, this may seem inefficient when only looking for one date. Since we are only analyzing **one** date, there is no point in storing the data. Instead, we can find the most active cookie by simply iterating through the entire log once, which takes $O(n)$. However, part of the assignment is to create **extendable** code, and I am assuming it's very reasonable to assume more date inputs could be given. 

Say we have $m$ dates instead of the previous one date input. If we use our current method, the time complexity would be this:
$$O(n + m \log n)$$

This is because we load the data once, $O(n)$, and perform $m$ binary searches, which we know takes $O(\log n)$. But if we use the naive method, we instead get this time complexity:
$$O(mn)$$
This is because we iterate through the entire log file $m$ times, and we know that iterating through the entire log file takes $O(n)$. 

Now, is it true we can still find the most active cookie for one date while loading the data? Absolutely. However, I believe the code quality will suffer because of that (juggling loading data and finding the most active cookie). Though it would be a simple fix, I decided not to so that other programmers would have an easy time reading and understanding the code (after all, I used OOP to make it easier to understand). 

Note that I included a file called `sorted_mega_tester.csv`, which is a file that resembles the original cookie log data but is extended to 1000 rows. Though I did not include any tests for this file in my `most_active_cookie_test.py` (My tests only utilize the original cookie log file), I used it to test my program on the side and it seemed to work! Please feel free to utilize `most_active_cookie_test.py` however you see fit.

That is my explanation for the program I have written! Thank you so much :)

