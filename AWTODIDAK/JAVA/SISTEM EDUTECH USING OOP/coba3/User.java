package quiz1.coba3;

public class User {
    private String name;
    private String email;

    // Konstruktor
    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }

    // Getter untuk nama
    public String getName() {
        return name;
    }

    // Getter untuk email
    public String getEmail() {
        return email;
    }

    // Setter untuk nama
    public void setName(String name) {
        this.name = name;
    }

    // Setter untuk email
    public void setEmail(String email) {
        this.email = email;
    }

    // Metode untuk menampilkan detail umum
    public void showPersonDetails() {
        System.out.println("Name : " + name);
        System.out.println("Email: " + email);
    }
}
