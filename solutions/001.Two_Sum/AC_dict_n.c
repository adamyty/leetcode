#include <stdio.h>
#include <stdlib.h>

#define HASHSIZE 101

struct nlist {
	struct nlist* next;
	int value;
	int index;
};

struct nlist* hashtable[HASHSIZE];

#if 1
int insert(struct nlist** head, int value, int index) {

	struct nlist* node = malloc(sizeof(struct nlist));
	struct nlist* current = *head;

	if ( node == NULL) {
		printf("alloc memory for new node fail\n");
		return 0;
	}
	node->value = value;
	node->index = index;
	node->next = NULL;

	if( *head == NULL) {
		printf("first node\n");
		*head = node;
		return 0;
	} else {
		printf("head is not null\n");
	}


	while( current->next != NULL)
		current = current->next;

	current->next = node;

	return 0;
}
#endif
int dump(struct nlist* head) {

	struct nlist* current = head;
	if( current == NULL )
		printf("List is null \n");

	while( current != NULL ) {
		printf("%d ",current->value);
		current = current->next;
	}

	printf("\n");
	return 0;

}

unsigned int hash(int num){

	unsigned int ret = 0;

	if( num < 0 )
		num = -num;

	ret = num % HASHSIZE;
	return ret;

}
/**
 * Return : -1 means not in hash otherwise index
 */
int lookup(int value) {

	struct nlist* current = hashtable[hash(value)];
	while( current !=NULL ){
		if( current->value == value )
			return current->index;

		current = current->next;
	}

	return -1;
}
void freeHash(struct nlist** hashtable) {
	int i = 0;
	struct nlist* current = NULL;
	struct nlist* next = NULL;
	
	for(i=0;i<HASHSIZE;i++) {
		if(hashtable[i] != NULL) {
			printf("hashtable[%d] is not NULL\n", i);
			/**
			 * on leetcode, it might has problem to free **hashtable
			 * if you want to pass leetcode judgement, do not free node in freeHash()
			 * just set hashtable[i] = NULL;
			 */
			current = hashtable[i];
			while(current != NULL) {
				next = current->next;
				free(current);
				current = next;
			}
		}
	}
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {

	int* ret = malloc(2*sizeof(int));
	int i = 0;
	unsigned int inhash = 0;
	
	freeHash(hashtable);
	
	for(i=0;i<numsSize;i++) {
		inhash = lookup(target - nums[i]);
		if( inhash != -1 ){
			ret[0] = inhash;
			ret[1] = i;
			printf("ans : {%d, %d}\n", ret[0], ret[1]);
			return ret;
		} else {
			insert(&hashtable[hash(nums[i])], nums[i], i);
		}

	}
	return NULL;

}


int main(int argc, char* argv[]) {

	#define NUMSSIZE 3	
	int numsSize = 3;
	int target = 6;
	int nums[NUMSSIZE] = {3, 2, 3};
	int i = 0;

	int* p = NULL;

	printf("nums : [ ");
	for(i=0;i<NUMSSIZE;i++)
		printf("%d ", nums[i]);
	printf("] target : %d\n", target);
	p = twoSum(nums, numsSize, target);
	printf("main() ans: {%d,%d}\n",p[0], p[1]);



	
#if 1

	/*for(i=0;i<numsSize;i++) {
		insert(&hashtable[hash(nums[i])], nums[i], i);
		//insert(&head, num[i], i);
	}*/
/*
	for(i=0;i<HASHSIZE;i++){
		if( hashtable[i] == NULL) {
			//printf("hashtable[%d] is NULL\n", i);
		} else {
			printf("hashtable[%d] : ", i);
			dump(hashtable[i]);
		}
	}
	
	freeHash(hashtable);
*/


#endif


	return 0;
}

