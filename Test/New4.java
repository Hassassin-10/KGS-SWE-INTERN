import java.util.Scanner;

class New4 {

    void fib(int n, int n1, int n2) {
        if (n <= 0) {
            return;
        }

        System.out.println(n1);
        fib(n - 1, n2, n1 + n2);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of terms: ");
        int n = sc.nextInt();

        New4 obj = new New4();
        obj.fib(n, 0, 1);

        sc.close();
    }
}