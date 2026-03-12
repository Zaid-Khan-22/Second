You are given a list of user activity records.
Each record is represented as a tuple:

(user_id: int, username: str, activities: List[str])

Your task

Process the data and return a dictionary with the following details:

Output Dictionary Requirements

"unique_users" → a set of all unique usernames

"activity_count" → a dictionary where keys are activities (string) and values are how many times they occurred across all users

"user_activity_map" → a dictionary mapping each username to a sorted list of their unique activities

"most_active_user" → the username (string) who performed the highest number of total activities

If there’s a tie, return the lexicographically smallest username
Input Example
records = [
    (1, "alice", ["login", "view", "logout"]),
    (2, "bob", ["login", "view"]),
    (3, "alice", ["login", "purchase"]),
    (4, "david", ["login", "view", "purchase", "logout"]),
]

Expected Output
{
    "unique_users": {"alice", "bob", "david"},
    "activity_count": {
        "login": 4,
        "view": 3,
        "logout": 2,
        "purchase": 2
    },
    "user_activity_map": {
        "alice": ["login", "logout", "purchase", "view"],
        "bob": ["login", "view"],
        "david": ["login", "logout", "purchase", "view"]
    },
    "most_active_user": "alice"
}