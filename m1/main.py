import argparse
import scrape
import process
import plots
import json
import utils
import character_correlation

parser = argparse.ArgumentParser(prog="PRI - Milestone 1 Pipeline")

parser.add_argument("--character-file", default="documents/characters.json")
parser.add_argument("--episode-file", default="documents/episodes.json")
parser.add_argument("--pokemon-file", default="documents/pokemons.json")
parser.add_argument("--scrape-characters", action="store_true")
parser.add_argument("--scrape-pokemon", action="store_true")
parser.add_argument("--scrape-episodes", action="store_true")
parser.add_argument("-b", "--broadcast-delay", nargs='?', const="broadcastfig.png")
parser.add_argument("-w", "--word-count", nargs='?', const="wordcountfig.png")
parser.add_argument("-m", "--major-events", nargs='?', const="eventsfig.png")
parser.add_argument('-o', "--character-occurences", nargs='?', const="characterfig.png")
parser.add_argument("-p", "--pokemon-types", nargs='?', const="typefig.png")
parser.add_argument("-c", "--word-cloud", nargs='?', const="wordcloud.png")
parser.add_argument("--scatter-episode-plot", nargs='?', const="scatterfig.png")
parser.add_argument("--correlation", nargs='?', const="jaccard_indexes.json")
parser.add_argument("--sentiment-analysis", nargs='?', const="sentiment.png")

args = parser.parse_args()
print(args)

if args.scrape_characters:
    scrape.scrape_characters(args.character_file)
if args.scrape_pokemon:
    scrape.scrape_pokemon(args.pokemon_file)
if args.scrape_episodes:
    scrape.scrape_episodes(args.episode_file)

character_df = process.dataset_processing_characters(args.character_file)
utils.save_df_as_json(character_df, utils.make_final_name(args.character_file))

episode_df = process.dataset_processing_series(args.episode_file)
utils.save_df_as_json(episode_df, utils.make_final_name(args.episode_file))

pokemon_df = process.dataset_processing_pokemon(args.pokemon_file)
utils.save_df_as_json(pokemon_df, utils.make_final_name(args.pokemon_file))

#with open(args.pokemon_file, "r") as file:
#    pokemon_json = json.load(file)

if args.broadcast_delay:
    plots.plot_broadcast_delay(episode_df, args.broadcast_delay)

if args.word_count:
    plots.plot_word_count(episode_df, args.word_count)

if args.major_events:
    plots.plot_major_events(episode_df, args.major_events)

if args.character_occurences:
    plots.plot_major_characters(episode_df, character_df, args.character_occurences)

if args.pokemon_types:
    plots.plot_type_representation(episode_df, json.loads(pokemon_df.to_json(orient="index")), args.pokemon_types)

if args.word_cloud:
    plots.plot_word_cloud(episode_df, "Plot", args.word_cloud)

if args.scatter_episode_plot:
    plots.plot_scatter_events(episode_df, args.scatter_episode_plot)

if args.correlation:
    character_correlation.get_correlations(character_df, episode_df, args.correlation)

if args.sentiment_analysis:
    plots.plot_sentiment(pokemon_df, "biology", args.sentiment_analysis)