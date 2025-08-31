package com.ddrsas.util;

import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;

public class EventLogger {
    private static final String LOG_FILE = "events.log";

   public static synchronized void log(String message) {
    String timestamped = "[" + LocalDateTime.now() + "] " + message;

    // Console colors (only affect live output, not log file)
    if (message.contains("✅")) {
        System.out.println("\u001B[32m" + timestamped + "\u001B[0m"); // Green
    } else if (message.contains("❌")) {
        System.out.println("\u001B[31m" + timestamped + "\u001B[0m"); // Red
    } else if (message.contains("New Request")) {
        System.out.println("\u001B[33m" + timestamped + "\u001B[0m"); // Yellow
    } else {
        System.out.println("\u001B[34m" + timestamped + "\u001B[0m"); // Blue
    }

    // File log (plain text, no colors)
    try (FileWriter fw = new FileWriter(LOG_FILE, true)) {
        fw.write(timestamped + "\n");
    } catch (IOException e) {
        System.err.println("Logging failed: " + e.getMessage());
    }
}

}
