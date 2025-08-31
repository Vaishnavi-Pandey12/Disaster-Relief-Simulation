package com.ddrsas.util;

import com.ddrsas.model.Request;
import java.util.Comparator;

public class RequestComparator implements Comparator<Request> {
    @Override
    public int compare(Request r1, Request r2) {
        return Integer.compare(r2.getUrgency(), r1.getUrgency()); // higher urgency first
    }
}
