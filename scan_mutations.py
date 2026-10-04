import pandas as pd
from Bio import AlignIO
import os

# Define input alignment file
alignment_file = "pb2_aligned.fasta"

if not os.path.exists(alignment_file):
    print(f"Error: {alignment_file} not found. Please run MAFFT alignment first.")
else:
    alignment = AlignIO.read(alignment_file, "fasta")
    results = []

    for record in alignment:
        seq_str = str(record.seq)
        sample_id = record.id
        
        # PB2 1-based coordinates mapped to 0-based Python indexing
        res_591 = seq_str[590] if len(seq_str) > 590 else "-"
        res_627 = seq_str[626] if len(seq_str) > 626 else "-"
        res_701 = seq_str[700] if len(seq_str) > 700 else "-"
        
        # Classification logic
        is_adapted = (res_627 == 'K' or res_591 == 'K' or res_701 == 'N')
        phenotype = "Mammalian-Adapted" if is_adapted else "Avian Wild-Type"
        
        results.append({
            "Isolate_ID": sample_id,
            "PB2_591": res_591,
            "PB2_627": res_627,
            "PB2_701": res_701,
            "Predicted_Phenotype": phenotype
        })

    df = pd.DataFrame(results)
    df.to_csv("mutation_summary.csv", index=False)
    print("Screening complete! Output saved to mutation_summary.csv\n")
    print(df.to_string(index=False))