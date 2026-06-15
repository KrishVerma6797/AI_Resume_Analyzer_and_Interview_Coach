QUESTIONS = {

    "python": [
        "What is a decorator in Python?",
        "Difference between list and tuple?",
        "What are *args and **kwargs?"
    ],

    "java": [
        "Difference between JDK, JRE, and JVM?",
        "What is method overloading and method overriding?",
        "What is the difference between an interface and an abstract class?"
    ],

    "sql": [
        "Difference between WHERE and HAVING?",
        "What is a JOIN? Explain different types of JOINs.",
        "What is the difference between DELETE, DROP, and TRUNCATE?"
    ],

    "machine learning": [
        "What is overfitting?",
        "Explain Bias vs Variance.",
        "What is the difference between supervised and unsupervised learning?"
    ],

    "deep learning": [
        "What is a neural network?",
        "What is the purpose of an activation function?",
        "What is the difference between Deep Learning and Machine Learning?"
    ],

    "nlp": [
        "What is tokenization?",
        "What is stemming and lemmatization?",
        "What are word embeddings?"
    ],

    "pandas": [
        "What is a DataFrame in Pandas?",
        "Difference between loc[] and iloc[]?",
        "How do you handle missing values in Pandas?"
    ],

    "numpy": [
        "What is a NumPy array?",
        "Difference between a Python list and a NumPy array?",
        "What is broadcasting in NumPy?"
    ],

    "docker": [
        "What is Docker?",
        "What is the difference between a Docker Image and a Docker Container?",
        "Why is containerization useful?"
    ],

    "git": [
        "What is Git?",
        "Difference between git pull and git fetch?",
        "What is the purpose of git merge?"
    ],

    "github": [
        "What is GitHub?",
        "Difference between Git and GitHub?",
        "What is a Pull Request?"
    ],

    "tensorflow": [
        "What is TensorFlow used for?",
        "Explain tensors in TensorFlow.",
        "What is the role of Keras in TensorFlow?"
    ],

    "pytorch": [
        "What is autograd in PyTorch?",
        "What is the difference between PyTorch and TensorFlow?",
        "What is a tensor in PyTorch?"
    ],

    "scikit-learn": [
        "What is Scikit-learn used for?",
        "What is the train_test_split() function?",
        "What is cross-validation?"
    ],

    "mysql": [
        "What is MySQL?",
        "What is a primary key?",
        "Difference between primary key and foreign key?"
    ]
}

def get_ques(skills):
    ques=[]
    for s in skills:
        if s in QUESTIONS:
            ques.extend(QUESTIONS[s])
    return ques