package com.ddrsas.util;

import com.ddrsas.model.Edge;
import com.ddrsas.data.Graph;
import java.util.*;

public class Dijkstra {
    public static Map<String, Integer> shortestPath(Graph graph, String start) {
        Map<String, Integer> dist = new HashMap<>();
        PriorityQueue<Map.Entry<String, Integer>> pq =
                new PriorityQueue<>(Map.Entry.comparingByValue());

        for (String loc : graph.getLocations()) {
            dist.put(loc, Integer.MAX_VALUE);
        }
        dist.put(start, 0);

        pq.add(new AbstractMap.SimpleEntry<>(start, 0));

        while (!pq.isEmpty()) {
            String current = pq.poll().getKey();

            for (Edge edge : graph.getNeighbors(current)) {
                int newDist = dist.get(current) + edge.getDistance();
                if (newDist < dist.get(edge.getDestination())) {
                    dist.put(edge.getDestination(), newDist);
                    pq.add(new AbstractMap.SimpleEntry<>(edge.getDestination(), newDist));
                }
            }
        }
        return dist;
    }
}
