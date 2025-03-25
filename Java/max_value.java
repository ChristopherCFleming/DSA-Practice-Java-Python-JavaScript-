class Source {
    public static double maxValue(double[] numbers) {
        double largest = numbers[0];

        for (int i = 0; i < numbers.length; i++) {
            double next = numbers[i];
            if ( next > largest) {
                largest = next;
            }
        }
        return largest;
    }

}

double[] numbers = { 4, 7, 2, 8, 10, 9 };
Source.maxValue(numbers); // -> 10