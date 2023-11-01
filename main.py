import pandas as pd
file_path = 'diabetic_data.csv'
df = pd.read_csv(file_path, header=0, delimiter=',')

#1 Melt
melt_df = df[['patient_nbr', 'diag_1', 'diag_2', 'diag_3']]
melted_df = melt_df.melt(id_vars=['patient_nbr'], var_name='diagnosis_num', value_name='diagnosis') #Melts the differing diagnosis columns for the patient_nbr
print(melted_df)

#2 Pivot
pivot_df = df[['encounter_id', 'diag_1', 'admission_type_id']]
pivoted_df = pivot_df.pivot(index='encounter_id', columns='admission_type_id', values='diag_1') #Not the best example, I would've loved a date column, but this shows the pivot functionality
print(pivoted_df)

#3 Aggregation
agg_df = df[['diag_1', 'diag_2', 'diag_3']]
agged_df = agg_df.agg(['min', 'max']) #This will look through all the diag values and return the min/max of each one
print(agged_df)

#4 Iteration
iter_df = df[['patient_nbr', 'age', 'diag_2']]
for i, row in iter_df.iterrows():
    print(row['patient_nbr'], row['age'], row['diag_2']) #Returns an iterated version of the rows, and specified columns

#5 Groupby
grouped = df.groupby('patient_nbr')
maxed = grouped['diag_1'].max() #These will group by the patient_nbr column, and return the max diag_1 value
print(maxed)
