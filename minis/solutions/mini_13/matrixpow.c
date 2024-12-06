#define PY_SSIZE_T_CLEAN
#include <Python.h>

void* pyobj_to_arr(PyObject* matrix, size_t size) {
    double* res = calloc(size * size, sizeof(double));
    for (size_t i = 0; i < size; i++) {
        PyObject* row = PyList_GetItem(matrix, i);
        for (size_t j = 0; j < size; j++) {
            PyObject* elem = PyList_GetItem(row, j);
            res[i * size + j] = PyFloat_AsDouble(elem);
        }
    }
    return res;
}

void* arr_to_pyobj(double* matrix, size_t size){
    PyObject* res = PyList_New(size);
    for (size_t i = 0; i < size; i++) {
        PyObject* row = PyList_New(size);
        for (size_t j = 0; j < size; j++) {
            double elem = matrix[i * size + j];
            PyList_SetItem(row, j, PyFloat_FromDouble(elem));
        }
        PyList_SetItem(res, i, row);
    }
    return res;
}

void* matrix_multiply(size_t n, double* A, double* B) {
    double* res = calloc(n * n, sizeof(double));
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            for (size_t k = 0; k < n; k++) {
                res[i * n + j] += A[i * n + k] * B[k * n + j];
            }
        }
    }
    return res;
}

static PyObject *matrix_pow(PyObject *self, PyObject *args)
{
	PyObject *py_matrix;
	size_t power;
	if (!PyArg_ParseTuple(args, "On", &py_matrix, &power))
		return NULL;
    size_t size = PyObject_Length(py_matrix);

    double* matrix = pyobj_to_arr(py_matrix, size);
    double* result = calloc(size * size, sizeof(double));
    memcpy(result, matrix, size * size * sizeof(double));
    for (size_t i = 1; i < power; i++) {
        result = matrix_multiply(size, result, matrix);
    }

    PyObject* py_result = arr_to_pyobj(result, size);
    free(matrix);
    free(result);

    return py_result;
}

static PyMethodDef ForeignMethods[] = {
	{"matrix_pow",
	matrix_pow, METH_VARARGS,
	"pow matrix"
	},
	{NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef foreignmodule = {
	PyModuleDef_HEAD_INIT,
	"matrixpow", /* name of module */
	NULL, /* module documentation, may be NULL */
	-1, /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
	ForeignMethods
};

PyMODINIT_FUNC PyInit_matrixpow(void) {
	return PyModule_Create(&foreignmodule);
}