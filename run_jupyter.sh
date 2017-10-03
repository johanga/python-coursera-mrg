#!/bin/bash

JUPYTER2=/cygdrive/c/Anaconda2/Scripts/jupyter.exe
JUPYTER3=/cygdrive/c/Anaconda3/Scripts/jupyter.exe

if [ -f "$JUPYTER2" ]; then
  $JUPYTER2 notebook
elif [ -f "$JUPYTER3" ]; then
  $JUPYTER3 notebook
else
  echo "Jupyter not found."
fi
