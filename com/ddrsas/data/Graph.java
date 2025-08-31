package com.ddrsas.data;

import com.ddrsas.model.Edge;
import java.util.*;

public class Graph {
    private Map<String, List<Edge>> adjList;

    public Graph() {
        adjList = new HashMap<>();
    }

    public void addLocation(String location) {
        adjList.putIfAbsent(location, new ArrayList<>());
    }

    public void addEdge(String from, String to, int distance) {
        adjList.get(from).add(new Edge(to, distance));
        adjList.get(to).add(new Edge(from, distance)); // undirected graph
    }

    public List<Edge> getNeighbors(String location) {
        return adjList.getOrDefault(location, new ArrayList<>());
    }

    public Set<String> getLocations() {
        return adjList.keySet();
    }
}
