""" A basic graph """

import csv
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

from pyrva_talk.twitter.api import get_tweets

def main():
    data = get_data()
    labels, values = process_data(data)
    draw_barchart(labels, values)


def get_data():
    """ get the data from csv """
    base_path = Path(__file__)
    data_path = base_path.parent / "tweets.csv"
    with data_path.open() as f:
        reader = csv.DictReader(f, ["date", "tweet"])
        lines = [line for line in reader]

    return lines


def get_twitter_data():
    """ Get data from twitter instead """
    tweets = get_tweets('#PyCon', start_date='2020-07-01')
    rows = [
        {'date': tweet.created_at.strftime('%x'), 'tweet':tweet.full_text} 
        for tweet in tweets
    ]
    return rows


def process_data(data):
    """ bin data into day & tweet count """
    labels = list(set(row["date"] for row in data))
    labels.sort()
    values = []
    for label in labels:
        count = sum(1 for row in data if row["date"] == label)
        values.append(count)
    return labels, values


def draw_barchart(labels, values):
    """ draw a bar chart """
    plt.bar(labels, values, color="blue")
    plt.xlabel("Date")
    plt.ylabel("Tweets")
    plt.title("Tweets using #PyCon")
    plt.show()


if __name__ == "__main__":
    main()
