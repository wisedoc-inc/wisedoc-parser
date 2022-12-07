import setuptools


dependencies = [
    "numpy",
    "pandas",
    "nltk",
    "spacy",
    "jellyfish",
    "ipython"
]

setuptools.setup(
    name="Wisedoc",
    version="1.0.0",
    author="Vamshi Bachaneboina",
    author_email="vamshi.bachaneboina@wisedoc.net",
    description="An NLP module to automatically Extract skills and certifications from unstructured job postings, texts, and applicant's resumes",
    url="https://github.com/wisedoc-inc/wisedoc-parser",
    keywords=["wisedoc", 'python', 'NLP', "NER",
              "skills-extraction", "job-description"],
    download_url='',
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
)
