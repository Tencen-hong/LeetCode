class Solution
{
  public:
    struct node
    {
        int x = 0;
        int y = 0;
    };
    bool judgeCircle(string moves)
    {
        node pos;
        for (int i = 0; i < moves.size(); i++)
        {
            switch (moves[i])
            {
            case 'U':
                pos.y += 1;
                break;
            case 'D':
                pos.y -= 1;
                break;
            case 'L':
                pos.x -= 1;
                break;
            case 'R':
                pos.x += 1;
                break;
            }
        }
        if (pos.x == 0 && pos.y == 0)
            return true;
        else
            return false;
    }
};