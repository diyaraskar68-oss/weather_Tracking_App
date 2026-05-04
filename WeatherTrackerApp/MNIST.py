import os
import numpy as np
import tensorflow as tf # fix env issue


def load_mnist():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    x_train = (x_train.astype(np.float32) / 255.0)[..., None]  # (N, 28, 28, 1)
    x_test = (x_test.astype(np.float32) / 255.0)[..., None]
    return (x_train, y_train), (x_test, y_test)


def build_model():
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(28, 28, 1)),
            tf.keras.layers.Conv2D(32, 3, activation="relu"),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Conv2D(64, 3, activation="relu"),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )


def main():
    epochs = int(os.environ.get("EPOCHS", "5"))
    batch_size = int(os.environ.get("BATCH_SIZE", "128"))
    model_path = os.environ.get("MODEL_PATH", "mnistmodels.keras")

    (x_train, y_train), (x_test, y_test) = load_mnist()

    # 10% of training set for validation
    val_size = int(0.1 * x_train.shape[0])
    x_val, y_val = x_train[:val_size], y_train[:val_size]
    x_tr, y_tr = x_train[val_size:], y_train[val_size:]

    model = build_model()
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    model.fit(
        x_tr,
        y_tr,
        validation_data=(x_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        verbose=2,
    )

    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
    print(f"Test loss: {test_loss:.2f}. Test accuracy: {test_accuracy * 100:.2f}%")

    model.save(model_path)
    print(f"Saved model to: {model_path}")


if __name__ == "__main__":
    main()