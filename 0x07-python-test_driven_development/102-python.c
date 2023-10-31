/*
 * Module to print Python strings
 */

#include <Python.h>

/*
 * print_python_string(p)
 *
 * Print a Python string.
 *
 * Parameters:
 *   p (str): The Python string to print.
 *
 * Returns:
 *   None
 *
 * Raises:
 *   TypeError: If p is not a valid Python string.
 *   RuntimeError: If decoding the string fails.
 */
static PyObject *print_python_string(PyObject *self, PyObject *args)
{
    PyObject *p;

    if (!PyArg_ParseTuple(args, "O", &p))
    {
        return NULL;
    }

    if (PyUnicode_Check(p))
    {
        const char *str = PyUnicode_AsUTF8(p);
        if (str)
        {
            printf("Python string: %s\n", str);
        }
        else
        {
            PyErr_SetString(PyExc_RuntimeError, "Failed to decode Python string");
            return NULL;
        }
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "Not a valid Python string");
        return NULL;
    }

    Py_RETURN_NONE;
}

static PyMethodDef PythonMethods[] = {
    {"print_python_string", print_python_string, METH_VARARGS, "Print a Python string"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pythonmodule = {
    PyModuleDef_HEAD_INIT,
    "pythonmodule",
    NULL,
    -1,
    PythonMethods
};

PyMODINIT_FUNC PyInit_pythonmodule(void)
{
    return PyModule_Create(&pythonmodule);
}
