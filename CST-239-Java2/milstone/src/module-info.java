module milstone {
    requires com.fasterxml.jackson.databind;
    requires com.fasterxml.jackson.core;
    requires com.fasterxml.jackson.annotation;
    requires org.junit.jupiter.api;
    requires org.mockito;
    requires org.mockito.junit.jupiter;
	requires org.junit.platform.suite.api;
	requires net.bytebuddy;
  
    // This is likely the name you want, but it could vary
    // If using mockito-junit-jupiter, you may also need something like:
    // requires mockito.junit.jupiter;

    // If Mockito needs to do reflection on classes in the product package
    opens product to com.fasterxml.jackson.databind, mockito.core, org.mockito , org.junit.platform.commons;
    opens test to org.mockito , org.junit.platform.commons;

    exports product;
}

