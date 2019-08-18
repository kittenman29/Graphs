from util import Queue

# create a graph

# do depth first traversal
# if the input has no parents, return -1
# if it's the longest traversal, then print the node at which that traversal ends
# if there is a tie for longest traversal, then print the one with the lowest numeric ID


def earliest_ancestor(ancestors, starting_node):
    graph = {}

    for i in ancestors:
        #prints a bunch of tuples
        # print(i)
        if i[1] not in graph:
            # this is setting the second element of each tuple into a set
            graph[i[1]] = set()
        # sets the first element of the tuple as the value of each key in the graph
        graph[i[1]].add(i[0])

    print(graph)

    # THIS IS THE OPPOSITE OF WHAT'S ABOVE AND THE NORMAL WAY TO PUT SHIT IN A GRAPH
    # for i in ancestors:
    #     #prints a bunch of tuples
    #     print(i)
    #     if i[1] not in graph:
    #         graph[i[1]] = set()
    #     graph[i[1]].add(i[0])

    # print(graph)
    visited = {}
   
    q = Queue()
    q.enqueue([starting_node])

    longest_path = 1
    #base case for if we don't have any children
    ancestor = -1
    
    while q.size() > 0:
        path = q.dequeue()
        newChildID = path[-1]
        if len(path) > longest_path:
            #set the length of the path
            longest_path = len(path)
            ancestor = newChildID
        if len(path) == longest_path:
            if newChildID < ancestor:
                ancestor = newChildID
        if newChildID not in visited:
            visited[newChildID] = path
            # print("path", path)
            # print("newChildID", newChildID)
            # print("graphNewChild", graph[newChildID])
            if newChildID in graph:
                for childID in graph[newChildID]:

                    if childID not in visited:

                        new_path = list(path)
                        new_path.append(childID)
                        q.enqueue(new_path)


    return ancestor

print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 8))