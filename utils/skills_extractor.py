SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "git",
    "github",
    "docker",
    "flask",
    "streamlit",
    "mysql"
]


def extract_skills(text):
    text=text.lower()
    present_skills=[]
    for skill in SKILLS:
        if skill in text:
            present_skills.append(skill)
    return present_skills

