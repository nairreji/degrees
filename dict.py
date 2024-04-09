import csv
import sys

directory = "small"
people = {}
with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            people[row["id"]]["movies"].update({"Reji","Jyoti","Ammu","Monu"})
for key in people:
    print(key,"-->",people[key])