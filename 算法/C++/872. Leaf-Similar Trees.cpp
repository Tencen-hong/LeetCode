/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution
{
  public:
    void getLeafOrder(TreeNode *root, vector<int> &order)
    {
        if (root == NULL)
        {
            return;
        }
        if (root->left == NULL && root->right == NULL)
        {
            order.push_back(root->val);
        }
        getLeafOrder(root->left, order);
        getLeafOrder(root->right, order);
    }
    bool leafSimilar(TreeNode *root1, TreeNode *root2)
    {
        vector<int> order1, order2;
        getLeafOrder(root1, order1);
        getLeafOrder(root2, order2);
        bool ans = true;
        if (order1.size() != order2.size())
        {
            ans = false;
        }
        else
        {
            for (int i = 0; i < order1.size(); ++i)
            {
                if (order1[i] != order2[i])
                {
                    ans = false;
                }
            }
        }
        return ans;
    }
};