class Solution
{
  public:
    struct node
    {
        int distance;
        int index;
    };
    static bool cmp1(node a, node b)
    {
        return a.distance < b.distance;
    }
    vector<vector<int>> kClosest(vector<vector<int>> &points, int K)
    {
        vector<vector<int>> ans;
        vector<node> Distance;

        int x, y;
        double distance;
        for (int i = 0; i < points.size(); i++)
        {
            x = points[i][0];
            y = points[i][1];
            distance = pow(x, 2) + pow(y, 2);

            node temp;
            temp.distance = distance;
            temp.index = i;
            Distance.push_back(temp);
        }
        sort(Distance.begin(), Distance.end(), cmp1);
        for (int i = 0; i < K; i++)
        {
            ans.push_back(points[Distance[i].index]);
        }
        return ans;
    }
};