//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class licz_pi {
    public static void main(String[] args) {
        float pi;
        float mnoznik = 4.0f;

        pi = mnoznik;
        int dokladnosc = Integer.valueOf(args[0]);
        int licznik = 0;
        float mianownik = 3;


        while(licznik <= dokladnosc) {
            pi -= (mnoznik) / mianownik;
            mianownik += 2;
            pi += (mnoznik) / mianownik;
            mianownik += 2;
            licznik++;

        }
        pi = (pi*4)/mnoznik;
        System.out.println(pi);
    }
}