# Import packages to use
import twint
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Get the last months bitcoin tweets
# Note the limit doesn't always work as expected (it may be counting tweets to limit but also displaying replies?)

c = twint.Config()
c.Hide_output = True

c.Search = '#bitcoin'
c.Since = '2022-03-01 00:00:00'
c.Output_csv = True
c.Output = 'bitcoin-tweets.csv'

twint.run.Search(c)