#!/bin/bash
# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <complex|simple>"
    exit 1
fi

case "$1" in
   "complex") SCHEMA="schema2.json"
   ;;
   "simple") SCHEMA="schema.json"
   ;;
   *) echo "No valid schema type provided."
   exit -1
   ;;
esac

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
curl -X POST -H 'Content-type:application/json' --data-binary @./data/$SCHEMA http://localhost:8983/solr/episodes/schema

# Wait for a moment to ensure the schema is applied
sleep 2

# Post the documents
docker exec -it pokemon_the_series bin/solr post -f -c episodes /data/docs/new_episodes.json

docker restart pokemon_the_series
echo "Schema and documents have been posted."