package com.ddrsas.model;

import java.util.HashMap;
import java.util.Map;

public class ReliefCenter {
    private String name;
    private Map<String, Integer> stock;

    public ReliefCenter(String name, int food, int water, int medicine) {
        this.name = name;
        this.stock = new HashMap<>();
        this.stock.put("food", food);
        this.stock.put("water", water);
        this.stock.put("medicine", medicine);
    }

    public String getName() {
        return name;
    }

    public Map<String, Integer> getStock() {
        return stock;
    }

    // ✅ Check if this center can fulfill request
    public boolean canFulfill(Request req) {
        return stock.get("food") >= req.getFoodNeeded()
            && stock.get("water") >= req.getWaterNeeded()
            && stock.get("medicine") >= req.getMedicineNeeded();
    }

    // ✅ Deduct stock if request is fulfilled
    public void allocate(Request req) {
        stock.put("food", stock.get("food") - req.getFoodNeeded());
        stock.put("water", stock.get("water") - req.getWaterNeeded());
        stock.put("medicine", stock.get("medicine") - req.getMedicineNeeded());
    }

    @Override
    public String toString() {
        return "ReliefCenter{" +
                name +
                ", stock=" + stock +
                '}';
    }
}
