class Solution {
public:
    static bool cmp1(int a, int b) {
        return a < b;
    }
    int findMinDifference(vector<string>& timePoints) {
        vector<int> time_points;
        for (auto &it : timePoints) {
            int temp_time = ((it[0] - '0') * 10 + (it[1] - '0') ) * 60 + ((it[3] - '0') * 10 + (it[4] - '0'));
            time_points.push_back(temp_time);
        }// convert string_time to int_time

        sort(time_points.begin(), time_points.end(), cmp1); // sort int_time from small to large
        int ans = 999999;

        for (int i = 1; i < time_points.size(); i++) {
            ans = min(time_points[i] - time_points[i - 1], ans);
        }// find minimun minutes between Adjacent time points
        ans = min(ans, 1440 - time_points[time_points.size() - 1] + time_points[0]); // situation last point and first point
        return ans;
    }
};