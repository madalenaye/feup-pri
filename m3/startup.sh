#!/bin/bash

# create semantic episodes file
# cat data/docs/new_episodes.json | python3 get_embeddings.py
#Execute above command first to create the semantic episodes file
# Startup with Docker
docker run -p 8983:8983 --name pokemon_the_series -v ${PWD}/data:/data -d solr:9 solr-precreate episodes

# Wait for Solr to start
echo "Waiting for Solr to start..."
until $(curl --output /dev/null --silent --head --fail http://localhost:8983/solr/episodes/admin/ping); do
    printf '.'
    sleep 2
done

echo "Solr is up and running."

docker cp data/synonyms.txt pokemon_the_series:/var/solr/data/episodes/conf/synonyms.txt
docker cp data/pokemon_synonyms.txt pokemon_the_series:/var/solr/data/episodes/conf/pokemon_synonyms.txt

# Post the schema
curl -X POST -H 'Content-type:application/json' --data-binary @./data/semantic_schema.json http://localhost:8983/solr/episodes/schema

# Wait for a moment to ensure the schema is applied
sleep 2

# Post the documents
docker exec -it pokemon_the_series bin/solr post -f -c episodes /data/docs/chunked_episodes_2.json

docker restart pokemon_the_series
echo "Schema and documents have been posted."