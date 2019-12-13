import collections


class Solution:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    # adds edge from src to destination
    def addEdge(self, source, destination):
        self.graph[source].append(destination)

    def findItinerary(self, tickets):
        for ticket in tickets:
            self.addEdge(ticket[0], ticket[1])
        result = ["JFK"]
        self.dfs(len(tickets), "JFK", result)
        return result

    # This function perform depth first search
    def dfs(self, numTickets, airport, result):
        # base condition
        if len(result) == numTickets + 1:
            return True
        # For all neighbour sorted lexographically keep doing dfs i.e explore left entirely and then right
        for nextAirport in sorted(self.graph[airport]):
            # add neighbour in result
            self.graph[airport].remove(nextAirport)
            result.append(nextAirport)
            # keep exploring next airport
            # if path reached return True else remove from result
            if self.dfs(numTickets, nextAirport, result):
                return True
            else:

                self.graph[airport].append(nextAirport)
                result.pop()
        return False

