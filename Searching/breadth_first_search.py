import inspect


def search(graph, start_vertex):
    # Take a list for storing already visited vertexes
    if start_vertex not in graph or graph[start_vertex] is None or graph[start_vertex] == []:
        return None

    # create a list to store all the vertexes for BFS and a set to store the visited vertices
    visited, queue = set(), [start_vertex]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def get_code():
    return inspect.getsource(search)
