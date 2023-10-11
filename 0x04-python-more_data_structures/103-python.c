#include <Python.h>

/**
 * print_python_list - prints info about Python lists
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	if (p && PyList_Check(p))
	{
		Py_ssize_t size = ((PyVarObject *)p)->ob_size;
		PyObject *element = NULL;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (Py_ssize_t i = 0; i < size; i++)
		{
			element = ((PyListObject *)p)->ob_item[i];
			printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "[*] Python list info\n");
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - prints info about Python bytes objects
 * @p: Python object
 */
void print_python_bytes(PyObject *p)
{
	if (p && PyBytes_Check(p))
	{
		Py_ssize_t size = ((PyVarObject *)p)->ob_size;
		Py_ssize_t max_display = size > 10 ? 10 : size;
		char *bytes = ((PyBytesObject *)p)->ob_sval;

		printf("[.] bytes object info\n");
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", bytes);
		printf("  first %ld bytes: ", max_display);

		for (Py_ssize_t i = 0; i < max_display; i++)
		{
			printf("%02hhx", bytes[i]);
			if (i < max_display - 1)
				printf(" ");
		}
		printf("\n");
	}
	else
	{
		fprintf(stderr, "[.] bytes object info\n");
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
	}
}
