//Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y.Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

import java.util.Scanner;

public class Ex05 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.printf("Informe a quantidade de casos de teste: ");
        int n = input.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.printf("Digite o primeiro número: ");
            int x = input.nextInt();
            System.out.printf("Digite o segundo número: ");
            int y = input.nextInt();

            int soma = 0;
            if (x > y) {
                for (int j = x-1; j > y; j--) {
                    if (j % 2 != 0) soma += j;
                }
            } else if (x < y) {
                for (int j = x+1; j < y; j++) {
                    if (j % 2 != 0) soma += j;
                }
            }
            System.out.println(soma);
        }
        input.close();
    }
}