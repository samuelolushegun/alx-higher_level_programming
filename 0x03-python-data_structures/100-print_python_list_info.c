#include <stdio.h>
#include <stdlib.h>
#include "listobject.h"
#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to a python oblect
 *
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	int taille = PyList_Size(p);

	printf("[*] Size of Python List = %d\n", taille);
	printf("[*] Allocated = %d\n", PyList_GET_SIZE(p));
	if (taille > 0)
	{
		for (i = 0 ; i < taille; i++)
			printf("Element %d: %p\n", Py_TYPE(PyList_GetItem(p, i))
				);
	}
}
