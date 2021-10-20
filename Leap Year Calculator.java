import java.util.Scanner;
public class LeapYear {
	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);
	
	System.out.println("Enter a year: ");
	int year = input.nextInt();
	boolean year1;
	
	if (year % 4 == 0 ){
		year1 = true;
	}
	else {
		year1 = false;
	}
	if (year1 && (year % 100 == 0)) {
			year1 = true;
	}
	if (year1 || (year % 400 == 0)){
		System.out.println("Leap year");
	}
	else {
		System.out.println("Common year");
	}
	input.close();
}
}
