package quiz1.coba3;

public class Payment {
    private Course course;
    private double amount;
    private String paymentStatus;
    private Date transactionDate;

    // Constructor
    public Payment(Course nameCourse,String paymentStatus, double amount, Date transactionDate) {
        this.paymentStatus = paymentStatus;
        this.amount = amount;
        this.transactionDate = transactionDate;
        this.course = nameCourse;
        
    }

    // Method untuk menampilkan detail pembayaran
    public void showPaymentDetails() {
        System.out.println("\n=== Payment Details ===");
        System.out.println("Course Name     : " + course.getCourseName());
        System.out.println("Payment Status  : " + paymentStatus);
        System.out.println("Amount Paid     : $" + amount);
        System.out.println("Transaction Date: " + transactionDate.getFormattedDate());
        System.out.println("===========================");
    }

}
