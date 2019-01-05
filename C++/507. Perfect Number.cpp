class Solution {
public:
    bool checkPerfectNumber(int num) {
        int c = pow(num, 0.5) + 1;
        set<int> factors;
        if (num <= 3)
            return false;
        for (int i = 2; i <= c; i++) {
            if (num % i == 0)
            {
                factors.insert(i);
                factors.insert(num / i);
            }
        }
        int sum = 1;
        for (auto &it : factors)
        {
            sum += it;
        }
        if (sum == num)
            return true;
        return false;
    }
};