import sys

users = {
    232: "Alice",
    550: "Bob",
    190: "Jack"
}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    user_id = int(line)
    name = users.get(user_id, "to all")
    print(f"Hi, {name}!")
