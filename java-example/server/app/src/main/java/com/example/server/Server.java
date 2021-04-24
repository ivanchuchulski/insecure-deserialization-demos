package com.example.server;

import com.example.lib.Virus;

import java.io.IOException;
import java.io.InvalidClassException;
import java.io.ObjectInput;
import java.io.ObjectInputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Arrays;

public class Server {
    private final ServerSocket serverSocket;
    private boolean runServer;

    public Server(int port) {
        try {
            runServer = true;
            serverSocket = new ServerSocket(port);
        } catch (IOException ioException) {
            throw new RuntimeException("cant start server", ioException);
        }
    }

    public static void main(String[] args) {
        final int PORT = 7777;
        new Server(PORT).startServer();
    }

    public void stop() {
        runServer = false;
    }

    private void startServer() {
        System.out.println("server up...");
        System.out.println(System.getProperty("java.runtime.version"));
        while (runServer) {
            try (Socket sock = serverSocket.accept();
//                ObjectInputStream in = new ObjectInputStream(sock.getInputStream());
                 SafeVirusInputStream safeVirusInputStream = new SafeVirusInputStream(sock.getInputStream())
            ) {
//                 Virus virus = (Virus) in.readObject(); // deserialization
                Virus virus = (Virus) safeVirusInputStream.readObject();

                System.out.println("received new virus : ");
                System.out.println(virus.getClass().getName());
                System.out.println(Virus.class.getName());
                virus.print();
            } catch (InvalidClassException invalidClassException) {
                System.out.println("invalid class except " + invalidClassException.getMessage());
            } catch (IOException ioException) {
                System.out.println("ioexception" + ioException);
            } catch (ClassNotFoundException classNotFoundException) {
                System.out.println("error : sent an unknown object");
            }
        }
        try {
            serverSocket.close();
        } catch (IOException ioException) {
            throw new RuntimeException("error closing server", ioException);
        }
    }
}
