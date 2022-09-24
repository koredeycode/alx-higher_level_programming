#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: an integer, 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *tmp;
	int len = 0, iterator, i;

	tmp = *head;
	if (tmp == NULL)
		return (1);
	while (tmp != NULL)
	{
		len += 1;
		tmp = tmp->next;
	}
	if (len == 1)
		return (1);
	iterator = len - 1;
	current = *head;
	while (iterator >= 1)
	{
		tmp = current;
		for (i = 0; i < iterator; i++)
		{
			tmp = tmp->next;
		}
		if (current->n != tmp->n)
			return (0);
		current = current->next;
		iterator -= 2;
	}
	return (1);
}
