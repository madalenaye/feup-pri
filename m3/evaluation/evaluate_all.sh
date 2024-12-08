#!/bin/bash

# Process the qrels file
cat "ashBattle/qrels.txt" | ./qrels2trec.py > "ashBattle/qrels_trec.txt"

# Evaluate the results
trec_eval "ashBattle/qrels_trec.txt" "ashBattle/results_simple_trec.txt"
trec_eval "ashBattle/qrels_trec.txt" "ashBattle/results_complex_trec.txt"

# Plot the precision-recall curve
cat "ashBattle/results_simple_trec.txt" | ./plot_pr.py --qrels "ashBattle/qrels_trec.txt" --output "ashBattle/prec_rec_simple.png"
cat "ashBattle/results_complex_trec.txt" | ./plot_pr.py --qrels "ashBattle/qrels_trec.txt" --output "ashBattle/prec_rec_complex.png"




# Process the qrels file
cat "mega/qrels.txt" | ./qrels2trec.py > "mega/qrels_trec.txt"

# Evaluate the results
trec_eval "mega/qrels_trec.txt" "mega/results_simple_trec.txt"
trec_eval "mega/qrels_trec.txt" "mega/results_complex_trec.txt"

# Plot the precision-recall curve
cat "mega/results_simple_trec.txt" | ./plot_pr.py --qrels "mega/qrels_trec.txt" --output "mega/prec_rec_simple.png"
cat "mega/results_complex_trec.txt" | ./plot_pr.py --qrels "mega/qrels_trec.txt" --output "mega/prec_rec_complex.png"




# Process the qrels file
cat "party/qrels.txt" | ./qrels2trec.py > "party/qrels_trec.txt"

# Evaluate the results
trec_eval "party/qrels_trec.txt" "party/results_simple_trec.txt"
trec_eval "party/qrels_trec.txt" "party/results_complex_trec.txt"

# Plot the precision-recall curve
cat "party/results_simple_trec.txt" | ./plot_pr.py --qrels "party/qrels_trec.txt" --output "party/prec_rec_simple.png"
cat "party/results_complex_trec.txt" | ./plot_pr.py --qrels "party/qrels_trec.txt" --output "party/prec_rec_complex.png"



# Process the qrels file
cat "steal/qrels.txt" | ./qrels2trec.py > "steal/qrels_trec.txt"

# Evaluate the results
trec_eval "steal/qrels_trec.txt" "steal/results_simple_trec.txt"
trec_eval "steal/qrels_trec.txt" "steal/results_complex_trec.txt"

# Plot the precision-recall curve
cat "steal/results_simple_trec.txt" | ./plot_pr.py --qrels "steal/qrels_trec.txt" --output "steal/prec_rec_simple.png"
cat "steal/results_complex_trec.txt" | ./plot_pr.py --qrels "steal/qrels_trec.txt" --output "steal/prec_rec_complex.png"


echo "Evaluation and plotting completed successfully."