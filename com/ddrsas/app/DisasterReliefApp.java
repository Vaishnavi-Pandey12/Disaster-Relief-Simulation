package com.ddrsas.app;

import com.ddrsas.model.ReliefCenter;
import com.ddrsas.model.Request;
import com.ddrsas.util.ResourceAllocator;
import java.util.*;

public class DisasterReliefApp {
    private static Scanner sc = new Scanner(System.in);
    private static List<ReliefCenter> centers = new ArrayList<>();
    private static Queue<Request> requests = new PriorityQueue<>(Comparator.comparingInt(Request::getUrgency).reversed());

    public static void main(String[] args) {
        // Create some sample relief centers
        centers.add(new ReliefCenter("Center A", 100, 100, 50));
        centers.add(new ReliefCenter("Center B", 80, 60, 40));
        centers.add(new ReliefCenter("Center C", 120, 90, 70));

        int choice;
        do {
            System.out.println("\n===== Disaster Relief Allocation System =====");
            System.out.println("1. Add new request");
            System.out.println("2. View relief centers");
            System.out.println("3. View pending requests");
            System.out.println("4. Allocate resources");
            System.out.println("5. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1 -> addRequest();
                case 2 -> viewCenters();
                case 3 -> viewRequests();
                case 4 -> allocateResources();
                case 5 -> System.out.println("Exiting... Stay safe!");
                default -> System.out.println("Invalid choice. Try again!");
            }
        } while (choice != 5);
    }

    // ✅ Add new request
    private static void addRequest() {
        sc.nextLine(); // consume newline
        System.out.print("Enter location: ");
        String location = sc.nextLine();

        System.out.print("Enter urgency (1-5, higher = urgent): ");
        int urgency = sc.nextInt();

        System.out.print("Food needed: ");
        int food = sc.nextInt();
        System.out.print("Water needed: ");
        int water = sc.nextInt();
        System.out.print("Medicine needed: ");
        int medicine = sc.nextInt();

        Request req = new Request(location, urgency, food, water, medicine);
        requests.add(req);
        System.out.println("✅ Request added successfully!");
    }

    // ✅ View centers
    private static void viewCenters() {
        System.out.println("\n--- Relief Centers ---");
        for (ReliefCenter center : centers) {
            System.out.println(center);
        }
    }

    // ✅ View pending requests
    private static void viewRequests() {
        System.out.println("\n--- Pending Requests ---");
        if (requests.isEmpty()) {
            System.out.println("No pending requests.");
        } else {
            for (Request req : requests) {
                System.out.println(req);
            }
        }
    }

    // ✅ Allocate resources
    private static void allocateResources() {
        if (requests.isEmpty()) {
            System.out.println("No requests to allocate!");
            return;
        }

        Request req = requests.poll(); // take highest urgency
        ResourceAllocator.allocate(req, centers);
    }
}
