import numpy


def sigmoid(x):
    return 1 / (1 + numpy.exp(-x))


train_inputs = numpy.array([[0, 0, 1],
                         [1, 1, 1],
                         [1, 0, 1],
                         [0, 1, 1]])

train_outputs = numpy.array([[0, 1, 1, 0]]).T

numpy.random.seed(1)

synaptic_weights = 2 * numpy.random.random((3, 1)) - 1
outputs = []

for i in range(100):
    input_layer = train_inputs
    outputs = sigmoid(numpy.dot(input_layer, synaptic_weights))

    err = train_outputs - outputs
    adjustment = numpy.dot(input_layer.T, err * (outputs * (1 - outputs)))

    synaptic_weights += adjustment

print("Веса:\n" + str(synaptic_weights))
print("Веса:\n" + str(outputs))
print("Результат:\n" +
      str(round(float( outputs[0] ))) +
      str(round(float( outputs[1] ))) +
      str(round(float( outputs[2] ))) +
      str(round(float( outputs[3] ))))
