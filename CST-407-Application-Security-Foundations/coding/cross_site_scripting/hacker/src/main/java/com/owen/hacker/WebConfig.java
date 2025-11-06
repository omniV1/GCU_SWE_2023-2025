package com.owen.hacker;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

  @Override
  public void addCorsMappings(CorsRegistry registry) {
    registry.addMapping("/**")
        .allowedOriginPatterns("*") // allow all clients from anywhere to connect
        .allowedMethods("GET") // only allow GET requests
        .allowedHeaders("*") // allow all headers
        .allowCredentials(true);
  }
}
