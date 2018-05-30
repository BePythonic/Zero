# -*- coding: utf-8 -*-
users = [
        {"id": 0, "name": "Hero" },
        {"id": 1, "name": "Dunn" },
        {"id": 2, "name": "Sue" },
        {"id": 3, "name": "Chi" },
        {"id": 4, "name": "Thor" },
        {"id": 5, "name": "Clive" },
        {"id": 6, "name": "Hicks" },
        {"id": 7, "name": "Devin" },
        {"id": 8, "name": "Kate" },
        {"id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (6, 2), (1, 6), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 7), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []
    
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user) 
                        for user in users)

for user in users:
    print(number_of_friends(user), end=' ')

num_users = len(users)
avg_connections = total_connections / num_users

print(avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user))
                    for user in users]

# traduzido para python 3
print(sorted(num_friends_by_id,
       key=lambda x: x[1],
       reverse=True))



















