//Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.

import java.util.Scanner;
public class Ex06 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        while (true) {
            System.out.printf("Digite o primeiro número: ");
            int x = input.nextInt();
            System.out.printf("Digite o segundo número: ");
            int y = input.nextInt();

            if (x == y) return;
                
            String resultado = (x > y)? "Decrescente":"Crescente";
            System.out.println(resultado);
        }
    }
}