#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked list of integers.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current_node = *head, *next_node, *previous_node = NULL;

	while (current_node)
	{
		next_node = current_node->next;
		current_node->next = previous_node;
		previous_node = current_node;
		current_node = next_node;
	}

	*head = previous_node;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list of integers is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reversed, *middle;
	size_t list_size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		list_size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (list_size / 2); i++)
		temp = temp->next;

	if ((list_size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reversed = reverse_listint(&temp);
	middle = reversed;

	temp = *head;
	while (reversed)
	{
		if (temp->n != reversed->n)
			return (0);
		temp = temp->next;
		reversed = reversed->next;
	}
	reverse_listint(&middle);

	return (1);
}
