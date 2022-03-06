import random
import numpy as np
import torch
from src.experiments.experiment_1 import Experiment1

# Lock random seeds
_RNG_SEED_VAL = 1337
random.seed(_RNG_SEED_VAL)
np.random.seed(_RNG_SEED_VAL)
torch.manual_seed(_RNG_SEED_VAL)
torch.cuda.manual_seed_all(_RNG_SEED_VAL)


def load_checkpoint(checkpoint, model):
    print(f"=> Loading weights from {checkpoint}")
    model.load_state_dict(torch.load(checkpoint))


# Run training
experiment1 = Experiment1(batch_size=32)
"""
load_checkpoint("checkpoints/1/params.pt.15", experiment1.model)
print("Sanity check:")
validation_stats = experiment1.evaluate(experiment1.val_dataloader)  # Sanity check
print(validation_stats)
print(f"Validation set size: {experiment1.val_dataloader.dataset}")
print(f"Validation Top 1 Accuracy: {validation_stats['top1_acc']}")
print(f"Validation Top 10 Accuracy: {validation_stats['top10_acc']}")
print(f"Validation Top 100 Accuracy: {validation_stats['top100_acc']}")
print(f"Validation Loss: {validation_stats['loss']}")
"""
experiment1.train(n_epochs=20, fine_tune_epochs=4, evaluate_every=5, gradient_clip=1.0)
# experiment1.train(n_epochs=4, fine_tune_epochs=4, evaluate_every=1, gradient_clip=1.0)

# Evaluate on training and validation stats
training_stats = exp1.evaluate(exp1.val_dataloader)
print(f"  Training Top 1 Accuracy: {training_stats['top1_acc']}")
print(f"  Training Top 10 Accuracy: {training_stats['top10_acc']}")
print(f"  Training Top 100 Accuracy: {training_stats['top100_acc']}")
print(f"  Training Loss: {training_stats['loss']}")

validation_stats = exp1.evaluate(exp1.val_dataloader)
print(f"  Validation Top 1 Accuracy: {validation_stats['top1_acc']}")
print(f"  Validation Top 10 Accuracy: {validation_stats['top10_acc']}")
print(f"  Validation Top 100 Accuracy: {validation_stats['top100_acc']}")
print(f"  Validation Loss: {validation_stats['loss']}")
