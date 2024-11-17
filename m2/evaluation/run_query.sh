# Run the query and process the results
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <query_name> <complex|simple>"
    exit 1
fi

QUERY_NAME=$1
QUERY_TYPE=$2

./query_solr.py --query "$1/query_$2.json" --uri http://localhost:8983/solr --collection episodes | \
./solr2trec.py > "$1/results_$2_trec.txt"

