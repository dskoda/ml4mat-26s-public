#!/bin/bash

mkdir -p data

TARGET=data/neu-surface-defect-database.zip
if [[ ! -e $TARGET ]]
then
    curl -L -o $TARGET\
      https://www.kaggle.com/api/v1/datasets/download/kaustubhdikshit/neu-surface-defect-database
fi

unzip -q $TARGET
