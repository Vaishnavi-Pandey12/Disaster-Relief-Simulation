package com.ddrsas.util;

import com.ddrsas.model.Request;
import java.util.PriorityQueue;
import java.util.Random;

public class RequestGenerator extends Thread {
    private PriorityQueue<Request> requestQueue;
    private String[] locations;
    private Random rand = new Random();
    private boolean running = true;

    public RequestGenerator(PriorityQueue<Request> requestQueue, String[] locations) {
        this.requestQueue = requestQueue;
        this.locations = locations;
    }

    @Override
    public void run() {
        while (running) {
            try {
                Thread.sleep(rand.nextInt(4000) + 2000); // 2–6 seconds

                String location = locations[rand.nextInt(locations.length)];
                int urgency = rand.nextInt(10) + 1;
                int food = rand.nextInt(50) + 10;
                int water = rand.nextInt(50) + 10;
                int medicine = rand.nextInt(30) + 5;

                Request req = new Request(location, urgency, food, water, medicine);

                synchronized (requestQueue) {
                    requestQueue.add(req);
                    EventLogger.log("[New Request Generated] " + req);
                }

            } catch (InterruptedException e) {
                running = false;
            }
        }
    }

    public void stopGenerator() {
        running = false;
    }
}
