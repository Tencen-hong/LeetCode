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
    bool preorder(TreeNode *root, int key)
    {
        if (root == NULL)
            return true;
        return (root->val == key) && preorder(root->left, key) && preorder(root->right, key);
    }
    bool isUnivalTree(TreeNode *root)
    {
        return preorder(root, root->val);
    }
};