# Run the query and process the results
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <query_folder> <complex|simple>"
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
esac

./query_solr.py --query "$1/query_$2.json" --uri http://localhost:8983/solr --collection episodes | \
./solr2trec.py --query-id $ID > "$1/results_$2_trec.txt"

