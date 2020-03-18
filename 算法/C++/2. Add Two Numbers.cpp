/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {

        ListNode *res = NULL;

        // work node
        ListNode *p = res;
        // carry
        int carry = 0;

        // do while when (l1!=NULL || l2!=NULL || carry !=0)
        while (l1 || l2 || carry != 0) {

            //add l1->val and l2->val to carry
            if (l1) {
                carry += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                carry += l2->val;
                l2 = l2->next;
            }

            // if res is head node
            if (res == NULL) {
                // construct a node with value = carry % 10
                res = new ListNode(carry % 10);
                p = res;
            } else {
                // construct a node with value = carry % 10
                p->next = new ListNode(carry % 10);
                p = p->next;
            }

            // deal with carry
            carry = carry / 10;

        }

        return res;
    }
};