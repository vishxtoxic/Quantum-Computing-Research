from matplotlib importpyplot as plt 
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram as plh

qc = QuantumCircuit(3)
qc.h(0)
qc.cx(1,2)
qc.x(1)
qc.measure_all()

sampler = StatevectorSampler()

result = sampler.run([qc], shots=1024).result()
count = result[0].data.meas.get_counts()

plh(count)
plt.show()

# Wrote a basic quantum Circuit and experimented  with ploltting on histogram to compare.
