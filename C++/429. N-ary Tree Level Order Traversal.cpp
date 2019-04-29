/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution
{
public:
    vector<vector<int>> levelOrder(Node *root)
    {
        vector<vector<int>> res;
        queue<Node *> q;
        if (root == NULL)
            return res;
        q.push(root);
        while (q.size())
        {
            int size = q.size();
            vector<int> level;
            while (size--)
            {
                Node *temp = q.front();
                q.pop();
                level.push_back(temp->val);
                for (int i = 0; i < temp->children.size(); i++)
                {
                    q.push(temp->children[i]);
                }
            }
            res.push_back(level);
        }
        return res;
    }
};