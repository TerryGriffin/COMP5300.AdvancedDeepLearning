#!/bin/bash
dir=$(realpath $1)

config=$(ls $dir/*.py 2> /dev/null )

eval_type="bbox"
if grep "evaluation = dict.*segm" $config > /dev/null ; then
    eval_type="bbox segm"
fi

eval_file=${dir}/eval_results.pickle
jsonfile_prefix=${dir}/json_results
pushd ~/repos/mmdetection
echo run_test on Processing $dir
#echo python tools/test.py $config $dir/best.pth --eval $eval_type --eval-option "classwise=True" "jsonfile_prefix=$jsonfile_prefix"
time python tools/test.py $config $dir/best.pth --eval $eval_type --out $eval_file --eval-option "classwise=True" "jsonfile_prefix=$jsonfile_prefix" > $dir/test_result.txt
popd

