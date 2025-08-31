package com.ddrsas.util;

import com.ddrsas.model.ReliefCenter;
import com.ddrsas.model.Request;
import java.util.List;

public class ResourceAllocator {

    // ✅ Try to allocate request to nearest possible relief center
    public static ReliefCenter allocate(Request req, List<ReliefCenter> centers) {
        ReliefCenter chosen = null;

        // simple: just pick the first that can fulfill
        for (ReliefCenter center : centers) {
            if (center.canFulfill(req)) {
                chosen = center;
                break;
            }
        }

        if (chosen != null) {
            chosen.allocate(req);
            System.out.println("✅ Request from " + req.getLocation() + " fulfilled by " + chosen.getName());
        } else {
            System.out.println("❌ Request from " + req.getLocation() + " could not be fulfilled (not enough stock).");
        }

        return chosen;
    }
}
