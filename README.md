# Email-classifier

This project is an email spam classifier. It trains several models, each with 4 different amounts of training data, to determine the best ML algorithm for our use case at those 4 varying dataset sizes. The dataset can be found in https://www.kaggle.com/datasets/meruvulikith/190k-spam-ham-email-dataset-for-classification.

The spam_filter_training.ipynb file contains the code that we used to train and save our models.

The demo folder includes the code for the frontend of our working demo. Enter the "start demo.html" command to run it.

The models_prediction file contains the code for the backend of our working demo and pickle some of our trained model files. We weren't able to put all our trained models in this repository due to the file size limitations of Github. For the rest of the models, they can be downloaded from https://drive.google.com/drive/folders/1nlG7z9wiUChDQxYhAab6uzrojPIzScDw?. To start this program, run "flask --app main.py run"
