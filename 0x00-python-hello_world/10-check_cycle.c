#include "lists.h"
/**
 * check_cycle - checks linked list for a loop
 * @list: head of linked list
 * Return: 0 if no loop, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *step = list, *jump = list;


	while (jump && jump->next)
	{
		step = step->next;
		jump = (jump->next)->next;
		if (step == jump)
			return (1);
	}
	return (0);
}
