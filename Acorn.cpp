#include<iostream>
#include<vector>
#include<sstream>
using namespace std;

int collectAcorns(vector<vector<int> > acorns, int trees, int height, int fly) {
    vector<vector<int> > results(trees, vector<int>(height, -1));
    vector<int> acornsByHeight(height, 0);
    // Initialize the top row of the results matrix
    for (int t = 0; t < trees; t++) {
        results[t][height - 1] = acorns[t][height - 1];
        acornsByHeight[height - 1] = max(acornsByHeight[height - 1], results[t][height - 1]);
    }

    // Calculate the maximum acorns for each tree and height
    for (int h = height - 2; h >= 0; h--) {
        bool canFly = h + fly < height;

        // Check if it's worth descending down the same tree or flying towards another.
        for (int t = 0; t < trees; t++) {
            results[t][h] = max(results[t][h + 1], canFly ? acornsByHeight[h + fly] : 0) + acorns[t][h];
        }

        // Update value for this height
        for (int t = 0; t < trees; t++) {
            acornsByHeight[h] = max(acornsByHeight[h], results[t][h]);
        }
    }

    // Find the maximum acorns that can be collected from any tree
    int maxAcorns = 0;
    for (int t = 0; t < trees; t++) {
        maxAcorns = max(maxAcorns, results[t][0]);
    }

    return maxAcorns;
}

int main() {
    int c, t, h, f;
    stringstream response; // Create a stringstream object
    cin >> c;
    while (c--) {
        cin >> t >> h >> f;

        // Initialize vectors based on input
        vector<vector<int> > acorns(t, vector<int>(h, 0));

        // Fill acorns vector with the given data
        for (int i = 0; i < t; i++) {
            int a;
            cin >> a;
            while (a--) {
                int p;
                cin >> p;
                acorns[i][p - 1]++;
            }
        }

        int maxAcorns = collectAcorns(acorns, t, h, f);
        response << maxAcorns << endl;
    }

    cout << response.str();
    return 0;
}
