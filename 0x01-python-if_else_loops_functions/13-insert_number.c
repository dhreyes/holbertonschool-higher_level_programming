#include "lists.h"
/**
 * insert_node - insert node at specified number
 * @head: head of linked list
 * @number: number to be inserted
 * Return: Address of new node, else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *iterator, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	iterator = *head;
	if (iterator == NULL || iterator->n >= number)
	{
		new->next = iterator;
		*head = new;
		return (new);
	}

	while (iterator && iterator->next && iterator->next->n < number)
		iterator = iterator->next;

	new->next = iterator->next;
	iterator->next = new;
	return (new);
}
