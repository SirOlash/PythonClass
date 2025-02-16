public class NumberSearch {
    public static void main(String[] args) {

        int [] numbers = {12,17,24,32,14};
        int numberCheck = 12;

        for(int index=0; index<numbers.length; index++){
            if (numberCheck == numbers[index]){
                System.out.println(index);
            }
        }

    }
}
