#!/bin/bash
# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0  <query_folder> <complex|simple>"
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

# Process the qrels file
cat "$1/qrels.txt" | ./qrels2trec.py --query-id $ID > "$1/qrels_trec.txt"

# Evaluate the results
trec_eval "$1/qrels_trec.txt" "$1/results_$2_trec.txt"

# Plot the precision-recall curve
cat "$1/results_$2_trec.txt" | ./plot_pr.py --qrels "$1/qrels_trec.txt" --output "$1/prec_rec_$2.png"

echo "Evaluation and plotting completed successfully."