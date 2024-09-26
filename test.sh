if [ -d ".conda" ]; then
  rm -r .conda
fi

conda create -p .conda 
conda activate .conda

pip install git+https://github.com/djoroya/loadjson.git

cd .. 

python -c "from loadsavejson.loadjson import loadjson"
