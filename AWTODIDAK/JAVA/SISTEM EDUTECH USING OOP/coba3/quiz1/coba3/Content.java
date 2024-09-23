package quiz1.coba3;


public class Content {
    private Course course;
    private String contentTitle;
    private String contentDescription;
    private String typeOfContent;
    private Mentor mentor;

    public Content(Course course, String contentTitle, String contentDescription, String typeOfContent, Mentor mentor) {
        this.course = course;
        this.contentTitle = contentTitle;
        this.contentDescription = contentDescription;
        this.typeOfContent = typeOfContent;
        this.mentor = mentor;
    }

    public void showContentDetails() {
        System.out.println("\n--- Content Details ---");
        System.out.println("Course Name: " + course.getCourseName());
        System.out.println("Content Title: " + contentTitle);
        System.out.println("Description: " + contentDescription);
        System.out.println("Type of Content: " + typeOfContent);
        System.out.println("Mentor Name: " + mentor.getNameOfMentor());
        System.out.println("------------------------");
    }

    public String getContentTitle() {
        return contentTitle;
    }
}
