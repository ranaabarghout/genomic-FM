from src.dataloader.data_wrapper import (
    RealClinVar, OligogenicDataWrapper, MAVEDataWrapper,
    GWASDataWrapper, ClinVarDataWrapper, GeneKoDataWrapper,
    CellPassportDataWrapper, eQTLDataWrapper, sQTLDataWrapper
)

NUM_RECORDS = 1000
ALL_RECORDS = False
SEQ_LEN = 20

# Load RealClinVar data
data_loader = RealClinVar(num_records=NUM_RECORDS, all_records=ALL_RECORDS)
data = data_loader.get_data(Seq_length=SEQ_LEN)
print(data)

# Load Oligogenic data
data_loader = OligogenicDataWrapper(num_records=NUM_RECORDS, all_records=ALL_RECORDS)
data = data_loader.get_data(Seq_length=SEQ_LEN)
print(data)

# Load ClinVar data
data_loader = ClinVarDataWrapper(num_records=NUM_RECORDS, all_records=ALL_RECORDS)
data = data_loader.get_data(Seq_length=SEQ_LEN)
print(data)

# Load GeneKo data
data_loader = GeneKoDataWrapper(num_records=NUM_RECORDS, all_records=ALL_RECORDS)
data = data_loader.get_data(Seq_length=SEQ_LEN)
print(data)

# Load CellPassport data
data_loader = CellPassportDataWrapper(num_records=NUM_RECORDS, all_records=ALL_RECORDS)
data = data_loader.get_data(Seq_length=SEQ_LEN)
print(data)

# Load eQTL data
data_loader = eQTLDataWrapper(num_records=NUM_RECORDS, all_records=ALL_RECORDS)
data = data_loader.get_data(Seq_length=SEQ_LEN)
print(data)

# Load sQTL data
data_loader = sQTLDataWrapper(num_records=NUM_RECORDS, all_records=ALL_RECORDS)
data = data_loader.get_data(Seq_length=SEQ_LEN)
print(data)

# Load MAVE data
data_loader = MAVEDataWrapper(num_records=NUM_RECORDS, all_records=ALL_RECORDS)
data = data_loader.get_data(Seq_length=SEQ_LEN)
print(data)

# Load GWAS data
data_loader = GWASDataWrapper(num_records=NUM_RECORDS, all_records=ALL_RECORDS)
data = data_loader.get_data(Seq_length=SEQ_LEN)
print(data)