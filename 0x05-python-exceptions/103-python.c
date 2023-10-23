#include <Python.h>

/**
 * print_python_list - Print information about a Python list
 * @p: PyObject pointer to the list
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		int size = PyList_Size(p);
		int allocated = ((PyListObject *)p)->allocated;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", allocated);

		for (int i = 0; i < size; i++)
		{
			printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: PyObject pointer to the bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	int size, i;
	char *raw_data;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	raw_data = bytes->ob_sval;

	printf("[.] bytes object info\n");
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", raw_data);

	printf("  first 10 bytes: ");
	if (size >= 10)
	{
		for (i = 0; i < 10; i++)
		{
			printf("%02x%c", (unsigned char)raw_data[i], i < 9 ? ' ' : '\n');
		}
	}
	else
	{
		for (i = 0; i < size; i++)
		{
			printf("%02x%c", (unsigned char)raw_data[i], i < size - 1 ? ' ' : '\n');
		}
	}
}

/**
 * print_python_float - Print information about a Python float object
 * @p: PyObject pointer to the float object
 */
void print_python_float(PyObject *p)
{
	if (PyFloat_Check(p))
	{
		double value = ((PyFloatObject *)p)->ob_fval;
		char *str_value = PyOS_double_to_string(value, 'r', 0, \
			       Py_DTSF_ADD_DOT_0, NULL);
		size_t str_len = strlen(str_value);

		printf("[.] float object info\n");
		printf("  value: %s\n", str_value);
		PyMem_RawFree(str_value);
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
	}
}
