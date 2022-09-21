#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head node
 * @number: the number to be inserted
 * Return: the address of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *ins;

	ins = malloc(sizeof(listint_t));
	if (ins == NULL)
		return (NULL);
	ins->n = number;
	ins->next = NULL;
	current = *head;
	if (current == NULL || current->n >= number)
	{
		ins->next = current;
		*head = ins;
		return (ins);
	}
	while (current != NULL && current->next != NULL && current->next->n < number)
		current = current->next;
	ins->next = current->next;
	current->next = ins;
	return (ins);
}
