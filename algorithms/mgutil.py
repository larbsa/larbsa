import heapq
def extractPathCompare (end, nodes, reverse=True):
    currentlyAt = end
    path = [end]
    # To avoid missing better solutions for the parent, 
    # since the parent may have been an alternative and missed 
    # the chanced to check whether it was good enough or not
    
    while currentlyAt in nodes and nodes[currentlyAt][0] != None:
        
        # Line added for update
        parent = currentlyAt
        # Line above added for update

        child = nodes[currentlyAt][0]
        
        left = (parent[0]+1,  parent[1]) 
        right = (parent[0]-1,  parent[1]) 
        top = (parent[0],  parent[1]+1) 
        bottom = (parent[0],  parent[1]-1) 
        if left in nodes:
            if left != path[len(path)-1]:
                if child != left:
                    if nodes[left][1] < nodes[child][1] and left not in path:
                        path.append(left)
                        currentlyAt = left
                        continue
        if right in nodes:
            if right != path[len(path)-1]:
                if child != right:
                    if nodes[right][1] < nodes[child][1] and right not in path:
                        path.append(right)
                        currentlyAt = right
                        continue
        if top in nodes:
            if top != path[len(path)-1]:
                if child != top:
                    if nodes[top][1] < nodes[child][1] and top not in path:
                        path.append(top)
                        currentlyAt = top
                        continue     
        if bottom in nodes:
            if bottom != path[len(path)-1]:
                if child != bottom:
                    if nodes[bottom][1] < nodes[child][1] and bottom not in path:
                        path.append(bottom)
                        currentlyAt = bottom
                        continue                                            
                        
        path.append(child)
        currentlyAt = child
        
    return path[::-1] if reverse else path


def extractPathCompareAdvanced (end, nodes, reverse=True):
    currentlyAt = end
    path = [end]
    # To avoid missing better solutions for the parent, 
    # since the parent may have been an alternative and missed 
    # the chanced to check whether it was good enough or not
    
    while currentlyAt in nodes and nodes[currentlyAt][0] != None:
        
        smallestNode = nodes[currentlyAt][0]
        smallestScore = nodes[currentlyAt][1]

        left = (currentlyAt[0]-1,  currentlyAt[1]) 
        right = (currentlyAt[0]+1,  currentlyAt[1]) 
        top = (currentlyAt[0],  currentlyAt[1]+1) 
        bottom = (currentlyAt[0],  currentlyAt[1]-1) 

        if left in nodes and left != path[len(path)-1] and nodes[left][1] < smallestScore:
            currentlyAt = left
            path.append(currentlyAt)
            continue
        if right in nodes and right != path[len(path)-1] and nodes[right][1] < smallestScore:
            currentlyAt = right
            path.append(currentlyAt)
            continue
        if top in nodes and top != path[len(path)-1] and nodes[top][1] < smallestScore:
            currentlyAt = top
            path.append(currentlyAt)
            continue
        if bottom in nodes and bottom != path[len(path)-1] and nodes[bottom][1] < smallestScore:
            currentlyAt = bottom
            path.append(currentlyAt)
            continue

        
    return path[::-1] if reverse else path


def extractPath (end, nodes, reverse=True):
    currentlyAt = end
    path = [end]
    # To avoid missing better solutions for the parent, 
    # since the parent may have been an alternative and missed 
    # the chanced to check whether it was good enough or not
    
    while currentlyAt in nodes and nodes[currentlyAt][0] != None:
        
        # Line added for update
        parent = currentlyAt
        # Line above added for update

        child = nodes[currentlyAt][0]
        
        left = (parent[0]+1,  parent[1]) 
        right = (parent[0]-1,  parent[1]) 
        top = (parent[0],  parent[1]+1) 
        bottom = (parent[0],  parent[1]-1) 
        if left in nodes:
            if left != path[len(path)-1]:
                if child != left:
                    if nodes[left][1] < nodes[child][1] and left not in path:
                        path.append(left)
                        currentlyAt = left
                        continue
        if right in nodes:
            if right != path[len(path)-1]:
                if child != right:
                    if nodes[right][1] < nodes[child][1] and right not in path:
                        path.append(right)
                        currentlyAt = right
                        continue
        if top in nodes:
            if top != path[len(path)-1]:
                if child != top:
                    if nodes[top][1] < nodes[child][1] and top not in path:
                        path.append(top)
                        currentlyAt = top
                        continue     
        if bottom in nodes:
            if bottom != path[len(path)-1]:
                if child != bottom:
                    if nodes[bottom][1] < nodes[child][1] and bottom not in path:
                        path.append(bottom)
                        currentlyAt = bottom
                        continue                                            
                        
        path.append(child)
        currentlyAt = child

        # Lines below added for update
        if nodes[currentlyAt] == None:
            continue
        
        # look the left, right, top and bottom
        # disregard parent, since it will be one of those nodes
        # we will compare default node with another node that might be of interest if it exists
        
        left = (child[0]+1,  child[1]) 
        right = (child[0]-1,  child[1]) 
        top = (child[0],  child[1]+1) 
        bottom = (child[0],  child[1]-1) 

        if left in nodes:
            if left != parent:
                if nodes[child][0] != left:
                    if nodes[left][1] < nodes[child][1] and left not in path:
                        path.append(left)
                        currentlyAt = left
                        continue

        if right in nodes:
            if right != parent:
                if nodes[child][0] != right:
                    if nodes[right][1] < nodes[child][1] and right not in path:
                        path.append(right)
                        currentlyAt = right
                        checkParentOptions = True
                        continue

        if top in nodes:
            if top != parent:
                if nodes[child][0] != top:
                    if nodes[top][1] < nodes[child][1] and top not in path:
                        path.append(top)
                        currentlyAt = top
                        continue     

        if bottom in nodes:
            if bottom != parent:
                if nodes[child][0] != bottom:
                    if nodes[bottom][1] < nodes[child][1] and bottom not in path:
                        path.append(bottom)
                        currentlyAt = bottom
                        continue                                

        # Lines above added for update



    return path[::-1] if reverse else path
