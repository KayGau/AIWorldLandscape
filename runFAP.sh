lang=('py' 'ipynb')
module=(tensorflow torch keras caffe mxnet cntk theano chainer spacy)
for la in ${lang[@]}
do
    for mod in ${module[@]}
    do
        echo $la $mod
        python -u findAIProjects.py $la $mod >> $la$mod.txt
    done
done
