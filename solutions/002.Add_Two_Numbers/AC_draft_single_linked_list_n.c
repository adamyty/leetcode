#include <stdio.h>
#include <stdlib.h>

struct ListNode {
	struct ListNode* next;
	int val;
};

int insert(struct ListNode** head, int val){
	//struct ListNode Node;
	struct ListNode* pNode = malloc(sizeof(struct ListNode));
	struct ListNode* current = *head;
	if(pNode == NULL)
		return -1;
	pNode->val = val;
	pNode->next = NULL;

#if 1
	if(*head == NULL) {
		printf("first node\n");
		*head = pNode;
		return 0;
	}

    while(current->next != NULL)
        current = current->next;

    current->next = pNode;


//These will change list point address
/*    while((*head)->next != NULL){
		printf("insert1() (*head) : 0x%08X\n", (*head));
        (*head) = (*head)->next;
		printf("insert2() (*head) : 0x%08X\n", (*head));
	}

    (*head)->next = pNode;
*/

#endif

#if 0
    if((current) == NULL) {
        (current) = pNode;
        return 0;
    }


	while(current->next != NULL)
		current = current->next;

	current->next = pNode;
#endif
	return 0;

}
int dump(struct ListNode* head) {

	if(head == NULL) {
		printf("NULL list\n");
		return -1;
	}
	while(head!=NULL) {
		printf("%u -> ",head->val);
		head = head->next;
	}
	printf("NULL\n");
	
	return 0;

}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

	struct ListNode* c1 = l1;
	struct ListNode* c2 = l2;
	struct ListNode* ans = NULL;
	int sum = 0;
	int carrier = 0;

	while(c1 != NULL || c2 != NULL || carrier != 0) {
		if(c1 != NULL) {
			sum += c1->val;
			c1 = c1->next;
		}
        if(c2 != NULL) {
            sum += c2->val;
            c2 = c2->next;
        }
		sum += carrier;
		carrier = 0;

		carrier = sum/10;
		sum = sum%10;
		insert(&ans, sum);
		sum = 0;
	}
	return ans;
    
}

int main(int argc, char* argv[]) {

	int nums1[] = {2, 4, 3};
	int nums2[] = {5, 6, 4};
	struct ListNode* l1 = NULL;
	struct ListNode* l2 = NULL;
	struct ListNode* ans = NULL;
	int i = 0;
	//make l1
	for(i=0;i<(sizeof(nums1)/sizeof(int));i++){
		insert(&l1, nums1[i]);
		if(l1 != NULL)
			printf("l1 : 0x%08X\n",l1);
	}

	//make l2
    for(i=0;i<(sizeof(nums2)/sizeof(int));i++){
        insert(&l2, nums2[i]);
    }
	ans = addTwoNumbers(l1, l2);
	dump(l1);
	dump(l2);
	dump(ans);

	return 0;
}
