import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sentiment-analysis-spanish",
    version="0.0.1",
    author="Hugo J. Bello",
    author_email="hjbello.wk@gmail.com",
    description="Sentiment analysis for sentences in spanish",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sentiment-analysis-spanish/sentiment-spanish",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)