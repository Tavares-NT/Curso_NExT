/*Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Exemplo de Saída

1 2 3 PUM
5 6 7 PUM
9 10 11 PUM
13 14 15 PUM
17 18 19 PUM
21 22 23 PUM
25 26 27 PUM
*/

import java.util.Scanner;

public class Ex07 {
	
    public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);
        System.out.printf("Digite o valor de N: ");
		int N = leitor.nextInt();
		int cont = 1;
        leitor.close();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < 3; j++) {
				System.out.print(cont + " ");
				cont++;
			}
			System.out.println("PUM");
			cont++;
		}
    }
}
