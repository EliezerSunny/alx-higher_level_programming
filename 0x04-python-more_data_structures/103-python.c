#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p) {
    Py_ssize_t size, allocated, i;
    const char *type;

    printf("[*] Python list info\n");
    
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)(p))->ob_size;
    allocated = ((PyListObject *)(p))->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++) {
        type = (PyList_GetItem(p, i))->ob_type->tp_name;
        printf("Element %zd: %s\n", i, type);
        
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(PyList_GetItem(p, i));
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);
    printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
    
    for (i = 0; i < size + 1 && i < 10; i++)
        printf(" %02x", (unsigned char) string[i]);
    
    printf("\n");
}
