package quiz1.coba3;

public class Main {
        public static void main(String[] args) {
                // Buat beberapa object
                Course course1 = new Course("C101", "Java Programming", "Learn Java from basics to advanced", 40, 200);
                Course course2 = new Course("C102", "Python Programming", "Learn Python from basics to advanced", 30,
                                150);

                Mentor mentor1 = new Mentor("Irwan", "irwan@gmail.com", 10, "USA");
                Mentor mentor2 = new Mentor("Joko", "joko@gmail.com", 5, "UK");

                // Membuat beberapa konten dan menambahkannya ke kursus
                // Course 1
                Content content1 = new Content(course1, "Introduction to Java", "Basic concepts of Java programming",
                                "Video", mentor1);
                Content content2 = new Content(course1, "Java OOP", "Object-Oriented Programming in Java", "Article",
                                mentor1);
                Content content3 = new Content(course1, "Java Collections", "Collections in Java", "Video", mentor1);

                // Mentor1 menambahkan konten ke course1
                mentor1.assignContent(content1);
                course1.addContent(content1); // Menambahkan konten ke kursus
                mentor1.assignContent(content2);
                course1.addContent(content2);
                mentor1.assignContent(content3);
                course1.addContent(content3);

                // Course 2
                Content content4 = new Content(course2, "Introduction to Python",
                                "Basic concepts of Python programming", "Video", mentor2);
                Content content5 = new Content(course2, "Python OOP", "Object-Oriented Programming in Python",
                                "Article", mentor2);
                Content content6 = new Content(course2, "Python Collections", "Collections in Python", "Video",
                                mentor2);

                // Mentor2 menambahkan konten ke course2
                mentor2.assignContent(content4);
                course2.addContent(content4);
                mentor2.assignContent(content5);
                course2.addContent(content5);
                mentor2.assignContent(content6);
                course2.addContent(content6);

                // Tampilkan detail kursus dan kontennya
                System.out.println("\n--- Course 1 Details ---");
                course1.showCourseDetails();
                course1.showAllContents();

                System.out.println("\n--- Course 2 Details ---");
                course2.showCourseDetails();
                course2.showAllContents();

                // Buat objek mahasiswa
                Student student1 = new Student("Alice Smith", "S123", "alice@gmail.com", "UK", 22, "Female");

                // Pendaftaran
                Date enrollmentDate = new Date(2024, 9, 21);
                Enrollment enrollment1 = new Enrollment(student1, course1, enrollmentDate, "Ongoing");
                enrollment1.showEnrollmentDetails();

                // Buat pembayaran
                Payment payment1 = new Payment(course1, "Paid", 200, enrollmentDate);
                payment1.showPaymentDetails();
        }
}
