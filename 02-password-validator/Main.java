import java.util.Scanner;

public class Main {
	/**
	 * Predicado indicando si password es una contraseña válida
	 * según los siguientes requisitos:
	 * - Debe contener al menos una letra mayúscula, una minúscula y un número
	 * - No puede tener signos de puntuación, acentos ni espacios
	 * - La contraseña debe tener de 6 a 32 caracteres
	 *
	 * @param password: la contraseña a validar
	 * @return true si la contraseña es válida, false en otro caso
	 */
	public static boolean validPassword(String password) {
		boolean[] conditions = {false, false, false, false};
		int size = 0;
		for(char character : password.toCharArray()) {
			if(!Character.isLetterOrDigit(character))
				return false;
			if(Character.isLowerCase(character))
				conditions[0] = true;
			if(Character.isUpperCase(character))
				conditions[1] = true;
			if(Character.isDigit(character))
				conditions[2] = true;
			size++;
		}
		conditions[3] = size >= 6 && size <= 32;
		return allTrue(conditions);
	}

	/**
	 * Predicado que indica si todos los elementos de flags son
	 * verdaderos.
	 *
	 * @param flags: el arreglo a revisar
	 * @return true si todos los elementos son verdaderos, false en otro caso
	 */
	public static boolean allTrue(boolean[] flags) {
		for(boolean flag : flags) {
			if(!flag)
				return false;
		}
		return true;
	}

	/**
	 * Lógica base del programa, lee todas las lineas hasta EOF.
	 * Cada linea es una contraseña a validar,
	 * imprime "Senha valida." si la contraseña es válida,
	 * imprime "Senha invalida." si la contraseña no es válida.
	 */
	public static void run() {
		Scanner scan = new Scanner(System.in);
		while(scan.hasNextLine()) {
			String password = scan.nextLine();
			if(validPassword(password)) {
				System.out.println("Senha valida.");
			} else {
				System.out.println("Senha invalida.");
			}
		}
	}

	/**
	 * Casos de prueba que vienen en la descripción del
	 * problema en URI.
	 */
	public static void test() {
		String[] passwords = {"URI Online Judge",
							  "AbcdEfgh99",
							  "URIOnlineJudge12",
						 	  "URI Online Judge 12",
						 	  "Aass9",
						 	  "Aassd9"};
		boolean[] expected = {false, true, true, false, false, true};
		for(int i=0; i < passwords.length; i++) {
			boolean condition = validPassword(passwords[i]) == expected[i];
			if(!condition) {
				System.out.println("Error en '" + passwords[i] + "', se esperaba " + expected[i]);
			}
		}
		System.out.println("Todas las pruebas terminadas!");
	}

	/**
	 * Punto de entrada del programa. Dependiendo de los argumentos
	 * ejecuta las pruebas o la lógica principal del programa.
	 */
	public static void main(String[] args) {
		if(args.length > 0 && args[0].equals("--test")) {
			test();
		} else {
			run();
		}
	}
}
