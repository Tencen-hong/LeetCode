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
    int maxdepth = 0;
    TreeNode *res;
    int postOrder(TreeNode *root, int depth)
    {
        if (root == NULL)
            return depth;
        int leftDepth = postOrder(root->left, depth + 1);
        int rightDepth = postOrder(root->right, depth + 1);
        if (leftDepth == rightDepth && leftDepth >= maxdepth)
        {
            res = root;
            maxdepth = leftDepth;
        }
        return max(leftDepth, rightDepth);
    }
    TreeNode *subtreeWithAllDeepest(TreeNode *root)
    {
        postOrder(root, 0);
        return res;
    }
};