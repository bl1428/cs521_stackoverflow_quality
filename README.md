# cs521_stackoverflow_quality
Prediction of closed questions on Stack Overflow

UIC CS 521, Spring 2021

--------
## Artifacts

### Code
The main code deliverables in this repo are:
- Scripts for retrieving and saving data in the `/data_utils` folder
- `StackClassifier.ipynb`: Notebook for experiments with different text features
- `Resampling_imbalanced_data.ipynb`: Notebook for experiments with resampling techniques and different classifiers
- `Generate_Bert_Embeddings.ipynb`: Code for generating BERT embeddings

Any other scripts and Jupyter notebooks contain exploratory and experimental code, the useful parts of which have been incorporated into the deliverables above.

### Data
Code for retrieving the data used in this project is included. For convenience, this [Google Drive link](https://drive.google.com/file/d/1aHecoSZiZMc2iN5dTp12VWuXjeDIXNX_/view?usp=sharing) contains the full corpus of ~147,000 questions in CSV format.



### Results

------
## Software Dependencies
To run the Jupyter notebooks, install the following dependencies:
- Python 3
    - Additional library dependencies as listed in the `import` section at the start of each Jupyter notebook
- TensorFlow 2.4.1
- Optional: CUDA 11.0 for running local GPU environment
