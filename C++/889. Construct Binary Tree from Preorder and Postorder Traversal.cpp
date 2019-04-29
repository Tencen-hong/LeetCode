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
    TreeNode *constructFromPrePost(vector<int> &pre, vector<int> &post)
    {
        vector<int>::iterator it;
        it = find(post.begin(), post.end(), pre[0]);

        if (pre.size() && post.size() && it != post.end())
        {
            int rootval = pre[0];
            pre.erase(pre.begin());
            TreeNode *root = new TreeNode(rootval);
            vector<int> temp(post.begin(), it);
            root->left = constructFromPrePost(pre, temp);
            root->right = constructFromPrePost(pre, temp);
            return root;
        }
        return NULL;
    }
};