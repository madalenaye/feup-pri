# Run the query and process the results
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <query_folder>"
    exit 1
fi

case "$1" in
   "steal") ID=1
   ;;
   "party") ID=2
   ;;
   "ashBattle") ID=3
   ;;
   "mega") ID=4
   ;;
   "angry") ID=5
   ;;
   "stealneed") ID=6
   ;;
   "partyneed") ID=7
   ;;
esac

python3 query_rerank.py --query "$1/query_rerank.json" --uri http://localhost:8983/solr --collection episodes | \
python3 solr2trec.py --query-id $ID > "$1/results_rerank_trec.txt"

