FROM mongo:latest

COPY init.json /init.json
CMD mongoimport --host mongodb --db dbsa --collection listado --type json --file /init.json --jsonArray