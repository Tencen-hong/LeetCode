class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int one = 0, two = 0, three = 0;
        // The decimal number appears 3 times, and the corresponding binary number also appears 3 times. All the numbers are expanded into binary. The purpose is to find out that each bit appears once (clearing 0 after 3 times) Happening.
        for (int i = 0; i < nums.size(); i++) {
            two = two | (one & nums[i]); //There are 2 occurrences, the previous one-bit status & this new occurrence. If a certain position appears twice, then the result is 1 and assigned to two. If it does not appear 2 times, the result is 0, then two retains the previous state.
            one = one ^ nums[i];//A bit appears once, if it appears 2 times, it is cleared.
            three = one & two; //Appeared 3 times
            one = one & ~three; //Clear 0 appears 3 times
            two = two & ~three; //Clear 0 appears 3 times
        }
        return one;
    }
};