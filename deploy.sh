if [ -d "dist" ]; then
  rm -r dist
fi

if [ -d "build" ]; then
  rm -r build
fi

if [ -d ".conda" ]; then
  rm -r .conda
fi

rm -r *.egg-info

conda create -p .conda 
conda activate .conda

python setup.py sdist
python setup.py bdist_wheel