#include <Python.h>

void print_python_list(PyObject *p) {
    // Check if p is a valid PyListObject
    if (!PyList_Check(p)) {
        printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    // Extract information from the PyListObject and print it
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, allocated);
    
    // Loop through each element of the list
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);
        // Print information about each element based on its type
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        } else if (PyFloat_Check(item)) {
            print_python_float(item);
        } else if (PyList_Check(item)) {
            print_python_list(item);
        } else {
            printf("%s\n", Py_TYPE(item)->tp_name);
        }
    }
}

void print_python_bytes(PyObject *p) {
    // Check if p is a valid PyBytesObject
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    // Extract information from the PyBytesObject and print it
    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n  size: %ld\n", size);
    
    // Print the first 10 bytes of the bytes object
    printf("  first %ld bytes: ", size > 10 ? 10 : size);
    unsigned char *bytes = (unsigned char *)PyBytes_AsString(p);
    for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++) {
        printf("%02x ", bytes[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    // Check if p is a valid PyFloatObject
    if (!PyFloat_Check(p)) {
        printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    // Extract information from the PyFloatObject and print it
    double value = PyFloat_AsDouble(p);
    printf("[.] float object info\n  value: %lf\n", value);
}
