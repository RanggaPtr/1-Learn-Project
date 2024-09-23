package quiz1.coba3;

public class Student extends User {
    private String studentID;
    private String country;
    private int age;
    private String gender;

    // Konstruktor
    public Student(String name, String email, String studentID, String country, int age, String gender) {
        super(name, email); // Memanggil konstruktor superclass (Person)
        this.studentID = studentID;
        this.country = country;
        this.age = age;
        this.gender = gender;
    }

    // Getter untuk studentID
    public String getStudentID() {
        return studentID;
    }

    // Setter untuk studentID
    public void setStudentID(String studentID) {
        this.studentID = studentID;
    }

    // Getter untuk country
    public String getCountry() {
        return country;
    }

    // Setter untuk country
    public void setCountry(String country) {
        this.country = country;
    }

    // Getter untuk age
    public int getAge() {
        return age;
    }

    // Setter untuk age
    public void setAge(int age) {
        this.age = age;
    }

    // Getter untuk gender
    public String getGender() {
        return gender;
    }

    // Setter untuk gender
    public void setGender(String gender) {
        this.gender = gender;
    }

    // Metode untuk menampilkan detail mahasiswa
    @Override
    public void showPersonDetails() {
        super.showPersonDetails(); // Menampilkan detail dari superclass
        System.out.println("Student ID  : " + studentID);
        System.out.println("Country     : " + country);
        System.out.println("Age         : " + age);
        System.out.println("Gender      : " + gender);
    }

    // Getter untuk nama mahasiswa menggunakan superclass
    @Override
    public String getName() {
        return super.getName();
    }

    // Getter untuk nama mahasiswa yang sebelumnya getStudentName
    public String getStudentName() {
        return getName(); // Menggunakan getter dari superclass
    }
}
