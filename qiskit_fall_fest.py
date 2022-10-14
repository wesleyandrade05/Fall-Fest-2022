import numpy as np
from qiskit import *

# Get the istring input from the user
string = input("String: ")

# Create a quantum circuit capable of measuring as many qubits as indicated by the user
qc = QuantumCircuit(len(string), len(string))

for i in range(len(string)):
    # If the qubit needs to be in state |1>, performs a not operation, then invert its phase with z-gate, 
    # measure it, and perform another z-gate to return to the previous phase
    if string[i] == "1":
        qc.x(i)
        qc.z(i)
        qc.measure(i, i)
        qc.z(i)
    # Otherwise, just measure it
    else:
        qc.measure(i, i)

qc.draw('mpl')
