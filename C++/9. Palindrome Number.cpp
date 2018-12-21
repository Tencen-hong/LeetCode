
class Solution {
public:
    bool isPalindrome(int x) {
        //if negative return false
        if (x < 0)
            return false;

        //make a copy of x
        int x_copy = x;

        //make a reverse of x
        int x_reverse = 0;

        while (x_copy > 0) {
            x_reverse = x_reverse * 10 + x_copy % 10;
            x_copy = x_copy / 10;
        }

        //if x_reverse == x  it's a palindrome
        if (x == x_reverse)
            return true;
        //if not
        return false;

    }
};