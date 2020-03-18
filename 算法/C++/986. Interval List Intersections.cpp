/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution
{
  public:
    vector<Interval> intervalIntersection(vector<Interval> &A, vector<Interval> &B)
    {
        int n = A.size(), m = B.size();
        int i = 0, j = 0;
        vector<Interval> ans;
        while (i < n && j < m)
        {
            int s1 = A[i].start, e1 = A[i].end;
            int s2 = B[j].start, e2 = B[j].end;
            if (s1 <= s2)
            {
                if (e1 < s2)
                {
                    i++;
                }
                else
                {
                    ans.emplace_back(Interval(s2, min(e1, e2)));
                    if (e1 >= e2)
                    {
                        j++;
                    }
                    else
                    {
                        i++;
                    }
                }
            }
            else
            {
                if (e2 < s1)
                {
                    j++;
                }
                else
                {
                    ans.emplace_back(Interval(s1, min(e1, e2)));
                    if (e2 >= e1)
                    {
                        i++;
                    }
                    else
                    {
                        j++;
                    }
                }
            }
        }
        return ans;
    }
};