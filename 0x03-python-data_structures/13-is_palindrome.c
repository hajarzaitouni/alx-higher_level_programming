#include "lists.h"

#include <stdio.h>
#include <stdlib.h>

listint_t *reverse_listint(listint_t *head);
/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 *
 * @head: the head of the linked list
 * Return: 1 if it is a palindrome and 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *ptr1, *ptr2, *sec_half;

	if (*head == NULL)
		return (1);

	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	sec_half = reverse_listint(slow->next);

	ptr1 = *head;
	ptr2 = sec_half;

	while (ptr2)
	{
		if (ptr1->n != ptr2->n)
			return (0);
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}

	return (1);
}

listint_t *reverse_listint(listint_t *head)
{
	listint_t *current, *prev, *next;

	current = next = head;
	prev = NULL;

	while (next != NULL)
	{
		next = next->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
