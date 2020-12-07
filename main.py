from test import *

asked_series = "The Green Archer"


#read_episode = open_tsv_file("title.episode.tsv")
read_title = open_tsv_file("title.series.tsv")
#read_ratings = open_tsv_file("title.ratings.tsv")


index_titles = create_dict_from_tsv(read_title, 1, 0)
#dict_ratings = create_dict_from_tsv(read_ratings, 0, 1)

asked_id = index_titles[asked_series]
print(asked_id)

'''
list_data = []
for row_episode in read_episode:
    if row_episode[1] == asked_id: 
        if row_episode[0] == 'tconst':
            row_episode.insert(2, 'serieTitle')
        for i in index_titles:
            if i == row_episode[1]:
                row_episode.insert(2, index_titles[i])
        for i in dict_ratings:
            if i == row_episode[0]:
                row_episode.append(dict_ratings[i])
                key_list = ['episode_id', 'title_id', 'title', 'season_nb', 'episode_nb', 'average_rate']
                list_data.append(dict(zip(key_list, row_episode)))

for k in list_data:
    print(list_data)

#list_data = sorted(list_data, key=lambda k: (k['title'], k['episode_nb']))
#list_data = convert_dicts_to_lists(list_data)
'''