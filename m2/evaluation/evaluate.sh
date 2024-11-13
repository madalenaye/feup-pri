#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 5 ]; then
    echo "Usage: $0 <query_file_in.json> <response_file_trec_out.txt> <qrels_file_in.txt> <qrels_trec_file_out.txt> <output_image>"
    exit 1
fi

# Assign input arguments to variables
QUERY_FILE=$1
RESULTS_FILE=$2
QRELS_FILE=$3
TEMP_TREC_TXT_FILE=$4
OUTPUT_IMAGE=$5

# Run the query and process the results
./query_solr.py --query "$QUERY_FILE" --uri http://localhost:8983/solr --collection episodes | \
./solr2trec.py > "$RESULTS_FILE"

# Check if the RESULTS_FILE was created successfully
if [ ! -f "$RESULTS_FILE" ]; then
    echo "Error: Results file $RESULTS_FILE was not created."
    exit 1
fi

# Run the keep_code_from_response.py script
python3 keep_code_from_response.py "$RESULTS_FILE"

# Check if the keep_code_from_response.py script ran successfully
if [ $? -ne 0 ]; then
    echo "Error: keep_code_from_response.py script failed."
    exit 1
fi

# Process the qrels file
cat "$QRELS_FILE" | ./qrels2trec.py > "$TEMP_TREC_TXT_FILE"

# Evaluate the results
trec_eval "$TEMP_TREC_TXT_FILE" "$RESULTS_FILE"

# Plot the precision-recall curve
cat "$RESULTS_FILE" | ./plot_pr.py --qrels "$TEMP_TREC_TXT_FILE" --output "$OUTPUT_IMAGE"

echo "Evaluation and plotting completed successfully."