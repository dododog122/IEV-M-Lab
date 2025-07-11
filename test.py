import tensorflow as tf
# List all physical devices
gpus = tf.config.list_physical_devices('GPU')
print("Num GPUs Available: ", len(gpus))
