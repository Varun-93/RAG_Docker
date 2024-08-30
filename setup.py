from setuptools import find_packages, setup

setup(
    name="qasystem",
    version="0.0.1",
    author="varun",
    author_email="bhatiavarun2007@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","pypdf","streamlit","faiss-cpu","boto3","python-dotenv","langchain-community"])