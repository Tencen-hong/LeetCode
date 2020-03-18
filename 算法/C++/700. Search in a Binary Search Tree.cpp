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
    TreeNode *ans;
    TreeNode *searchBST(TreeNode *root, int val)
    {
        if (root != NULL)
        {
            if (root->val == val)
            {
                ans = root;
            }
            searchBST(root->left, val);
            searchBST(root->right, val);
        }
        return ans;
    }
};