import numpy as np
import inspect


def extract_numpy_docs():
    """
    Extract selected NumPy function docstrings
    and return them as a list of formatted strings.
    """

    numpy_functions = [
        np.reshape,
        np.mean,
        np.dot,
        np.array,
        np.sum,
        np.std
    ]

    documents = []

    for func in numpy_functions:
        name = func.__name__
        doc = inspect.getdoc(func)

        if doc:
            formatted_text = f"""
Function: {name}

Documentation:
{doc}
"""
            documents.append(formatted_text.strip())

    return documents


# This block runs only if we execute this file directly
if __name__ == "__main__":
    docs = extract_numpy_docs()
    print("Total Documents Extracted:", len(docs))
    print("\nSample Document:\n")
    print(docs[0][:800])