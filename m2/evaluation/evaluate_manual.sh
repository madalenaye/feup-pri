# Run the query and process the results
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <query_file_in.json> <response_eval_trec_out.txt>"
    exit 1
fi

QUERY_FILE=$1
RESULTS_FILE=$2

./query_solr.py --query "$QUERY_FILE" --uri http://localhost:8983/solr --collection episodes | \
./solr2trec.py > "$RESULTS_FILE"

