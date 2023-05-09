#include "lists.h"

/**
 * insert_node - add node in a sorted linked list
 * @head: the linked list.
 * @number: the data to be added.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur;
	listint_t *new;


	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	cur = *head;
	if (new->n <= cur->n)
	{
		new->next = cur;
		*head = new;
		return *head;
	}
	else
	{
		while(cur != NULL)
		{
			if (new->n <= cur->n)
			{
				new->next = cur->next;
				cur->next = new;
				break;
			}
			if (cur->next == NULL)
			{
				cur->next = new;
				break;
			}
			cur = cur->next;
		}
	}
	return *head;
}
