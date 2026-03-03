FROM eclipse-temurin:17-jdk-alpine AS build
WORKDIR /app
COPY CST-323-Cloud-Computing/code/topic-2/cloud-app .
RUN chmod +x ./mvnw && ./mvnw package -DskipTests

FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
