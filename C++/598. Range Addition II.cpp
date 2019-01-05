class Solution {
public:

    int maxCount(int m, int n, vector<vector<int>>& ops) {
        int min_a = m, min_b = n;
        for (auto &it : ops) {
            if (it[0] < min_a)
                min_a = it[0];
            if (it[1] < min_b)
                min_b = it[1];
        }
        return min_a * min_b;
    }
};