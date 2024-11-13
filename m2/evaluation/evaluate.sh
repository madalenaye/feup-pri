#!/bin/bash
# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0  <query_response_eval_trec.txt> <qrels_file_in.txt> <qrels_trec_file_out.txt> <output_image>"
    exit 1
fi

# Assign input arguments to variables
RESULTS_FILE=$1
QRELS_FILE=$2
TEMP_TREC_TXT_FILE=$3
OUTPUT_IMAGE=$4



# Process the qrels file
cat "$QRELS_FILE" | ./qrels2trec.py > "$TEMP_TREC_TXT_FILE"

# Evaluate the results
trec_eval "$TEMP_TREC_TXT_FILE" "$RESULTS_FILE"

# Plot the precision-recall curve
cat "$RESULTS_FILE" | ./plot_pr.py --qrels "$TEMP_TREC_TXT_FILE" --output "$OUTPUT_IMAGE"

echo "Evaluation and plotting completed successfully."