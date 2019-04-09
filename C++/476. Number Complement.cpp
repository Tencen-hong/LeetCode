class Solution
{
  public:
    int findComplement(int num)
    {
        bitset<32> ans_bit(num);
        for (int i = 0; i < ans_bit.size(); i++)
        {
            if (pow(2, i) > num)
            {
                break;
            }
            ans_bit.flip(i);
        }
        int ans = (int)ans_bit.to_ulong();
        return ans;
    }
};