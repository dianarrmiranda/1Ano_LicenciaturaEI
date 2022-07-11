package aula07.ex01;

public class Triangulo extends Forma {
    public double lado1, lado2, lado3;

	public Triangulo(double l1, double l2, double l3){
		this.lado1 = l1;
		this.lado2 = l2;
		this.lado3 = l3;
    }

	public void setTriangulo(double l1, double l2, double l3){
		this.lado1 = l1;
		this.lado2 = l2;
		this.lado3 = l3;
    }


	public double getLado1() {
		return lado1;
	}

	public double getLado2() {
		return lado2;
	}

	public double getLado3() {
		return lado3;
	}
	public static Boolean values(double lado1, double lado2, double lado3){
        boolean valid = false;
		if((lado1+lado2 > lado3)&&(lado1+lado3 > lado2)&&(lado2+lado3 > lado1)){
			valid = true;
		}
		return valid;
    }

	public String toString() {
		if(Boolean.TRUE.equals(values(lado1, lado2, lado3)))
            return String.format ("Lado1 - %s, Lado2 - %s, Lado3 - %s", lado1, lado2, lado3);
        else{
            return "Valores inválidos!";
        }
	}
	
	public double perimetro () {
		return lado1 + lado2 + lado3;
	}
	
	//Usando a fórmula de Heron
	public double area() {
		double s = perimetro() / 2;
		return Math.sqrt(s * (s-lado1) * (s-lado2) * (s-lado3));
	}

	@Override
    public boolean equals(Object o) {
        if (o == this) {
            return true;
        }
 
        if (!(o instanceof Triangulo)) {
            return false;
        }

        Triangulo t = (Triangulo) o;

        return Double.compare(lado1, t.lado1) == 0
			&& Double.compare(lado2, t.lado2) == 0
			&& Double.compare(lado3, t.lado3) == 0;
    }



}
