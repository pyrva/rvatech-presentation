import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

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
    packages=setuptools.find_packages("src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
