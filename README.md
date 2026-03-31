# Machine Learning for Materials Science - MAT SCI 298 - UCLA, Spring 2026

## Overview

This repository contains Jupyter notebooks for the lecture notes of MAT SCI 298, a course in Machine Learning for Materials Science at UCLA (Spring 2026).
The course covers various machine learning techniques and their applications in the field of materials science.

## Contents

- Lectures: Jupyter notebooks for each lecture, some of which are used as labs
- `ml4mat_ucla`: scripts and helper tools to make usage of the folder easier

## Usage

To get started, clone this repository and open the Jupyter notebooks in your preferred environment.
Ensure you have all the necessary dependencies installed.
If you use Anaconda, you can `cd` to the local repository and install the environment by doing the following:

```bash
conda create -n ml4mat python=3.11
conda activate ml4mat
pip install -e .
```

This will create a new environment called `ml4mat`, install this repository locally, and all the dependencies with it (which are listed under `pyproject.toml`).
Then, to activate the kernel on a Jupyter notebook, you can run the following command:

```bash
python3 -m ipykernel install --user --name ml4mat --display-name "ml4mat"
```

Now, you can see the lectures by opening a Jupyter session:

```bash
jupyter notebook
```

Make sure you select the right kernel under Kernel > Change Kernel > ml4mat once you open the notebook!

### Using in the classroom

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dskoda/ml4mat-26s-public/)

## License

Code in this repository is licensed under the MIT license.
Lecture content (e.g., Jupyter Notebook/slides) is licensed under CC BY-NC 4.0.
Datasets included in this repository are subject to their own licenses as described in DATA_LICENSE.md.
