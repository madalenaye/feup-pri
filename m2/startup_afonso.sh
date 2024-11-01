#A PARTE DE INICIAR O SOLR NESTE FICHEIRO É SÓ PARA O MEU PORTÁTIL SEM DOCKER

cd ~/solr-9.7.0/bin

./solr stop --all
./solr start &

sleep 5

./solr delete -c pokemon
./solr create -c pokemon

cd ~/feup-pri/m2

curl -X POST -H 'Content-type:application/json' --data-binary @./schema.json http://localhost:8983/solr/pokemon/schema

curl -X POST -H 'Content-type:application/json' \
    --data-binary @new_episodes.json \
    http://localhost:8983/solr/pokemon/update?commit=true
