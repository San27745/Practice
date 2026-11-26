public class DecimalToBinary {
    public static void main(String[] args) {
        int dec = 7;
        int bin = 0;
        int pow = 1;

        while(dec > 0){
            int remainder = dec % 2;
            bin = bin + (remainder* pow);
            pow = pow *10;
            dec = dec / 2;
        } System.out.println("binary number is :" + bin);
    }
}
