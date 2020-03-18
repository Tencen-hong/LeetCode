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
    void insert(TreeNode *&root, int val)
    {
        if (root == NULL)
        {
            root = new TreeNode(val);
            return;
        }
        if (root->val < val)
            insert(root->right, val);
        else if (root->val > val)
            insert(root->left, val);
    }
    TreeNode *insertIntoBST(TreeNode *root, int val)
    {
        insert(root, val);
        return root;
    }
};