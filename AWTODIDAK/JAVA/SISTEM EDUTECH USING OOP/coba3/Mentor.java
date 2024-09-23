package quiz1.coba3;

public class Mentor extends User {
    private int experience; // dalam tahun
    private String country; // negara asal

    // Konstruktor
    public Mentor(String name, String email, int experience, String country) {
        super(name, email); // Memanggil konstruktor superclass (Person)
        this.experience = experience;
        this.country = country;
    }

    // Getter untuk experience
    public int getExperience() {
        return experience;
    }

    // Setter untuk experience
    public void setExperience(int experience) {
        this.experience = experience;
    }

    // Getter untuk country
    public String getCountry() {
        return country;
    }

    // Setter untuk country
    public void setCountry(String country) {
        this.country = country;
    }

    // Metode untuk menampilkan detail mentor
    @Override
    public void showPersonDetails() {
        super.showPersonDetails(); // Menampilkan detail dari superclass
        System.out.println("Experience : " + experience + " years");
        System.out.println("Country     : " + country);
    }

    // Metode spesifik Mentor
    public void assignContent(Content content) {
        System.out.println("\n" + getName() + " has assigned content: " + content.getContentTitle());

    }

    // Mengubah nama metode dari superclass
    public String getNameOfMentor() {
        return getName(); // Menggunakan getter dari superclass
    }
}
