#A PARTE DE INICIAR O SOLR NESTE FICHEIRO É SÓ PARA O MEU PORTÁTIL SEM DOCKER

cd ~/solr-9.7.0/bin

./solr stop --all
./solr start &

sleep 10

./solr delete -c episodes
./solr create -c episodes

cd ~/feup-pri/m2

curl -X POST -H 'Content-type:application/json' --data-binary @data/schema2.json http://localhost:8983/solr/episodes/schema

curl -X POST -H 'Content-type:application/json' \
    --data-binary @data/docs/new_episodes.json \
    http://localhost:8983/solr/episodes/update?commit=true
