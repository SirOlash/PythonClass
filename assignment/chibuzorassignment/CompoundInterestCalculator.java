import java.util.Scanner;
public class CompoundInterestCalculator {

public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    double principal;
    double monthlyContribution;
    double lengthOfTime;
    double interestRate;
    double varianceRange;
    double temp = 1;
    double rate = 1 ;
    int frequency = 0;
    double noOfYears;
    double compoundInterest = 0;
    String compoundFrequency;
        //boolean principalCheck = true;
        while (true) {
            try {
                System.out.print("Enter principal: ");
                principal = input.nextDouble();
                if (principal <= 0) {
                    System.out.println("Principal can't be negative or zero");
                } else break;
            } catch (Exception e) {
                System.out.println("Invalid input");
                input.next();
            }
        }

        while (true) {
            try {
                System.out.print("Enter Your Monthly Contribution: (Amount that you plan to add to the principal every month, or a negative number for the amount that you plan to withdraw every month.): ");
                monthlyContribution = input.nextDouble();
                    break;
            } catch (Exception e) {
                System.out.println("Invalid input");
                input.next();
            }
        }

    while (true) {
        try {
            System.out.print("Enter the length of time in years ");
            lengthOfTime = input.nextDouble();
            if (lengthOfTime <= 0) {
                System.out.println("lengthOfTime can't be negative or zero");
            } else break;
        } catch (Exception e) {
            System.out.println("Invalid input");
            input.next();
        }
    }
    while (true) {
        try {
            System.out.print("Enter the Estimated interest Rate in percentage: ");
            interestRate = input.nextDouble();
            if (interestRate <= 0) {
                System.out.println("Interest Rate can't be negative or zero");
            } else break;
        } catch (Exception e) {
            System.out.println("Invalid input");
            input.next();
        }
    }

    while (true) {
        try {
            System.out.print("Enter your interest rate variance range: ");
            varianceRange = input.nextDouble();
            if (varianceRange < 0) {
                System.out.println("Interest Rate can't be negative");
            } else break;
        } catch (Exception e) {
            System.out.println("Invalid input");
            input.next();
        }
    }
    input.nextLine();
    while (true) {
        try {
            System.out.print("Enter the compound frequency(Daily/Monthly/Semi-yearly/quarterly/Yearly): ");
            compoundFrequency = input.nextLine();
            switch (compoundFrequency.toLowerCase()) {
                case "daily":
                    frequency = 365;
                    temp = monthlyContribution / (365/12);
                    break;
                case "monthly":
                    frequency = 12;
                    break;
                case "Semi-yearly":
                    frequency = 6;
                    temp = monthlyContribution * 6;
                    break;
                case "quarterly":
                    frequency = 3;
                    temp = monthlyContribution * 3;
                    break;
                case "yearly":
                    frequency = 1;
                    temp = monthlyContribution * 12;
                    break;
                default:
                    System.out.println("Invalid");
                    continue;
            }
            break;
        } catch (Exception e) {
            System.out.println("Invalid input");
        }

    }
    rate = (interestRate/100)/frequency;
    noOfYears = frequency * lengthOfTime;

    for (int index = 0; index < noOfYears; index++) {
        compoundInterest = compoundInterestOnPrincipal(interestRate,principal,frequency,lengthOfTime,rate,noOfYears) + compoundInterestOnMonthlyDeposit(interestRate,principal,frequency,lengthOfTime,rate,noOfYears,temp);
    }
    System.out.printf("Your Compound Interest is %.3f",compoundInterest);
}
public static double compoundInterestOnPrincipal(double interestRate,double principal, int frequency,double lengthOfTime,double rate,double noOfYears) {
    return principal * (Math.pow(1 + rate,noOfYears));
}

public static double compoundInterestOnMonthlyDeposit(double interestRate,double principal, int frequency,double lengthOfTime,double rate,double noOfYears,double temp) {
    return temp *((Math.pow(1 + rate,noOfYears)-1)/rate);
}

}
