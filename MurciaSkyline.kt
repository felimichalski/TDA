object MurciaSkyline {
    @JvmStatic
    fun main(args: Array<String>) {
        val testCases = readln().toInt()
        val answer = StringBuilder()
        repeat(testCases) { testCase ->
            readln() // Read the number of cases is useless in Kotlin because arrays are resizable
            val heights: List<Int> = readln().split("\\s+".toRegex()).map { it.toInt() }
            val widths: List<Int> = readln().split("\\s+".toRegex()).map { it.toInt() }

            val increasingLength = longestSubsequence(heights, widths) { a, b -> a > b }
            val decreasingLength = longestSubsequence(heights, widths) { a, b -> a < b }

            if (increasingLength >= decreasingLength) {
                answer.append("Case ${testCase + 1}. Increasing (${increasingLength}). Decreasing (${decreasingLength}).")
            } else {
                answer.append("Case ${testCase + 1}. Decreasing (${decreasingLength}). Increasing (${increasingLength}).")
            }
            if(testCase + 1 != testCases) {
                answer.append("\n")
            }
        }
        println(answer.toString())
    }

    private fun longestSubsequence(heights: List<Int>, widths: List<Int>, compare: (Int, Int) -> Boolean): Int {
        // Initialize subsequences list with widths values
        val subSequences = widths.toMutableList()

        for (i in 1..<heights.size) {
            for (j in 0..<i) {
                // If the condition is met then there is a new subsequence candidate
                if (compare(heights[i], heights[j])) {
                    // Verify if candidate is longer that current
                    subSequences[i] = maxOf(subSequences[i], subSequences[j] + widths[i])
                }
            }
        }

        return subSequences.maxOrNull() ?: 0
    }
}
