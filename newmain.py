import argparse
import scrape
import process
import plots

parser = argparse.ArgumentParser(prog="PRI - Milestone 1 Pipeline")

parser.add_argument("-c", "--character-file", default="documents/characters.json")
parser.add_argument("-e", "--episode-file", default="documents/episodes.json")
parser.add_argument("-s", "--skip-scraping", action="store_true")
parser.add_argument("-b", "--broadcast-delay", nargs='?', const="broadcastfig.png")
parser.add_argument("-w", "--word-count", nargs='?', const="wordcountfig.png")
parser.add_argument("-m", "--major-events", nargs='?', const="eventsfig.png")
parser.add_argument('-o', "--character-occurences", nargs='?', const="characterfig.png")

args = parser.parse_args()
print(args)
if args.skip_scraping == False:
    scrape.scrape_characters(args.character_file)
    scrape.scrape_episodes(args.episode_file)

character_df = process.dataset_processing_characters(args.character_file)
episode_df = process.dataset_processing_series(args.episode_file)

if args.broadcast_delay:
    plots.plot_broadcast_delay(episode_df, args.broadcast_delay)

if args.word_count:
    plots.plot_word_count(episode_df, args.word_count)

if args.major_events:
    plots.plot_major_events(episode_df, args.major_events)

if args.character_occurences:
    plots.plot_major_characters(episode_df, character_df, args.character_occurences)