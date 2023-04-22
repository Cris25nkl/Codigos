public class Matematicas {

    public static void factorial(int n){
        int fac = 1;
        int i = 1;

        while (i <= n) {
            fac = fac * i;
            i++;
        }

        System.out.println(fac);  
    }

    public static void parImpar(int n){
        if (n % 2 == 0) {
            System.out.println("Par");
        }else System.out.println("Impar");
    }

    public static void primos(int n){
        int cont=0;

       for (int k = 1; k <= n; k = k+1) {
            if (n % k == 0) {
                cont = cont + 1;
            }
       }

        if (cont <= 2) {
            System.out.println("es primo");
        }else System.out.println("no es primo");
    }

}
