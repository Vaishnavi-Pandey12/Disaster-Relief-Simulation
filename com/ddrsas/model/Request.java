package com.ddrsas.model;

public class Request implements Comparable<Request> {
    private String location;
    private int foodNeeded;
    private int waterNeeded;
    private int medicineNeeded;
    private int urgency; // Higher value = more urgent

    public Request(String location, int food, int water, int medicine, int urgency) {
        this.location = location;
        this.foodNeeded = food;
        this.waterNeeded = water;
        this.medicineNeeded = medicine;
        this.urgency = urgency;
    }

    public String getLocation() {
        return location;
    }

    public int getFoodNeeded() {
        return foodNeeded;
    }

    public int getWaterNeeded() {
        return waterNeeded;
    }

    public int getMedicineNeeded() {
        return medicineNeeded;
    }

    public int getUrgency() {
        return urgency;
    }

    @Override
    public String toString() {
        return "Request{" +
                "location='" + location + '\'' +
                ", food=" + foodNeeded +
                ", water=" + waterNeeded +
                ", medicine=" + medicineNeeded +
                ", urgency=" + urgency +
                '}';
    }

    // ✅ Used by PriorityQueue (higher urgency first)
    @Override
    public int compareTo(Request other) {
        return Integer.compare(other.urgency, this.urgency);
    }
}
