package utils; // or whichever package you want to put it in

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class FileIO implements FileIOInterface{

    /**
     * Reads content from a file and returns it as a String.
     *
     * @param filePath The path to the file to read from.
     * @return The content of the file as a String.
     * @throws IOException If an I/O error occurs reading from the file.
     */
	
	@Override
	public String readFromFile(String filePath) throws IOException {
	    Path path = Paths.get(filePath);
	    
	    // Confirm the path before attempting to read
	    System.out.println("Attempting to read from path: " + path.toAbsolutePath());
	    
	    // Check if the file exists and is not a directory
	    if (Files.exists(path) && !Files.isDirectory(path)) {
	        return new String(Files.readAllBytes(path));
	    } else {
	        throw new IOException("File does not exist or is a directory: " + path);
	    }
	}


    @Override
    public void writeToFile(String filePath, String content) throws IOException {
        Path path = Paths.get(filePath);
        Files.write(path, content.getBytes());
    }
}
