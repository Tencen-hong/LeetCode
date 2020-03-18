class Solution
{
public:
    int mincostTickets(vector<int> &days, vector<int> &costs)
    {
        vector<int> res(366, 0);
        for (int i = 0; i < days.size(); i++)
        {
            res[days[i]] = 1;
        }
        for (int i = 1; i < res.size(); i++)
        {
            if (res[i] == 0)
                res[i] = res[i - 1];
            else
            {
                res[i] = min(costs[0] + res[i - 1], min(costs[1] + res[max(i - 7, 0)], costs[2] + res[max(i - 30, 0)]));
            }
        }
        return res[days[days.size() - 1]];
    }
};