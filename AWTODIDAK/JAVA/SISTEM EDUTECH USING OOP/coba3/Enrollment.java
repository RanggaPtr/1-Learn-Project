    package quiz1.coba3;

    public class Enrollment {
        private Student student;
        private Course course;
        private Date enrollmentDate;
        private String courseStatus;

        // Constructor
        public Enrollment(Student student, Course course, Date enrollmentDate, String courseStatus) {
            this.student = student;
            this.course = course;
            this.enrollmentDate = enrollmentDate;
            this.courseStatus = courseStatus;
        }

        // Method show details enrollment
        public void showEnrollmentDetails() {
            System.out.println("\n=== Enrollment Details ===");
            System.out.println("Student Name      : " + student.getStudentName());
            System.out.println("Course Name       : " + course.getCourseName());
            System.out.println("Enrollment Date   : " + enrollmentDate.getFormattedDate());
            System.out.println("Course Status     : " + courseStatus);
            System.out.println("===========================");
        }
    }
