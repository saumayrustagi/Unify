import java.util.Scanner;
import java.lang.Math;

class Matches {
	static Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		int tt = 4;
		while (tt-- > 0) {
			solve();
		}
	}

	static void solve(){
		String a = in.nextLine();
		String b = in.nextLine();

		// Strip Whitespace
		a = a.strip().toLowerCase();
		b = b.strip().toLowerCase();

		float c = new Levenshtein().ret_lev(a, b);
		System.out.println((c >= 1) + " " + c);
	}
}

class Levenshtein {

	float ret_lev(String a, String b) {

		String[] s1 = a.split(" ");
		String[] s2 = b.split(" ");
		InnerStandardize obj = new Computation();
		return obj.lvnshtn_sim(s1, s2);
	}

	interface InnerStandardize {
		float lvnshtn_dist(String a, String b);

		float lvnshtn_sim(String[] arr1, String[] arr2);
	}

	class Computation implements InnerStandardize {
		public float lvnshtn_dist(String a, String b) {

			/*
			 * Takes 2 strings and returns their levenshtein distance
			 */

			int n1 = a.length(), n2 = b.length();
			float dist = Math.max(n1, n2) - Math.min(n1, n2);
			for (int i = 0; i < Math.min(n1, n2); i++)
				if (a.charAt(i) != (b.charAt(i)))
					++dist;

			try {
				dist = dist / (n1 + n2);
			} catch (ArithmeticException e) {
				System.out.println("Something went Wrong during Calculation!");
			}
			return 1 - dist;
		}

		public float lvnshtn_sim(String[] arr1, String[] arr2) {

			/*
			 * arr1 = an array of Strings from correct
			 * arr2 = an array of Strings from input
			 */

			boolean flag = false;
			float lev = 0;
			float dissim = 0;

			for (int i = 0; i < arr1.length; i++) {
				flag = false;
				for (int j = 0; j < arr2.length; j++) {
					if (arr1[i].charAt(0) == arr2[j].charAt(0)) {
						float sim = lvnshtn_dist(arr1[i], arr2[j]);
						if (sim == 1.0)
							flag = false;
						lev += sim;
						break;
					} else
						flag = true;
				}
				if (flag == true)
					++dissim;
			}
			try {
				dissim = dissim / Math.max(arr1.length, arr2.length);
			} catch (ArithmeticException e) {
				System.out.println("Something went Wrong during Calculation!");
			}
			return lev - dissim;
		}
	}

}