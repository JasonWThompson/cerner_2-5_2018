#!/usr/bin/env python3

# timetravel.py
# Author: Jason W. Thompson
# Commentary: Oh shoot! I was so busy watching WWE's "Hell in a Cell" on the WWE Network that I completley forgot to do
# day four of the cerner_2^5_2018. How will I ever get the coveted 2^5 sticker and the "most programming languages"
# sticker??? What would New Japan Pro Wrestling's Kushida do!? Go BACK IN TIME!
# (Queue some "Huey Lewis and the News" music). 
# Nothing's more productive than time travel after all. This python script will change the date of the last commit to
# appear that it happened yesterday.
# I don't know Python, so I leveraged quite a bit of help from the following: 
# https://stackoverflow.com/questions/15344710/get-yesterdays-date-in-python-dst-safe
# https://stackoverflow.com/questions/89228/calling-an-external-command-in-python
# And a shout out to "Code with Hugo" for the syntax on manipulating git checkin dates.
# https://codewithhugo.com/change-the-date-of-a-git-commit/

from datetime import datetime, timedelta
from subprocess import call

yesterday = datetime.today() - timedelta(days=1)

call(["git", "commit", "--amend", "--no-edit", "--date", str(yesterday)])