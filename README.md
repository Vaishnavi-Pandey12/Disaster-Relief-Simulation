# 🌍 Dynamic Disaster Relief Simulation & Allocation System (DDR-SAS)

![GitHub stars](https://img.shields.io/github/stars/Vaishnavi-Pandey12/Disaster-Relief-Simulation?style=social)
![GitHub forks](https://img.shields.io/github/forks/Vaishnavi-Pandey12/Disaster-Relief-Simulation?style=social)
![License](https://img.shields.io/github/license/Vaishnavi-Pandey12/Disaster-Relief-Simulation)
![Issues](https://img.shields.io/github/issues/Vaishnavi-Pandey12/Disaster-Relief-Simulation)

---

## 📖 Overview
**DDR-SAS** is a **Java console-based simulation project** that models disaster relief allocation.  
It demonstrates **DSA concepts** in a practical scenario:

- **Priority Queues** → Handle urgent requests first  
- **Graphs + Dijkstra’s Algorithm** → Optimize routes to relief centers  
- **HashMaps** → Manage relief stock efficiently  
- **Threads (optional)** → Simulate real-time request generation  

---

## ⚡ Features
✔️ Add relief requests with urgency levels  
✔️ Allocate resources (food, water, medicine) from nearest centers  
✔️ Event logging of allocations  
✔️ User-friendly console menu  
✔️ Extendable for **road closures & multiple allocation strategies**  

---

## 🏗️ Tech Stack
- **Language:** Java (JDK 17+ recommended)  
- **Concepts Used:** Priority Queue, Graphs, Dijkstra, HashMap, Comparator  
- **Type:** Console Application  

---

## 📂 Project Structure
```

com/
└── ddrsas/
├── app/ # Main application (DisasterReliefApp.java)
├── model/ # Data models (Request, ReliefCenter, Edge)
├── util/ # Utility classes (Dijkstra, Allocator, Logger)
└── data/ # Graph implementation

```


---

## 🚀 How to Run
```bash
# compile
javac com\ddrsas\app\*.java com\ddrsas\model\*.java com\ddrsas\util\*.java
# or (Linux/Mac)
javac com/ddrsas/**/*.java

# run
java com.ddrsas.app.DisasterReliefApp
```
--
##Demo

<img width="710" height="205" alt="Screenshot 2025-08-31 201036" src="https://github.com/user-attachments/assets/b3f44445-1f32-47ce-bedf-788644583fd0" />
<img width="884" height="935" alt="Screenshot 2025-08-31 201020" src="https://github.com/user-attachments/assets/698e933e-09ac-42bd-a407-f08d6d083bf1" />
<img width="1107" height="914" alt="Screenshot 2025-08-31 200638" src="https://github.com/user-attachments/assets/94fd1b2a-6ab4-481d-89be-e72f379aa074" />
