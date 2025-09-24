package admin;

import java.io.*;
import java.net.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class AdminServer {
    private ServerSocket serverSocket;
    private ExecutorService executorService;
    private AdministrationService administrationService;

    public AdminServer(int port, AdministrationService administrationService) {
        this.administrationService = administrationService;

        try {
            serverSocket = new ServerSocket(port);
            executorService = Executors.newCachedThreadPool();
            System.out.println("AdminServer is listening on port " + port);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void start() {
        while (true) {
            try {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected: " + clientSocket.getInetAddress().getHostAddress());

                // Create a new client handler thread
                ClientHandler clientHandler = new ClientHandler(clientSocket);
                executorService.submit(clientHandler);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private class ClientHandler implements Runnable {
        private Socket clientSocket;

        public ClientHandler(Socket clientSocket) {
            this.clientSocket = clientSocket;
        }

        @Override
        public void run() {
            try (
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)
            ) {
                String message;
                while ((message = in.readLine()) != null) {
                    System.out.println("Received from client: " + message);

                    // Process the received message using the AdministrationService
                    String response = administrationService.processClientCommand(message);

                    // Send a response back to the client
                    out.println(response);
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    clientSocket.close();
                    System.out.println("Client disconnected: " + clientSocket.getInetAddress().getHostAddress());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
