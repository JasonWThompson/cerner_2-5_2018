# timetravel.py
# Author: Jason W. Thompson
# Commentary: Oh shoot! I was so busy watching WWE's "Hell in a Cell" on the WWE Network that I completley forgot to do
# day four of the cerner_2^5_2018. How will I ever get the coveted 2^5 sticker and the "most programming languages"
# sticker??? What would New Japan Pro Wrestling's Kushida do!? Go BACK IN TIME!
# (Queue some "Huey Lewis and the News" music). 
# Nothing's more productive than time travel after all. This python script will change the date of the last commit to
# appear that it happened yesterday.
# I don't know Python, so I leveraged quite a bit of help from: 
# https://stackoverflow.com/questions/15344710/get-yesterdays-date-in-python-dst-safe

from datetime import datetime, timedelta

dt_naive = datetime.today() - timedelta(days=1)

print(dt_naive)