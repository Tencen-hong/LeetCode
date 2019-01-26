class Solution
{
  public:
    vector<vector<int>> ans;
    vector<int> temp_path;
    void help(int source, int target, vector<vector<int>> &graph)
    {
        if (temp_path.back() == target)
        {
            ans.push_back(temp_path);
        }
        else
        {
            for (int j = 0; j < graph[source].size(); j++)
            {
                temp_path.push_back(graph[source][j]);
                help(graph[source][j], target, graph);
                temp_path.pop_back();
            }
        }
    }
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>> &graph)
    {
        temp_path.push_back(0);
        //Deep traversal from 0 node, record this path when encountering path node = target
        help(0, graph.size() - 1, graph);
        return ans;
    }
};