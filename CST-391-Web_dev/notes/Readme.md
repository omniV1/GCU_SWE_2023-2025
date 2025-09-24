# CST -391 javaScript Web Application Developement

### Topic 1 Activity 0 

### NodeJS

- Frees Javascript from the constraints of the browser. 
- JavaScript Engine from Chrome ===> the V8 Engine
  
  - the V8 Engine was developed to support Google Maps and Office Apps.
  - ah JIT compilation approach to optimizing running code. 
  
    - Similar: The Java JVM. 

- **Used for**:
- lightweight web servers / general purpose programming enviornments. 
- Analogous to the JVM or .NET CLR

  - Like Java, it can be turned into a web server with framework libraries.
- Front end developement build and deployment systems. 

    - NPM (node package manager)
    - simular to maven 
- Angular
- React


**NPM**   

- NPM manages dependencies 
  
    - these are the libraries your application needs. 
    - supports development and deployment 
    - application libraries: code your application needs to run, deployed to the site. 
- As NPM does its work, it modifies file named "package.json" 

- NPM can install:

    - Globally 
    - Dev Tools used across applications
    - -g
- Local
    - application libraries
    - --save is not necessary any more


- What is Express? 

- Express: 
    - Express is a minimal and flexible Node.js web application framework.
    - EE and spring on the java side
      - simpler and written in a language with built in web interaction. 
  - Javascript is the programming language used to build Express applications.
     

**Asynchronous Code in Javascript**

- Application makes a request and provides a callback. 
    - get and time
    - normally this is a blocking request
    - instead the operation taken from the event queue and handed to a worker thread. 
    - when the worker thread completes it invokes the callback method.
- Javascript is single threaded. but the C++ runtime of the JavaScript Virtual Machine is not. 
  - it works the same in browser
  - all GUI systems are single threaded systems driven by and event loop.  
