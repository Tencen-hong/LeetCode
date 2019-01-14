class Solution
{
  public:
    /*
    The idea is to find the original sequence, so that the original sequence is subjected to regular transformation to obtain an ascending sequence.
Regularity: Sort the original sequence in descending order, move the last element of <vector>ans to the first position, and then insert the largest number from the descending sequence into the first position of <vector>ans.
The sequence is finally obtained.
    */
    static bool cmp1(int a, int b)
    {
        return a > b;
    }
    vector<int> deckRevealedIncreasing(vector<int> &deck)
    {
        sort(deck.begin(), deck.end(), cmp1);
        vector<int> ans;
        for (int i = 0; i < deck.size(); i++)
        {
            if (!ans.empty())
            {
                int temp = ans.back();
                ans.pop_back();
                ans.insert(ans.begin(), temp);
            }
            ans.insert(ans.begin(), deck[i]);
        }
        return ans;
    }
};