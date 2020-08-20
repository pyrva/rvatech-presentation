from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def main():

    pd.read_csv(
        Path(__file__).parent / "tweets.csv",
        names=['date', 'tweet']
    ).groupby('date').size().to_frame('tweets').plot.bar(rot=0, legend=None)

    plt.xlabel("Date")
    plt.ylabel("Tweets")
    plt.title("Tweets using #PyRVA")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
