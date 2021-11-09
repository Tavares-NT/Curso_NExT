// Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

import java.util.Scanner;


public class Ex03 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.printf("Informe o 1º número: ");
        int x = input.nextInt();
        System.out.printf("Informe o 2º número: ");
        int y = input.nextInt();

        input.close();
       
        int soma = 0;
       
        if (x > y) {
            for (int i = x-1; i > y; i--) {
                if (i % 2 != 0) {
                    soma += i;
                }
            }
        } else {
           for (int i = x; i < y; i++) {
                if (i % 2 != 0) {
                    soma += i;
                }
            }
        }
       
        System.out.println(soma);

    }
}