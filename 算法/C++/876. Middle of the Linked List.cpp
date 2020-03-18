/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
  public:
    ListNode *middleNode(ListNode *head)
    {
        ListNode *p = head;
        int count = 0;
        while (p != NULL)
        {
            count++;
            p = p->next;
        }
        int middle = count / 2 + 1;
        p = head;
        count = 0;
        ListNode *ans;
        while (p != NULL)
        {
            count++;
            if (count == middle)
            {
                ans = p;
                break;
            }
            p = p->next;
        }
        return ans;
    }
};