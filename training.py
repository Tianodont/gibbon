
import numpy
import tensorflow as tf

a = []
b = []
lictus = ["I", "Eat", "Bread", "Water", "Drink"]

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(2520, 1)),
  tf.keras.layers.Dense(2520, activation='relu'),
  tf.keras.layers.Dense(2520, activation='relu'),
    tf.keras.layers.Dense(2520, activation='relu'),
  tf.keras.layers.Dense(5),
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

for i in range(5):
    with open(f"{lictus[0]}.txt", 'r') as f:
        for rtg in f:
            for line in rtg.replace('"', "").replace("'", "").split("@")[:-1]:
                line = line.split("!")[:-1]
                line = list(map(float, line))
                if line:
                    b.append(i)
                    t = numpy.asarray(line)
                    a.append(t)
b = numpy.asarray(b)
a = numpy.asarray(a)
print(b, a)

from tensorflow import keras
model.fit(
    tf.stack(a),
    tf.stack(b),
    epochs=3,
)
model.save("htf")
