records = [
    (1, "alice", ["login", "view", "logout"]),
    (2, "bob", ["login", "view"]),
    (3, "alice", ["login", "purchase"]),
    (4, "david", ["login", "view", "purchase", "logout"]),
]
uniqueName = set()
activityCount = {
    "login":0,
    "view":0,
    "logout":0,
    "purchase":0
}
userActivityMap = {
    "alice": [],
    "bob": [],
    "david": []
}
mostActive = "bob"
for r in records:
    uniqueName.add(r[1])
    for s in r[2]:
        if s not in userActivityMap[r[1]]:
            userActivityMap[r[1]].append(s)
    for a in r[2]:
        activityCount[a] += 1

for key, value in userActivityMap.items():
    if(len(userActivityMap[key]) > len(userActivityMap[mostActive])):
        mostActive = key

print(uniqueName)
print(activityCount)
print(userActivityMap)
print(mostActive)
