"""
Inspect sQTL data to understand original format before PCA transformation
"""
from src.dataloader.data_wrapper import sQTLDataWrapper

# Load sQTL data with longer sequences to see full context
NUM_RECORDS = 100
SEQ_LEN = 1024  # Match the sequence length used in training

print("="*80)
print("Loading sQTL data...")
print(f"Number of records: {NUM_RECORDS}")
print(f"Sequence length: {SEQ_LEN}")
print("="*80)

data_loader = sQTLDataWrapper(num_records=NUM_RECORDS, all_records=False)
data = data_loader.get_data(Seq_length=SEQ_LEN)

print("\nFirst 10 records:")
for i, record in enumerate(data[:10]):
    ref_seq, alt_seq, tissue, label = record[0][0], record[0][1], record[0][2], record[1]
    print(f"\nRecord {i+1}:")
    print(f"  Tissue: {tissue}")
    print(f"  Label: {label}")
    print(f"  Ref sequence (first 100bp): {ref_seq[:100]}")
    print(f"  Alt sequence (first 100bp): {alt_seq[:100]}")
    # Check where sequences differ
    diff_positions = [j for j in range(min(len(ref_seq), len(alt_seq))) if ref_seq[j] != alt_seq[j]]
    print(f"  Differences at positions: {diff_positions[:10] if len(diff_positions) > 10 else diff_positions}")
    print(f"  Total differences: {len(diff_positions)}")

print("\n" + "="*80)
print("Data structure:")
print(f"Type: {type(data)}")
print(f"Length: {len(data)}")
print(f"First record structure: {type(data[0])}")
print(f"First record: [[ref_seq, alt_seq, tissue], label]")
print("="*80)
