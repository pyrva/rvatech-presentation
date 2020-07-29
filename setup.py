import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

dev_req = []

test_req = [
    "pytest>=5.4.3",
]

setuptools.setup(
    name="pyrva_talk",
    version="0.0.1",
    author="PyRVA",
    author_email="author@example.com",
    description="Code used for a PyRVA talk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pyrva/rvatech-2020-07-21/tree/twitter_data",
    package_dir={"": "src"},
    install_requires=[
        "python-dotenv>=0.13.0",
        "streamlit>=0.61.0",
        "tweepy>=3.8.0",
        "matplotlib>=3.3.0",
    ],
    extras_require={"dev": test_req + dev_req, "test": test_req,},
    packages=setuptools.find_packages("src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
