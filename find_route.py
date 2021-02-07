################################################
# Name: FAHAD UR RAHAMAN
# Student ID: 1001753107
# Course: CSE-5360-003-ARTIFICIAL INTELLIGENCE I
################################################

from collections import defaultdict
import sys

# This method generates the list of places with heauristic values from heuristic input txt file provided
def fact_finding(data):
    inputterminated = "end of input"
    for h in data:
        if h.lower().find(inputterminated) != -1:
            break
        else:
            record = h.split(" ")
            facts[places.index(record[0])] = int(record[1])
    return

# This method validates the previously visted nodes
def validateVisitedNode(presentnode, visited):
    for node in visited:
        if presentnode == node["node"]:
            return True
    return False

# This method identifies optimal routes from start to target
def findingOptimalRoute(out, visited):

    route = []

    def backtrack(dest, s):
        if dest is None:
            return
        else:
            for visited_places in s:
                if visited_places["node"] == dest:
                    route.append(dest)
                    backtrack(visited_places["previous"], s)

    if out:
        print ("distance: " + str(out["count"]) + " km")
        print ("route:")
        backtrack(out["present"], visited)
        route.reverse()
        for i in range(0, len(route) - 1):
            print ("{} to {}, {} km".format(places [route[i]], places[route[i+1]],str(map[route[i]][route[i+1]])))
    else:
        print ("distance: infinity")
        print ("route:")
        print ("none")
    return

# This method generates a graph based on the input file provided
def Map_Maker(data):
    inputterminated = "end of input"
    for route in data:
        if route.lower().find(inputterminated) != -1:
            break
        else:
            src, des, *rest = route.strip().split(" ")
            True if src in places else places.append(src)
            True if des in places else places.append(des)
    places.sort()

    for i in range(len(places)):
        map.append([])
        for j in range(len(places)):
            map[i].append(-1)
        map[i][i] = 0

    for route in data:
        if route.lower().find(inputterminated) != -1:
            break
        else:
            src, des, c = route.strip().split(" ")
            map[places.index(src)][places.index(des)] = float(c)
            map[places.index(des)][places.index(src)] = float(c)
    return

# This methods performs sorting and storage during search
def sorting_of_graphical_data_structure(graphical_data_structure, flag):
    if(len(graphical_data_structure) > 1):
        for node_i in range(0, len(graphical_data_structure) - 1):
            small = node_i
            for node_j in range(node_i+1, len(graphical_data_structure)):
                s = graphical_data_structure[small]["count"]
                n = graphical_data_structure[node_j]["count"]
                if flag:
                    s += graphical_data_structure[small]["heur_cost"]
                    n += graphical_data_structure[node_j]["heur_cost"]
                if(s > n):
                    small = node_j
            temp = graphical_data_structure[small]
            graphical_data_structure[small] = graphical_data_structure[node_i]
            graphical_data_structure[node_i] = temp
        return graphical_data_structure
    else:
        return graphical_data_structure

# This method performs A* Tree Search where f(n) = estimated cost of the cheapest solution through n = g(n) + h(n) [Informed Search Algorithm]

def Astarsearch():
    dest = places.index(destination)
    generatednodes = 1
    expandednodes = 0
    graphical_data_structure = []
    visited = []
    out = False
    graphical_data_structure.append({"present": places.index(source), "count": 0, "heur_cost": facts[places.index(source)], "previous": None})
    while(len(graphical_data_structure) > 0):
        expandednodes = expandednodes + 1
        if graphical_data_structure[0]["present"] == dest:
            visited.append({"node"  : graphical_data_structure[0]["present"], "previous": graphical_data_structure[0]["previous"]})
            out = graphical_data_structure[0]
            break
        elif validateVisitedNode(graphical_data_structure[0]["present"], visited):
            del graphical_data_structure[0]
            continue
        else:
            visited.append({"node"  : graphical_data_structure[0]["present"], "previous": graphical_data_structure[0]["previous"]})
            for i in range(len(map[graphical_data_structure[0]["present"]])):
                if map[graphical_data_structure[0]["present"]][i] > 0:
                    graphical_data_structure.append({"present": i, "count": graphical_data_structure[0]["count"]+map[graphical_data_structure[0]["present"]][i], "heur_cost": facts[i], "previous": graphical_data_structure[0]["present"]})
                    generatednodes = generatednodes + 1
            del graphical_data_structure[0]
            graphical_data_structure = sorting_of_graphical_data_structure(graphical_data_structure, True)
    print();
    print("The output for Informed Search is as shown below:")
    print();
    print("nodes expanded: " + str(expandednodes));
    print("nodes generated: " + str(generatednodes));
    findingOptimalRoute(out, visited)
    return

# This method performs the Uninformed Search Algorithm

def Uniform_Cost_Search():
    dest = places.index(destination)
    generatednodes = 1
    expandednodes = 0
    graphical_data_structure = []
    visited = []
    out = False
    graphical_data_structure.append({"present": places.index(source), "count"  : 0, "previous": None});
    while(len(graphical_data_structure) > 0):
        expandednodes = expandednodes + 1
        if graphical_data_structure[0]["present"] == dest:
            visited.append({"node"  : graphical_data_structure[0]["present"], "previous": graphical_data_structure[0]["previous"]})
            out = graphical_data_structure[0]
            break
        elif validateVisitedNode(graphical_data_structure[0]["present"], visited):
            del graphical_data_structure[0]
            continue
        else:
            visited.append({"node"  : graphical_data_structure[0]["present"], "previous": graphical_data_structure[0]["previous"]})
            for i in range(len(map[graphical_data_structure[0]["present"]])):
                if map[graphical_data_structure[0]["present"]][i] > 0:
                    graphical_data_structure.append({"present":i, "count" :graphical_data_structure[0]["count"]+map[graphical_data_structure[0]["present"]][i], "previous":graphical_data_structure[0]["present"]})
                    generatednodes = generatednodes + 1
            del graphical_data_structure[0]
            graphical_data_structure = sorting_of_graphical_data_structure(graphical_data_structure, False)
    print();
    print("The output for Uninformed Search is as shown below:")
    print();
    print("nodes expanded: " + str(expandednodes))
    print("nodes generated: " + str(generatednodes))
    findingOptimalRoute(out, visited)
    return

# This is the main program
if len(sys.argv) >= 4:

    places = []
    map = []

    Map_Maker(open(sys.argv[1], "r").read().split("\n"))
    source = sys.argv[2]
    destination = sys.argv[3]
    if len(sys.argv) != 5:
        Uniform_Cost_Search()
    elif len(sys.argv) == 5:
            facts = [0] * len(places)
            fact_finding_data = sys.argv[4]
            fact_finding(open(sys.argv[4], "r").read().split("\n"))
            Astarsearch()
    else:
        print ("Accurate search output was not found")

