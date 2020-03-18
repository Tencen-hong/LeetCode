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
    /*如果两个树都是空树，那么可以互相得到。如果两个数有一个是空，另一个不空，那么一定不能互相得到。如果两个树的节点的值不等，也不能互相得到。
    如果进行翻转，那么root1的左子树可以通过root2的右子树得到，同时root1的左子树通过root2的右子树得到；如果不进行翻转，那么root1和root2的对应左右子树通过操作应该也能互相得到。
    */
    bool flipEquiv(TreeNode *root1, TreeNode *root2)
    {
        if (root1 == nullptr && root2 == nullptr)
            return true;
        if (root1 == nullptr && root2 != nullptr)
            return false;
        if (root1 != nullptr && root2 == nullptr)
            return false;
        if (root1->val != root2->val)
            return false;
        return (flipEquiv(root1->left, root2->left) && flipEquiv(root1->right, root2->right)) || (flipEquiv(root1->left, root2->right) && flipEquiv(root1->right, root2->left));
    }
};