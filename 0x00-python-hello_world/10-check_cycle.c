#include "lists.h"
/**
 * check_cycle - cghecks for a cycle in a listint_t list
 * @list: pointer to head of list
 * Return: 0 if theres no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *head;
	/*check for NULL list*/
	if (list == NULL)
		return (0);
	/*outer loop to traverse list*/
	current = list;
	while (current != NULL)
	{
		/*second loop to traverse*/
		/*starting from current node till end of list*/
		/*if any node matches current node=>cycle!*/
		if (current->next != NULL)
			head = current->next;
		else
			head = NULL;
		while (head != NULL)
		{
			if (head == current)
				return (1);
			if (head->next != NULL)
				head = head->next;
			else
				head = NULL;
		}
		if (current->next != NULL)
			current = current->next;
		else
			current = NULL;
	}
	return (0);
}
