#A PARTE DE INICIAR O SOLR NESTE FICHEIRO É SÓ PARA O MEU PORTÁTIL SEM DOCKER

cd ~/solr-9.7.0/bin

./solr stop --all
./solr start &

sleep 10

./solr delete -c episodes
./solr create -c episodes


cd ~/feup-pri/m3
cp data/synonyms.txt /home/onso/solr-9.7.0/server/solr/episodes/conf/synonyms.txt
cp data/pokemon_synonyms.txt /home/onso/solr-9.7.0/server/solr/episodes/conf/pokemon_synonyms.txt

curl -X POST -H 'Content-type:application/json' --data-binary @data/semantic_schema.json http://localhost:8983/solr/episodes/schema

curl -X POST -H 'Content-type:application/json' \
    --data-binary @data/docs/chunked_episodes_2.json \
    http://localhost:8983/solr/episodes/update?commit=true
