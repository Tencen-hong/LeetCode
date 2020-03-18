class Solution
{
public:
    int distributeCandies(vector<int> &candies)
    {
        map<int, int> myMap;
        for (int i = 0; i < candies.size(); i++)
        {
            myMap[candies[i]]++;
        }
        return myMap.size() > candies.size() / 2 ? candies.size() / 2 : myMap.size();
    }
};