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

    public static void run() {
        // this function behaves as `main()` for the 'run' command
        // you may sandbox in this function, but should not remove it
    }
}