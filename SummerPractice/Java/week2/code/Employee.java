package week2.code;

public class Employee extends Person implements Greetable {
    private String company; 

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company; 
    }

    @Override
    public void introduce() {
        super.introduce();
        System.out.println("I work at: " + company); 
    }

    @Override 
    public void greet() {
        System.out.println("Hello, welcome to: " + company); 
    }
}
