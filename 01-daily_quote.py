#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date

quotes = [
    'Never spend 5 hours on a manual task that you could spend 5 days failing to automate.',
    'When you are dead, you dont know that you are dead.',
    'A wise man can change his mind.',
    'Cauliflower is nothing but cabbage with a college education.',
    "'I didnt say half the things people say I did.' -Albert Einstein",
    'Everybody has a plan until they get punched in the mouth'
]


def get_quote_of_the_day(quotes):
    todays_quote = None
    seed = str(date.today())
    random.seed(seed)
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt
