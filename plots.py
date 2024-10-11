from matplotlib import pyplot as plt
from wordcloud import WordCloud
import re
import matplotlib.pyplot as plt


def plot_word_cloud(df,column):
    all_plot = ' '.join(df[column].astype(str))  
    
    # Create a word cloud
    wordcloud = WordCloud(width = 800, height = 800, 
                    background_color ='white', 
                    ).generate(all_plot)
    plt.figure(figsize = (10, 10), facecolor = None)
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.axis("off")
    plt.show()

def plot_word_count(df, file):
    hist = df.hist(column="Plot Word Count")
    hist[0][0].get_figure().savefig(file)

def plot_broadcast_delay(df, file):
    df = df.sort_values('First broadcast Japan', ascending=True)
    #plt.plot(df['First broadcast Japan'], df['Broadcast Delay'])
    #plt.xticks(rotation='vertical')
    plot = df.plot(x="First broadcast Japan", y="Broadcast Delay")
    plot.get_figure().savefig(file)

def plot_major_events(df, file):
    print(df["Major events"].apply(lambda x: len(x)))
    hist = df["Major events"].apply(lambda x: len(x)).hist()
    hist.get_figure().savefig(file)

def get_name_re(name):
    words = name.split(' ')
    if len(words) == 1:
        return name
    elif name.find("'") != -1:
        return None
    else:
        return f"({name}|{words[0]})"

def add_occurences(row, ep):
    #print(row['re'])
    #print(re.findall(re.compile(row['re']), "Ash found Jessie amazing"))
    row['occ'] += len(re.findall(re.compile(row['re']), ep['Plot']))
    return row

def plot_major_characters(episodes, characters, file):
    main_chars = characters[characters["Role"].apply(lambda x: re.search("main", x, re.IGNORECASE) is not None)][["Name"]]
    main_chars['re'] = main_chars['Name'].apply(lambda x: get_name_re(x))
    main_chars = main_chars.dropna()
    main_chars['occ'] = 0
    for index, episode in episodes.iterrows():
        main_chars = main_chars.apply(lambda x: add_occurences(x, episode), axis=1)
    plot = main_chars.plot.bar(x="Name", y="occ", rot=0)
    plot.get_figure().savefig(file)

def get_pokemon_name(name):
    idx = name.find('(')
    if idx == -1:
        return name
    else:
        return name[:idx-1]

def plot_type_representation(episodes, pokemon_json, file):
    types = {}
    for index, episode in episodes.iterrows():
        pokemons = list(map(lambda x: get_pokemon_name(x), episode["Characters"]["Pokemons"]))
        for pokemon in pokemons:
            if pokemon not in pokemon_json:
                print(pokemon)
                continue
            pokemon_obj = pokemon_json[pokemon]
            for type in pokemon_obj["Types"]:
                if type is not None:
                    types[type] = types.get(type, 0) + 1
    plt.bar(*zip(*types.items()))
    plt.savefig(file)