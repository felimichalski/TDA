import java.util.Scanner;

interface Comparator {
    boolean compare(int a, int b);
}

class GreaterComparator implements Comparator {
    @Override
    public boolean compare(int a, int b) {
        return a > b;
    }
}

class LessComparator implements Comparator {
    @Override
    public boolean compare(int a, int b) {
        return a < b;
    }
}

class Main {
    static int longestSubsequenceLength(int[] heights, int[] widths, Comparator comparator) {
        // Initialize subsequences array with widths values (copy array)
        int[] subsequences = new int[widths.length];
        for(int i = 0; i < widths.length; i++) {
            subsequences[i] = widths[i];
        }

        // Calculate subsequences based on comparator and save the best results
        for (int i = 1; i < heights.length; ++i) {
            for (int j = 0; j < i; ++j) {
                if (comparator.compare(heights[i], heights[j])) {
                    subsequences[i] = Math.max(subsequences[i], subsequences[j] + widths[i]);
                }
            }
        }

        // Find the value of the longest subsequence and return it
        int max = subsequences[0];
        for (int i = 1; i < subsequences.length; i++) {
            if (subsequences[i] > max) {
                max = subsequences[i];
            }
        }
        return max;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCases = scanner.nextInt();

        StringBuilder answer = new StringBuilder();

        for (int testCase = 0; testCase < testCases; ++testCase) {
            int numCases = scanner.nextInt();
            
            // Read and save heights
            int[] heights = new int[numCases];
            for (int i = 0; i < numCases; ++i) {
                heights[i] = scanner.nextInt();
            }
            
            // Read and save widths
            int[] widths = new int[numCases];
            for (int i = 0; i < numCases; ++i) {
                widths[i] = scanner.nextInt();
            }

            // Retrieve longest subsequence based on comparator
            int increasingLength = longestSubsequenceLength(heights, widths, new GreaterComparator());
            int decreasingLength = longestSubsequenceLength(heights, widths, new LessComparator());

            // Compare retrieved values and append result
            if (increasingLength >= decreasingLength) {
                answer.append("Case ").append(testCase + 1).append(". Increasing (").append(increasingLength).append("). Decreasing (").append(decreasingLength).append(").");
            } else {
                answer.append("Case ").append(testCase + 1).append(". Decreasing (").append(decreasingLength).append("). Increasing (").append(increasingLength).append(").");
            }

            if (testCase + 1 != testCases) {
                answer.append("\n");
            }
        }

        scanner.close();

        System.out.println(answer.toString());
    }
}
