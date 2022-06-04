from pathlib import Path

import torch
from torch.nn import CosineSimilarity

from unixcoder import UniXcoder

device = "cpu"
model = UniXcoder("microsoft/unixcoder-base")
model.to(device)

cosine_sim = CosineSimilarity()
sim = lambda x, y: cosine_sim(x, y).item()

def embed(x: str):
    chunks = [x[i:i+512] for i in range(0, len(x), 512)]
    
    accumulate = torch.zeros(1, 768)

    for chunk in chunks:
        tokens_ids = model.tokenize([chunk])
        source_ids = torch.tensor(tokens_ids).to(device)
        _, max_func_embedding = model(source_ids)
        accumulate += max_func_embedding

    return accumulate / len(chunks)

def embed_from_file(path: Path):
    with open(path) as fp:
        return embed(fp.read())
