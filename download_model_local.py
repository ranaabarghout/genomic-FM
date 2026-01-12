#!/usr/bin/env python3
"""
Download DNABERT-2 model locally before running jobs on compute nodes
"""
import os
from transformers import AutoModel, AutoTokenizer

model_name = "zhihan1996/DNABERT-2-117M"
save_path = "/project/def-mahadeva/ranaab/genomic-FM/models/dnabert2"

print(f"Downloading {model_name} to {save_path}...")

# Create directory
os.makedirs(save_path, exist_ok=True)

# Download and save model
print("Loading model...")
model = AutoModel.from_pretrained(model_name, trust_remote_code=True)
print("Saving model...")
model.save_pretrained(save_path)

# Download and save tokenizer
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
print("Saving tokenizer...")
tokenizer.save_pretrained(save_path)

print(f"Model and tokenizer saved to {save_path}")
print("\nTo use this model, replace 'zhihan1996/DNABERT-2-117M' with the path:")
print(f"  {save_path}")
