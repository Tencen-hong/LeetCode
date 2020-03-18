class Solution
{
public:
    set<int> visited;
    void VisitRooms(vector<vector<int>> &rooms, int room_number)
    {
        visited.insert(room_number);
        for (int j = 0; j < rooms[room_number].size(); j++)
        {
            if (visited.count(rooms[room_number][j]) == 0)
                VisitRooms(rooms, rooms[room_number][j]);
        }
    }
    bool canVisitAllRooms(vector<vector<int>> &rooms)
    {

        VisitRooms(rooms, 0);
        if (visited.size() == rooms.size())
            return true;
        return false;
    }
};