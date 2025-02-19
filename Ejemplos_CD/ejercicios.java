public boolean ePrimo() {
    for (int n = 2/*1*/; n * n < numero/*2*/; n++/*5*/) {
        if (numero % n == 0/*3*/) {
            return false/*4*/;
        }
    }
    return true/*6*/;
}/*7*/

/* 
                1
                |
                |
            |---2---|
            |       6
        |---3---|   |
        5       4   |
                |---|
                  |                
                  7 
  
*/


public String ganador(String xogada1, String xogada2) {
    String resultado/*1*/;
    if (xogada1.equals(xogada2)/*2*/) {
        resultado = "EMPATE"/*3*/;
    } else if (xogada1.equals("PEDRA")/*4*/ && xogada2.equals("PAPEL")/*5*/) {
        resultado = "Gaña o xogador 2"/*6*/;
    } else if (xogada1.equals("PAPEL")/*7*/ && xogada2.equals("TESOIRAS")/*8*/) {
        resultado = "Gaña o xogador 2"/*9*/;
    } else if (xogada1.equals("TESOIRAS")/*10*/ && xogada2.equals("PEDRA")/*11*/) {
        resultado = "Gaña o xogador 2"/*12*/;
    } else {
        resultado = "Gaña o xogador 1"/*13*/;
    }
    return resultado/*14*/;
}