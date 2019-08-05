# extract uniq project names from data obtained from runFAP.sh
lang=('py' 'ipynb')
module=(tensorflow torch keras caffe mxnet cntk theano chainer spacy)
for la in ${lang[@]}
do
    for mod in ${module[@]}
    do
        echo $la $mod
        p='Project'
        suffix1='.txt'
        cat $la$mod$suffix1 | awk -F ';' '{print $2}' | sort | uniq > $la$mod$p$suffix1
    done
done
