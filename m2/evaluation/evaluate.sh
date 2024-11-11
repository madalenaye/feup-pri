./query_solr.py --query query_sys1.json --uri http://localhost:8983/solr --collection episodes | \
./solr2trec.py > results_sys1_trec.txt

cat qrels.txt | ./qrels2trec.py > qrels_trec.txt

trec_eval qrels_trec.txt results_sys1_trec.txt

cat results_sys1_trec.txt | ./plot_pr.py --qrels qrels_trec.txt --output prec_rec_sys1.png
