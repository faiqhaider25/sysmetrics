from setuptools import setup, find_packages

setup(
    name="syspulse",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "psutil>=5.8.0",
        "prometheus-client>=0.11.0",
        "python-multipart>=0.0.5",
        "jinja2>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "syspulse=syspulse.cli:main",
        ],
    },
    author="Shameer Awais",
    author_email="your.email@example.com",
    description="A system monitoring tool for Windows, macOS, and Linux",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ShameerAwais/SysPulse",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
) 