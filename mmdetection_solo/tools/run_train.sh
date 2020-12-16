#!/usr/bin/env bash
CONFIG=$1
GPUS=$2
PORT=${PORT:-29500}

BASE_WORK_DIR=$(python $(dirname $0)/print_config.py ${CONFIG} | grep work_dir | cut -d ' ' -f 3 | tr -d \')
WORK_DIR=$($(dirname "$0")/generate_outdir.py $BASE_WORK_DIR)
echo WORK_DIR: $WORK_DIR

if [ "$GPU" == "1" ]; then
    python $(dirname "$0")/train.py $CONFIG --cfg-options work_dir=${WORK_DIR} ${@:3}
else
    PYTHONPATH="$(dirname $0)/..":$PYTHONPATH python -m torch.distributed.launch --nproc_per_node=$GPUS --master_port=$PORT $(dirname "$0")/train.py $CONFIG --launcher pytorch --cfg-options work_dir=${WORK_DIR} ${@:3}
fi
python $(dirname $0)/find_best_from_log.py $WORK_DIR
if [ -f $WORK_DIR/best.pth ]; then
    echo $(dirname $0)/run_test.sh $WORK_DIR
    $(dirname $0)/run_test.sh $WORK_DIR
fi
if [ -f $WORK_DIR/test_result.txt ]; then
    python $(dirname $0)/get_config_summary.py $WORK_DIR
    tail $WORK_DIR/test_result.txt
fi



