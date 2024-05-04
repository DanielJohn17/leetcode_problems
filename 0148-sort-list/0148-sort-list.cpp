/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* merge(ListNode* left, ListNode* right){
        if (left == nullptr)
            return right;
        if (right == nullptr)
            return left;
        
        ListNode* sort;

        if(left->val < right->val)
        {
            sort = left;
            sort->next = merge(left->next, right);
        }
        else
        {
            sort = right;
            sort->next = merge(left, right->next);
        }
        return sort;
    }

    ListNode* midPoint(ListNode* head){
        ListNode* slow = head;
        ListNode* fast = head->next;

        while(fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow;
    }

    ListNode* sortList(ListNode* head) {
        if (head == nullptr || head->next == nullptr)
            return head;
        
        ListNode* mid = midPoint(head);
        ListNode* left = head;
        ListNode* right = mid->next;
        mid->next = nullptr;

        left = sortList(left);
        right = sortList(right);

        return merge(left, right);
    }
};