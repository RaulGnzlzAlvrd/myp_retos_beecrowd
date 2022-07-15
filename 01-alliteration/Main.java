import java.util.Scanner;

public class Main {
	/**
	 * Regresa el número de aliteraciones en line, usando el algoritmo explicado en
	 * el Readme.txt
	 *
	 * @param line La cadena de texto a la que se le calcula el número de aliteraciones
	 * @return El número de aliteraciones
	 */
	public static int getAlliterations(String line) {
		String[] words = line.split(" ");
		int alliterations = 0;
		int consecutiveLetters = 1;
		char lastLetter = ' ';
		char currentLetter;
		for(String word: words) {
			currentLetter = word.charAt(0);
			if(currentLetter == lastLetter) {
				consecutiveLetters++;
				if(consecutiveLetters == 2) {
					alliterations++;
				}
			} else {
				lastLetter = currentLetter;
				consecutiveLetters = 1;
			}
		}
		return alliterations;
	}

	/**
	 * Punto de entrada del programa, toma como entrada estándar una línea de
	 * texto, e imprime en pantalla el número de aliteraciones contenidas.
	 */
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		while(scan.hasNextLine()) {
			String line = scan.nextLine();
			line = line.toLowerCase();
			int alliterations = getAlliterations(line);
			System.out.println(alliterations);
		}
	}
}
