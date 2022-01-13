import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amplefastapi",
    version="0.0.1",
    author="Kelvin Wangonya",
    author_email="kwangonya@gmail.com",
    description="Ample Analytics middleware package for FastApi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wangonya/amplefastapi",
    project_urls={
        "Bug Tracker": "https://github.com/wangonya/amplefastapi/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
