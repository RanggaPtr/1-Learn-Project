package quiz1.coba3;

public class Date {
    private int year;
    private int month;
    private int day;

    public Date(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }

    public String getFormattedDate() {
        return day + "/" + month + "/" + year;
    }

}
