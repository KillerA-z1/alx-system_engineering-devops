#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop to make the program hang
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: always 0
 */
int main(void)
{
	int i = 0;
	pid_t ZOMBIE_PID;

	while (i < 5)
	{
		ZOMBIE_PID = fork();
		if (!ZOMBIE_PID)
			return (0);
		printf("Zombie process created, PID: %d\n", ZOMBIE_PID);
	i++;
	}

	infinite_while();
	return (0);
}
