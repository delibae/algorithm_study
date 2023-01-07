def shortest_path(graph, n1, n2):
    
    p_index = 0
    p_l = [[n1]]
    
    prev_n = {n1}
    if n1 == n2:
        return p_l[0]
        
    while p_index < len(p_l):
        c_p = p_l[p_index]
        l_n = c_p[-1]
        n_ns = graph[l_n]

        if n2 in n_ns:
            c_p.append(n2)
            return c_p

        for n_n in n_ns:
            if not n_n in p_ns:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

graph = {}
graph[1] = {2, 5}
graph[2] = {1, 3, 5}
graph[3] = {2, 4}
graph[4] = {3, 5, 6}
graph[5] = {1, 2, 4}
graph[6] = {4}

re = shortest_path(graph, 1, 6)
print(re)