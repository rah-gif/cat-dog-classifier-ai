# 🐱🐶 Cat vs Dog Classifier AI

A deep learning project built with **TensorFlow/Keras** to classify images of cats and dogs.  
This model achieves ~76% validation accuracy after 15 epochs.

---

## 📊 Training Results
- Training Accuracy: ~100%
- Validation Accuracy: ~76%
- The model shows overfitting → perfect on training, moderate on validation.

---

## 🚀 Features
- name classification (Cat / Dog)
- TensorFlow/Keras-based CNN model
- Saved trained model as `cat_dog_model.h5`

-------------------------------------------------------

## 📂 Project Structure
cat-dog-classifier-ai/
│
├── model.py 
├── cat_dog_model.h5 
├── requirements.txt 
├── README.md
├── prepare_data.py  
├── predict.py 
└── data/ # (Optional) dataset instructions

------------------------------------------------------



📦 Requirements

Note: " you must create a preject directory(project folder : inside your computor) before doing these implementations. All of this files should inside that project directory, open CMD from that folder only to execute necessary instructions such as run the model and installing the eaxh requirements! "




- Python 3.10 or higher
- TensorFlow / Keras
- NumPy
- opencv-python


📂 Setup & Usage

1. Clone the repo:
   git clone https://github.com/rah-gif/cat-dog-classifier-ai.git
   cd cat-dog-classifier-ai

2. Install dependencies:
   pip install -r requirements.txt

3. Download the trained model:
   [Download cat_dog_model.h5 from Google Drive](https://drive.google.com/file/d/1lMChe9-zfbpSqaAy5LkxTV6C50ut7-0E/view?usp=sharing)
   Note* Place it in the project root if downloaded manually.



📦 Download Trained Model Automatically

NOTE: The model will be downloaded automatically if you add this part top of predict.py. It will dowload automatically when you run the model. you won't need manually doelaod it from Google drive unless you dont need it.

----------------------------------------------------------------------------------------------
import os
import gdown

# Automatically download model if not present
if not os.path.exists("cat_dog_model.h5"):
    url = "https://drive.google.com/uc?export=download&id=1lMChe9-zfbpSqaAy5LkxTV6C50ut7-0E"
    gdown.download(url, "cat_dog_model.h5", quiet=False)
    
---------------------------------------------------------------------------------------------


4. Run predictions:
   python predict.py

5. (Optional) Train the model:
   python model.py
   → Requires dataset in 'data/' folder
   → Trained model will be saved as cat_dog_model.h5

6. you can run the model by typing:

      (python predict.py)



      
NOTE: if you want to check using diffent images to predict accuracy, you can simply add a {.jpg}  (MUST be in dataset folder, outside images will cause occuring errors) image to predict.py bottom line.  And see whether it is possibly working accurately!



✨ Credits

Developed by Chethana Rahul.

