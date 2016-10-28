import json
with open('dictionary.json') as dictionaryFile:
	file = json.load(dictionaryFile)

rawData = {}
visited = []
for word in file:
    length = len(word)
    if length in rawData:
        rawData[length].append(word)
    else:
        rawData[length] = []
        rawData[length].append(word)




word1 = input("Enter the first word:\n")
word2 = input("Enter the second word:\n")
dictionary = rawData[len(word1)]


def check(first,second):
    ok = False
    for c1, c2 in zip(first, second):
        if c1 != c2:
            if ok:
                return False
            else:
                ok = True

    return ok

wordMap = {}



def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
        	return path
        elif node not in visited:
        	visited.append(node)
        	neighbours = graph[node]
        	for adjacent in neighbours:
        		new_path = list(path)
        		new_path.append(adjacent)
        		queue.append(new_path)



count = 0
for i in dictionary:
    wordMap[i] = []
    for j in dictionary:
        if check(i,j):
            wordMap[i].append(j)
        print(count)
        count+=1


print(bfs(wordMap,word1,word2))