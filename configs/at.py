import torch

config = {
    "task": "train",
    "model_args": {
        "arch": "resnet",
        "mean": torch.load("data/hello_mean.pt"),
        "var": torch.load("data/hello_var.pt"),
        "masks": [torch.ones_like(torch.load("data/hello_mean.pt"))]
    },
    "train_args": {
        "batch_size": 32,
        "epochs": 10,
        "lr": 1e-4,
        "num_gpus": 1,
        "adv_train": {
            "eps": 10,
            "step_size": 1,
            "steps": 10,
        }
    },
    "saliency_args": {
        "c": 0.001,
        "num_samples": 1000,
        "steps": 1000,
        "max_ensemble_size": 8
    },
    "eval_args": {
        "ckpt": [
            ],
        "threshold": [0.5],
        "attack": "surfree",
        "eps": 0.0257,
        "budget": 50000,
        "log_dir": "attack_results/at",
    }
}
