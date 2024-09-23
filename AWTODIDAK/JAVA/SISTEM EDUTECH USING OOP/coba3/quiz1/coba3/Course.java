package quiz1.coba3;

import java.util.ArrayList;

public class Course {
    private String courseCode;
    private String courseName;
    private String description;
    private int duration; // dalam jam
    private double price;
    private ArrayList<Content> contents; // ArrayList untuk menyimpan konten

    public Course(String courseCode, String courseName, String description, int duration, double price) {
        this.courseCode = courseCode;
        this.courseName = courseName;
        this.description = description;
        this.duration = duration;
        this.price = price;
        this.contents = new ArrayList<>(); // Inisialisasi ArrayList
    }

    public void showCourseDetails() {
        System.out.println("\n=== Course Details ===");
        System.out.println("Course Code  : " + courseCode);
        System.out.println("Course Name  : " + courseName);
        System.out.println("Description  : " + description);
        System.out.println("Duration     : " + duration + " hours");
        System.out.println("Price        : $" + price);
        System.out.println("Number of Contents: " + contents.size()); // Menampilkan jumlah konten
        System.out.println("=======================");
    }

    // Method untuk menampilkan semua konten yang ada dalam kursus
    public void showAllContents() {
        System.out.println("\n--- All Contents for Course: " + courseName + " ---");
        for (Content content : contents) {
            content.showContentDetails();
        }
    }

    // Method untuk menambahkan konten ke kursus dari mentor
    public void addContent(Content content) {
        contents.add(content);
    }

    public String getCourseName() {
        return courseName;
    }

    public String getCourseCode() {
        return courseCode;
    }
}
