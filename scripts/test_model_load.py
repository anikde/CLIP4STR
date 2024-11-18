import torch

# Try loading the model file directly
model_path = '/DATA1/ocrteam/anik/git/CLIP4STR/ViT-B-16.pt'
try:
    model = torch.load(model_path, weights_only=True)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

import torch

# Load the checkpoint
checkpoint = torch.load(model_path, weights_only=True)

# Check if "pytorch-lightning_version" key exists
if "pytorch-lightning_version" in checkpoint:
    print("Checkpoint saved with PyTorch Lightning version:", checkpoint["pytorch-lightning_version"])
else:
    print("Checkpoint does not contain the PyTorch Lightning version key.")

