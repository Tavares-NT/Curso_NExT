// Faça um conversor de temperatura que receba o valor Celsius e converta para Kelvin, Reaumur, Rankine e Fahrenheit.

import java.util.Scanner;

public class Ex01 {
  public static void main(String[] args) {
  
  Scanner leia = new Scanner(System.in);
  float celsius = 0.0f;

  System.out.printf("Informe a temperatura [Celsius]: ");
  celsius = leia.nextInt();
  leia.close();
  
  float kelvin = celsius + 273.15f;
  float reaumur = celsius * 0.8f;
  float rankine = (celsius * 1.8f) + 491.67f;
  float fahrenheit = (celsius * 1.8f) + 32f;

  System.out.printf("\nResultados:\n");
  System.out.printf("Kelvin = %.2f\n", kelvin);
  System.out.printf("Reaumur = %.2f\n", reaumur);
  System.out.printf("Rankine = %.2f\n", rankine);
  System.out.printf("Fahrenheit = %.2f\n", fahrenheit);
  }

}