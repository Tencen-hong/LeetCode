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
    void post_order(TreeNode *&root)
    {
        if (root == NULL)
            return;
        post_order(root->left);
        post_order(root->right);
        if (root->val == 0)
        {
            if (root->left == NULL && root->right == NULL)
            {
                TreeNode *p = root;
                free(p);
                root = NULL;
            }
        }
    }
    TreeNode *pruneTree(TreeNode *root)
    {
        //Post-order traversal, set the 0 leaf node to NULL，This way, the pruning operation can be completed one by one.
        post_order(root);
        return root;
    }
};