import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="resizeanyfile",
    version="0.0.2",
    author="Sai Hemanth",
    author_email="saihemanth9019@gmail.com",
    description="Command line tool to resize any file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shb9019/resize-any-file",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        resizeanyfile=main:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
