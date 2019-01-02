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
    queue<TreeNode*> my_queue;
    vector<int> vec;
    void level_traverse(TreeNode* root) {
        my_queue.push(root);
        while (!my_queue.empty()) {
            TreeNode* temp = my_queue.front();
            vec.push_back(temp->val);
            my_queue.pop();
            if (temp->left)
                my_queue.push(temp->left);
            else if (temp->val != -1)
                my_queue.push(new TreeNode(-1));
            if (temp->right)
                my_queue.push(temp->right);
            else if (temp->val != -1)
                my_queue.push(new TreeNode(-1));
        }
    }
    bool isCompleteTree(TreeNode* root) {
        //Hierarchical traversal using queues
        level_traverse(root);
        //Null (ie -1) appears in the middle of the hierarchical traversal result, not a complete binary tree
        int flag_1 = 0, flag_2 = 0;
        for (int i = 0; i < vec.size(); i++) {
            if (vec[i] == -1)
                flag_1 = 1;
            if (flag_1 == 1 && vec[i] != -1)
                flag_2 = 1;
        }
        if (flag_1 == 1 && flag_2 == 1)
            return false;
        else
            return true;
    }
};