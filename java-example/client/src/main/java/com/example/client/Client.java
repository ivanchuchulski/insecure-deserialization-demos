package com.example.client;

import com.example.lib.Virus;

import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.time.LocalDate;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Client {
    private final static String HOST = "localhost";
    private final static int PORT = 7777;

    public static void main(String[] ars) throws InterruptedException {
        demo();
    }

    private static void demo() throws InterruptedException {
        Virus swineInfluenza = new Virus("influenza A virus subtype H1N1",
                "A/H1N1", LocalDate.parse("1918-04-01"));

        Virus mers = new Virus("Middle East respiratory syndrome ",
                "MERS", LocalDate.parse("2012-05-01"));

        Virus covid = new Virus("Severe acute respiratory syndrome coroNavirus 2",
                "SARS‑CoV‑2", LocalDate.parse("2019-12-30"));

        System.out.println("sending viruses to database server");
        List<Virus> virusList = List.of(swineInfluenza, mers, covid);
        for (Virus virus : virusList) {
            System.out.println("sending virus : " + virus);
            Thread.sleep(2_000);
            registerVirus(virus);
        }

        /* when sending this payload in the safe server variant, after the first part of the hashset is rejected the
        server closes the connection */
        Object dosPayload = buildDoSPayload();
        // registerVirus(dosPayload);

        System.out.println("data is send");
    }

    private static Object buildDoSPayload() {
        Set root = new HashSet();
        Set s1 = root;
        Set s2 = new HashSet();
        for (int i = 0; i < 100; i++) {
            Set t1 = new HashSet();
            Set t2 = new HashSet();
            t1.add("foo"); // make it not equal to t2
            s1.add(t1);
            s1.add(t2);
            s2.add(t1);
            s2.add(t2);
            s1 = t1;
            s2 = t2;
        }
        return root;
    }

    private static void registerVirus(Object p) {
        try (Socket socket = new Socket(HOST, PORT);
             ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream())) {
            out.writeObject(p);
            out.flush();
        } catch (IOException ioException) {
            throw new RuntimeException("error sending data", ioException);
        }
    }
}

