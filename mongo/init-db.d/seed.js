// Since Seeding in Mongo is done in alphabetical order... It's is important to keep
// file names alphabetically ordered, if multiple files are to be run.

db.test.drop();
db.test.insert_many([
    {"type": "cat", "weight": 25, "color": "orange"},
    {"type": "dog", "weight": 35, "color": "black"},
    {"type": "cat", "weight": 10, "color": "black"}
])