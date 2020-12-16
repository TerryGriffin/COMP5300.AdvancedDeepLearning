"""
get_config_summary reads the config file and the test_results.txt file
and creates config_summary.txt containing a single line summarizing the
config and results.
"""
import os
import sys
import glob
import re
import shutil

def get_config_summary(root):
    sys.path.append(root)
    config_file = glob.glob(os.path.join(root, "*.py"))
    if len(config_file) != 1:
        print(f"{root}: found {len(config_file)} config files")
        return -1
    config_file = os.path.basename(config_file[0])

    config = __import__(config_file[:-3])
    model_type = config.model["type"]
    backbone = config.model["backbone"]["type"]
    backbone_depth = config.model["backbone"]["depth"]
    pretrain = config.model["pretrained"]
    train_set = os.path.basename(config.data["train"]["ann_file"])
    evaluation = str(config.evaluation["metric"]).replace(',',' ').replace("'","")
    optimizer = config.optimizer["type"]
    lr = config.optimizer["lr"]
    momentum = config.optimizer.get("momentum", 0)
    weight_decay = config.optimizer["weight_decay"]
    work_dir = os.path.basename(config.work_dir)
    warmup_iters = config.lr_config["warmup_iters"]
    lr_steps = str(config.lr_config["step"]).replace(',',' ')
    total_epochs = config.total_epochs

    with open(os.path.join(root,"test_result.txt"),"r") as f:
        results = f.readlines()[-1]


    output_filename = os.path.join(root,"config_summary.txt")
    with open(output_filename,"w") as f:
        f.write("work_dir, config_file, model_type, backbone, backbone_depth, pretrain, "
                "train_set, evaluation, optimizer, lr, momentum, weight_decay, "
                "warmup_iters, lr_steps, total_epochs\n")
        f.write(f"{work_dir}, {config_file}, {model_type}, {backbone}, {backbone_depth}, {pretrain}, "
                f"{train_set}, {evaluation}, {optimizer}, {lr}, {momentum}, {weight_decay}, "
                f"{warmup_iters}, {lr_steps}, {total_epochs}, {results}")
    return 0

if __name__ == "__main__":
    exit(get_config_summary(sys.argv[1]))
