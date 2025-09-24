package utils;

import java.io.IOException;

public interface FileIOInterface {
    String readFromFile(String filePath) throws IOException;
    void writeToFile(String filePath, String content) throws IOException;
}
