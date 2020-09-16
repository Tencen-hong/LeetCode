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
    TreeNode *invertTree(TreeNode *root)
    {
        if (root == NULL)
        {
            return root;
        }
        queue<TreeNode *> Queue;
        Queue.push(root);
        while (!Queue.empty())
        {
            TreeNode *top = Queue.front();
            Queue.pop();
            TreeNode *t = top->left;
            top->left = top->right;
            top->right = t;
            if (top->left)
            {
                Queue.push(top->left);
            }
            if (top->right)
            {
                Queue.push(top->right);
            }
        }
        return root;
    }
};