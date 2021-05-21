import json
# for turning strings into dates
from dateutil import parser
from pytz import timezone
# for making pretty graphs
import seaborn as sns
import matplotlib.pyplot as plt

import os
dirname = os.path.dirname(__file__)

def file(r_path):
  return os.path.join(dirname, r_path)

def main():
  count_map = {}
  for i in range(24):
    count_map[i] = 0

  with open(file('ed.json')) as data_file:
    data = json.load((data_file))
    for post in data:
      hour = get_hour(post['created_at'])
      count_map[hour] += 1
  make_bar_plot(count_map)

def get_hour(time_string):
    """
    Given a time string, returns the day of the week (in pacific time).
    >>> get_hour('2021-05-21T01:20:39.296044+10:00')
    'Thu'
    """
    date_time = parser.parse(time_string)
    # change to my timezone
    date_time = date_time.astimezone(timezone('US/Pacific'))
    # get the hour out of the time object
    return date_time.hour

def make_bar_plot(count_map):
    """
    Turns a dictionary (where values are numbers) into a bar plot.
    Labels gives the order of the bars! Uses a package called seaborn
    for making graphs.
    """
    # turn the counts into a list
    counts = []
    # loop over the labels, in order
    for label in count_map:
        counts.append(count_map[label])
    # format the data in the way that seaborn wants
    data = {
        'x':list(count_map.keys()),
        'y':counts
    }
    sns.barplot(x = 'x',y = 'y', data= data)
    plt.savefig(file("plot.png"))

main()