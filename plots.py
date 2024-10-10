from matplotlib import pyplot as plt
from wordcloud import WordCloud


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