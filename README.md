
# 🌍 Dynamic Disaster Relief Simulation & Allocation System (DDR-SAS)

## 📖 Overview
DDR-SAS is a **Java console-based simulation project** that models disaster relief allocation.  
It demonstrates **DSA concepts** by using:
- **Priority Queues** → For handling urgent requests first.
- **Graphs + Dijkstra’s Algorithm** → For route optimization to relief centers.
- **HashMaps** → For managing relief stock.
- **Threads (optional)** → For simulating real-time request generation.

---

## ⚡ Features
✔️ Add relief requests with urgency levels.  
✔️ Allocate resources (food, water, medicine) from nearest centers.  
✔️ Event logging of allocations.  
✔️ User-friendly console menu.  
✔️ Extendable for **road closures & multiple strategies**.

---

## 🏗️ Tech Stack
- **Language:** Java (JDK 17+ recommended)
- **Concepts Used:** Priority Queue, Graphs, Dijkstra, HashMap, Comparator
- **Type:** Console Application

---

## 🚀 How to Run
```bash
# compile
javac com/ddrsas/**/*.java

# run
java com.ddrsas.app.DisasterReliefApp
