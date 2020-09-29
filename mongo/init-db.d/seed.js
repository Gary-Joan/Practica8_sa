db.test1.drop();
db.test1.insert_many([
    {"type": "cat", "weight": 25, "color": "orange"},
    {"type": "dog", "weight": 35, "color": "black"},
    {"type": "cat", "weight": 10, "color": "black"}
])