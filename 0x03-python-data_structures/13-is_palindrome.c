#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: linked list to be checked.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *tmp1 = *head;
	int len = 0, i = 0;
	int *tab;

	if (*head == NULL)
		return (1);

	while (tmp != NULL)
	{
		len++;
		tmp = tmp->next;
	}
	tab = malloc(sizeof(int) * len);
	while (tmp1 != NULL)
	{
		tab[i] = tmp1->n;
		tmp1 = tmp1->next;
		i++;
	}
	for (i = 0; i < len / 2; i++)
	{
		if (tab[i] != tab[len - i - 1])
		{
			free(tab);
			return (0);
		}
	}
	free(tab);
	return (1);
}
