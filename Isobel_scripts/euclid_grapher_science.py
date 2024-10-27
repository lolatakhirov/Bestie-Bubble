#!/usr/bin/env python3

import pandas
import plotly.express as px

def euclid_grapher(distances, user_name):
    #distances needs to be pandas dataframe
    #user_name is name of person taking personality quiz as string
    return

similarity_dict = {}
jaccard_similarity = {}
gower_similarity = {}
with open('categorical_similarity.txt', 'r') as read_file:
    for line in read_file:
        line = line.rstrip()
        [name, jaccard, gower] = line.split('\t')
        similarity_dict[name] = {}
        similarity_dict[name]['Jaccard'] = float(jaccard)
        similarity_dict[name]['Gower'] = float(gower)
        jaccard_similarity[name] = float(jaccard)

similarity_dict['username']={}
similarity_dict['username']['Jaccard'] = 1
similarity_dict['username']['Gower'] = 1
jaccard_similarity['username'] = 1
sorted_sims = sorted(jaccard_similarity, key=jaccard_similarity.get, reverse=True)

sorted_dict = {}
for name in sorted_sims:
    sorted_dict[name] = {}
    sorted_dict[name]['Jaccard'] = similarity_dict[name]['Jaccard']
    sorted_dict[name]['Gower'] = similarity_dict[name]['Gower']


colors = ['black'] * len(sorted_dict)
colors[0] = 'magenta'
colors[1] = '#FFD700'
colors[2] = '#C0C0C0'
colors[3] = '#CD7F32'
colors[len(sorted_dict)-1] = "#8FC554"

markers = ['circle'] * len(sorted_dict)
markers[0] = 'star'

sizes = [5] * len(sorted_dict)
sizes[0] = 20

names = [''] * len(sorted_dict)
names[0] = sorted_sims[0] + " 🦄"
names[1] = sorted_sims[1] + " 🥇"
names[2] = sorted_sims[2] + " 🥈"
names[3] = sorted_sims[3] + " 🥉"
names[len(sorted_dict) -1] = sorted_sims[len(sorted_dict)-1] + " 🐸"

column_label = ['Jaccard','Gower']
similarities = pandas.DataFrame.from_dict(sorted_dict, orient='index', columns=column_label)
similarities['color'] = colors
similarities['marker'] = markers
similarities['y-axis'] = 0
similarities['size'] = sizes
similarities['name'] = names

fig1 = px.scatter(similarities, x='Gower', y='y-axis', color='color', color_discrete_map='identity', symbol='marker', symbol_map='identity', size='size', text='name')
fig1.update_traces(offsetgroup=0, textposition='top center')
fig1.write_image(f"images/{sorted_sims[0]}_gower_matches.png", scale=2)


fig2 = px.scatter(similarities, x='Jaccard', y='y-axis', color='color', color_discrete_map='identity', symbol='marker', symbol_map='identity', size='size', text='name')
fig2.update_traces(offsetgroup=0, textposition='top center')
fig2.write_image(f"images/{sorted_sims[0]}_jaccard_matches.png", scale=2)