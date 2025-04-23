import torch

config = {
    "task": "adv_eval",
    "model_args": {
        "arch": "resnet",
        "mean": torch.load("data/hello_mean.pt"),
        "var": torch.load("data/hello_var.pt"),
        "masks": [], # for training i^th model, use i^th mask
    },
    "train_args": {
        "batch_size": 32,
        "epochs": 20,
        "lr": 1e-4,
        "num_gpus": 1,
        "adv_train": {
            "eps": 10,
            "step_size": 1,
            "steps": 10,
        }
    },
    "eval_args": {
        "ckpt": [
            "",
           ],
        "threshold": [0.5],
        "attack": "surfree",
        "eps": 0.0257,
        "budget": 50000,
        "log_dir": "attack_results/d4",
    }
}
