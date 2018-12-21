
class Solution {
public:
    int reverse(int x) {
        long flag = 1;
        long res = 0;

        if (x < 0) {
            x = -x;
            flag = -1;
        }


        while (x) {
            res = res * 10 + x % 10;
            x /= 10;
        }

        res = flag * res;
        
        if (res < -pow(2, 31) || res > pow(2, 31) - 1)
            return 0;
        else
            return res;

    }
};