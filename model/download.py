import kagglehub

# Download latest version
path = kagglehub.model_download("google/gemma-2/pyTorch/gemma-2-9b-pt")

print("Path to model files:", path)