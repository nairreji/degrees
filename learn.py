import sys
import csv

oneactormanymovies=dict()
onemoviemanyactors=dict()
l=[]

with open(f"large/stars.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["person_id"] in oneactormanymovies:
            ps=oneactormanymovies[row["person_id"]]+","+row["movie_id"]
            oneactormanymovies[row["person_id"]]=ps
        else:
            oneactormanymovies[row["person_id"]]=row["movie_id"]
    
with open(f"large/stars.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["movie_id"] in onemoviemanyactors:
            ps=onemoviemanyactors[row["movie_id"]]+","+row["person_id"]
            onemoviemanyactors[row["movie_id"]]=ps
        else:
            onemoviemanyactors[row["movie_id"]]=row["person_id"]


from_actor = "102"
to_actor = "420"
tactor="a"+to_actor
frontier=["a"+from_actor]
DeletedFromFrontier=[]
x=0
trips=0
while (x==0): 
    # mov_act = frontier[len(frontier)-1]
    # frontier=frontier[0:len(frontier)-1]
    mov_act = frontier[0]
    frontier=frontier[1:len(frontier)]    
    DeletedFromFrontier+=[mov_act]   
    ftype=mov_act[0]
    mov_act=mov_act[1:]
    trips=trips+1
    if ftype=="a":
        movies=oneactormanymovies[mov_act]
        movies=movies.split(",")
        movies = ["m" + a for a in movies]
        frontier=frontier + movies
    else:
        actors=onemoviemanyactors[mov_act]
        actors=actors.split(",")
        actors = ["a" + a for a in actors]
        frontier=frontier + actors
    frontier = [i for i in frontier if i not in DeletedFromFrontier]
    print(frontier)
    if tactor in frontier:
        print(trips)
        print(frontier)
        x=1
        break
    