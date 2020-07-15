import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notifyml", # Replace with your own username
    version="0.0.1",
    author="Iveno Carolus",
    author_email="bubblesortguru@gmail.com",
    description="Notification app for personal machine learning projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IvenoCarolus/NotifyML",
    packages=setuptools.find_packages(),
    install_requires=['twilio'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)