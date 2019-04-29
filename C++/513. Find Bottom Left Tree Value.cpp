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
    TreeNode *res;
    int depth = -1;
    void preOrder(TreeNode *root, int level)
    {
        if (root != NULL)
        {
            if (level > depth)
            {
                depth = level;
                res = root;
            }
            preOrder(root->left, level + 1);
            preOrder(root->right, level + 1);
        }
    }
    int findBottomLeftValue(TreeNode *root)
    {
        preOrder(root, 0);
        return res->val;
    }
};