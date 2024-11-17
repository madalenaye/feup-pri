#!/bin/bash
# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0  <query_name> <complex|simple>"
    exit 1
fi

# Assign input arguments to variables
QUERY_NAME=$1
QUERY_TYPE=$2

# Process the qrels file
cat "$1/qrels.txt" | ./qrels2trec.py > "$1/qrels_trec.txt"

# Evaluate the results
trec_eval "$1/qrels_trec.txt" "$1/results_$2_trec.txt"

# Plot the precision-recall curve
cat "$1/results_$2_trec.txt" | ./plot_pr.py --qrels "$1/qrels_trec.txt" --output "$1/prec_rec_$2.png"

echo "Evaluation and plotting completed successfully."