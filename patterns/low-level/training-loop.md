# Training Loop (Low-level Pattern)

## Summary

Robust training loop patterns for checkpointing, mixed-precision, and distributed training.

## Solution

- Use an explicit epoch/step loop, checkpointing, and resume semantics.

## Example (pseudo)

```python
for epoch in range(start, max_epochs):
    for batch in loader:
        loss = model.step(batch)
        optimizer.step()
    save_checkpoint()
```
