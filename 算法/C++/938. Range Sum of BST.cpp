/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int sum = 0;
    void preorder(TreeNode* root, int L, int R) {
        if (root == NULL)
            return;
        //The value is accumulated between L and R
        if (root->val >= L && root->val <= R)
            sum += root->val;
        preorder(root->left, L, R);
        preorder(root->right, L, R);
    }
    int rangeSumBST(TreeNode* root, int L, int R) {
        //Preorder traversal of binary tree
        preorder(root, L, R);

        return sum;
    }
};