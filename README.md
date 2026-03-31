# Machine Learning for Materials Science - MAT SCI 298 - UCLA, Winter 2025

## Overview

This repository contains Jupyter notebooks for the lecture notes of MAT SCI 298, a course in Machine Learning for Materials Science at UCLA (Winter 2025).
The course covers various machine learning techniques and their applications in the field of materials science.

## Contents

- Lecture Notes: Jupyter notebooks for each lecture.
- Datasets: a few datasets that will be used throughout the lectures.

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

## Notice

The code is not public yet - this repository is for use of MAT SCI 298 students only.
Distribution of the data or code is prohibited until the repository is made public.
