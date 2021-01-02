import csv


def find_id_by_title(series_title):
    with open("title.series.tsv", "r") as file:
        data = csv.reader(file, delimiter="\t")

        for row in data:
            if clear(row[1]) == clear(series_title):
                return row[0], row[1]


def find_episodes_by_series(series_id):
    with open("title.episode.tsv", "r") as file:
        data = csv.reader(file, delimiter="\t")
        episodes = []
        for row in data:
            if row[1] == series_id:
                episodes.append([row[0], row[2], row[3]])
    return episodes


def find_rated_episodes(episodes_id):
    with open("title.ratings.tsv", "r") as file:
        data = csv.reader(file, delimiter="\t")

        rated_episodes = []
        for row in data:
            if row[0] in episodes_id:
                rated_episodes.append(row[:2])
        return rated_episodes


def clear(title):
    lower_title = title.lower()
    cleared_title = ''.join(e for e in lower_title if e.isalnum())
    return cleared_title
