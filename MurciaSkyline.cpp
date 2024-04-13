#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

bool greaterThan(int a, int b) {
    return a > b;
}

bool lessThan(int a, int b) {
    return a < b;
}

int longestSubsequence(const vector<int>& heights, const vector<int>& widths, bool (*compare)(int, int)) {
    vector<int> subSequences(widths.begin(), widths.end());

    for (int i = 1; i < heights.size(); ++i) {
        for (int j = 0; j < i; ++j) {
            if (compare(heights[i], heights[j])) {
                subSequences[i] = max(subSequences[i], subSequences[j] + widths[i]);
            }
        }
    }

    return *max_element(subSequences.begin(), subSequences.end());
}

int main() {
    int testCases;
    cin >> testCases;
    cin.ignore(); // Ignore newline after reading test cases

    stringstream answer;

    for (int testCase = 0; testCase < testCases; ++testCase) {
        int numCases;
        cin >> numCases;
        vector<int> heights(numCases);
        vector<int> widths(numCases);

        for (int i = 0; i < numCases; ++i) {
            cin >> heights[i];
        }

        for (int i = 0; i < numCases; ++i) {
            cin >> widths[i];
        }

        int increasingLength = longestSubsequence(heights, widths, greaterThan);
        int decreasingLength = longestSubsequence(heights, widths, lessThan);

        if (increasingLength >= decreasingLength) {
            answer << "Case " << testCase + 1 << ". Increasing (" << increasingLength << "). Decreasing (" << decreasingLength << ").";
        } else {
            answer << "Case " << testCase + 1 << ". Decreasing (" << decreasingLength << "). Increasing (" << increasingLength << ").";
        }

        if (testCase + 1 != testCases) {
            answer << endl;
        }
    }

    cout << answer.str() << endl;

    return 0;
}
