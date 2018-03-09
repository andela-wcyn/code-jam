import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class SeatingChart {
	public static void main(String[] args) throws FileNotFoundException {
		File file = new File("C-small-practice.in");
		Scanner keyboard = new Scanner(file);

		int number = keyboard.nextInt();
		ArrayList<String> array = new ArrayList<String>(number);
		keyboard.nextLine();
		for (int i = 0; i < number; i++) {
			array.add(keyboard.nextLine());
		}

		int possibleCombo = 0;
		for (int i = 0; i < array.size(); i++) {
			possibleCombo++;
			String ara = array.get(i);
			int n = Integer.parseInt(ara.substring(0, ara.indexOf(" ")));
			ara = ara.substring(ara.indexOf(" "));
			int k = Integer.parseInt(ara.substring(0, ara.indexOf(" ")));
			System.out.println("Case #" + (i + 1) + ": " + possibleCombo);
			System.out.println("| " + n + ", " + k + " |");
		}
	}
}