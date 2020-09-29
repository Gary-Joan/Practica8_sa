db.test.drop();
db.test.insertMany([
    {"type": "cat", "weight": 25, "color": "orange"},
    {"type": "dog", "weight": 35, "color": "black"},
    {"type": "cat", "weight": 10, "color": "black"}
])