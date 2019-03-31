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
    int maxDepth(Node *root)
    {
        if (root == NULL)
            return 0;
        depth++;
        for (int i = 0; i < root->children.size(); i++)
        {
            maxDepth(root->children[i]);
        }
        ans = max(ans, depth);
        depth--;
        return ans;
    }

  private:
    int ans = 0;
    int depth = 0;
};