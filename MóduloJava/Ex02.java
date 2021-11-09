// Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

import java.util.Scanner;

public class Ex02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.printf("Informe o 1º número: ");
        int A = entrada.nextInt();
        System.out.printf("Informe o 2º número ");
        int B = entrada.nextInt();

        entrada.close();
        if (A % B == 0 || B % A == 0) {
            System.out.println("São Múltiplos");
        } else {
            System.out.println("Não são Múltiplos");

        }
    }

}
