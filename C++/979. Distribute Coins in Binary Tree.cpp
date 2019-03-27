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
    /*从叶子到跟寻找，对于每个节点，只能剩下一个。多了的值肯定要全给父亲，少的值全问父亲要，统计一下就好了*/
    int distributeCoins(TreeNode *root)
    {
        ans = 0;
        dfs(root);
        return ans;
    }
    int dfs(TreeNode *root)
    {
        if (root == nullptr)
            return 0;
        int left = dfs(root->left);
        int right = dfs(root->right);
        ans += abs(left) + abs(right);
        return root->val - 1 + left + right;
    }

  private:
    int ans;
};