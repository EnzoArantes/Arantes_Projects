import java.util.Scanner;

public class BMICalculator {

    // Method to compute BMI based on height (in inches) and weight (in pounds)
    public static double computeBMI(double heightInInches, double weightInPounds) {
        double weightInKg = weightInPounds / 2.205;  // Convert weight to kilograms
        double heightInMeters = heightInInches / 39.37;  // Convert height to meters
        return weightInKg / (heightInMeters * heightInMeters);  // Calculate BMI
    }

    public static void main(String[] args) {
        // Try-with-resources to ensure Scanner is automatically closed
        try (Scanner input = new Scanner(System.in)) {

            System.out.println("This program computes and evaluates Body Mass Index (BMI)");

            // User input for height
            System.out.print("Enter height in feet: ");
            int heightFeet = input.nextInt();
            System.out.print("Enter height in inches: ");
            int heightInches = input.nextInt();
            System.out.print("Enter weight in pounds: ");
            double weight = input.nextDouble();

            // Convert height to total inches
            double height = (heightFeet * 12) + heightInches;
            System.out.println("Height is " + height + " inches");

            // Calculate BMI
            double bmi = computeBMI(height, weight);
            System.out.printf("Your Body Mass Index is %.1f%n", bmi);

            // Evaluate and print BMI category
            if (bmi >= 18.5 && bmi <= 25) {
                System.out.println("Normal Weight");
            } else if (bmi > 25) {
                System.out.println("Overweight");
            } else {
                System.out.println("Underweight");
            }
        }
    }
}
