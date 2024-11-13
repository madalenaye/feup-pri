#!/bin/bash

# Startup with Docker
docker run -p 8983:8983 --name pokemon_the_series -v ${PWD}/data:/data -d solr:9 solr-precreate episodes

# Wait for Solr to start
echo "Waiting for Solr to start..."
until $(curl --output /dev/null --silent --head --fail http://localhost:8983/solr/episodes/admin/ping); do
    printf '.'
    sleep 2
done

echo "Solr is up and running."

# Post the schema
curl -X POST -H 'Content-type:application/json' --data-binary @./data/schema.json http://localhost:8983/solr/episodes/schema

# Wait for a moment to ensure the schema is applied
sleep 2

# Post the documents
docker exec -it pokemon_the_series bin/solr post -f -c episodes /data/docs/new_episodes.json

echo "Schema and documents have been posted."