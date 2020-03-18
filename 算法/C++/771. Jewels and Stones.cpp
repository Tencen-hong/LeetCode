class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int Jewels_dict[128] = {0};
        for (int i = 0; i < J.size(); i++)
            Jewels_dict[J[i]] = 1;
        int count = 0;
        for (int i = 0; i < S.size(); i++) {
            if (Jewels_dict[S[i]] == 1)
                count++;
        }
        return count;
    }
};