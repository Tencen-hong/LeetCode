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
    vector<int> ret;
    void inOrder(TreeNode *root)
    {
        if (root == NULL)
        {
            return;
        }

        inOrder(root->left);
        ret.push_back(root->val);
        inOrder(root->right);
    }
    vector<int> inorderTraversal(TreeNode *root)
    {
        inOrder(root);
        return ret;
    }
};