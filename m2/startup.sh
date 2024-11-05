#Startup with docker
docker run -p 8983:8983 --name pokemon_the_series -v ${PWD}:/data -d solr:9 solr-precreate episodes

curl -X POST -H 'Content-type:application/json' --data-binary @./data/schema.json http://localhost:8983/solr/episodes/schema

curl -X POST -H 'Content-type:application/json' \
    --data-binary @./data/docs/new_episodes.json \
    http://localhost:8983/solr/episodes/update?commit=true
