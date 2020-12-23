from functions import find_id_by_title
from functions import find_episodes_by_series
from functions import find_rated_episodes


def create_grades_table(title):
    series_id = find_id_by_title(title)
    episodes_data = find_episodes_by_series(series_id)
    episodes_id = []
    for ep in episodes_data:
        episodes_id.append(ep[0])
    rated_episodes = find_rated_episodes(episodes_id)
    for ep in episodes_data:
        for id in rated_episodes:
            if ep[0] == id[0]:
                ep.append(id[1])
        if len(ep) <= 3:
            ep.append("")
        del (ep[0])

    dict_data = []
    keys = ["season", "episode", "grade"]
    for ep in episodes_data:
        dict_data.append(dict(zip(keys, ep)))
    dict_data = sorted(dict_data, key=lambda k: k["season"])
    list_data = []
    for dictionary in dict_data:
        list_data.append(list(dictionary.values()))

    data = []
    seasons = []
    nb_eps = []
    for ep in list_data:
        seasons.append(int(ep[0]))
        nb_eps.append(int(ep[1]))
    nb_eps = sorted(set(nb_eps))
    data.append([""]+sorted(set(seasons)))

    for i in nb_eps:
        grades_list = [str(i)]
        for ep in list_data:
            if ep[1] == str(i):
                grades_list.append(ep[2])
        data.append(grades_list)
        grades_list = []
    return(data)