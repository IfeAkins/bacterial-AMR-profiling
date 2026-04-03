import pandas as pd

#load the AMRFinder output file
df = pd.read_csv("amrfinder_result.csv", sep=",")

#filter AMR  element with >80% coverage only
df_AMR = df[(df["Element type"] == "AMR") & (df["% Coverage of reference sequence"] > 80)]

# build grouped matrix (genes under class)
df_AMR_matrix = pd.crosstab(df_AMR["Name"], [df_AMR ["Class"], df_AMR ["Gene symbol"]])

#save
df_AMR_matrix.to_csv("AMRFinder_genes_matrix.csv")


#build AMR class matrix 
df_AMR_class = pd.crosstab(df_AMR["Name"], df_AMR["Class"])
df_AMR_class.to_csv("AMRFinder_class_matrix.csv")

print (f"\nTotal isolates analysed: {df_AMR['Name'].nunique()}")
print (f"Total unique AMR genes: {df_AMR['Gene symbol'].nunique()}")
print (f"Total unique drug class: {df_AMR['Class'].nunique()}")
print ("\nThe grouped matrix (genes under class) saved!")
print ("The AMR class matrix saved!")
