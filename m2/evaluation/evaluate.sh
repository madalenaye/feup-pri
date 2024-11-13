./query_solr.py --query steal/query_complex.json --uri http://localhost:8983/solr --collection episodes | \
./solr2trec.py > steal/results_complex_trec.txt

cat steal/qrels.txt | ./qrels2trec.py > steal/qrels_trec.txt

trec_eval steal/qrels_trec.txt steal/results_complex_trec.txt

cat steal/results_complex_trec.txt | ./plot_pr.py --qrels steal/qrels_trec.txt --output steal/prec_rec_sys2.png
