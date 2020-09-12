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
    vector<double> averageOfLevels(TreeNode *root)
    {
        auto q = queue<TreeNode *>();
        auto ret = vector<double>();
        q.push(root);
        while (!q.empty())
        {
            double sum = 0;
            auto size = q.size();
            for (int i = 0; i < size; i++)
            {
                auto top = q.front();
                q.pop();
                sum += top->val;
                if (top->left)
                {
                    q.push(top->left);
                }
                if (top->right)
                {
                    q.push(top->right);
                }
            }
            ret.push_back(sum / size);
        }
        return ret;
    }
};