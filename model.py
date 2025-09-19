from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from prepare_data import prepare_dataset

x,y= prepare_dataset()

model=Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')  # sigmoid used for Binary classification you remeber that huh? 
])


#complie the model now!
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#train the model right now!
model.fit(x, y, epochs=15, batch_size=32, validation_split=0.2)

# Save the model
model.save('cat_dog_classifier.h5')
print("✅ Model saved as cat_dog_model.h5")