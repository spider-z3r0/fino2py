from ..dependencies import pd, Tuple

def minute_by_minute(df, df_id):

    df['Time (s)'] = df.index
    flat_array = df.values.flatten()
    flat_frame = pd.DataFrame(flat_array).T




    new_columns = [[f"{col}_minute_{i}" for col in df.columns] for i in range(df.shape[0])]
    new_columns_flat = [item for sublist in new_columns for item in sublist]



    flat_frame.columns = new_columns_flat
    flat_frame.insert(0, 'Participant ID', df_id)
   

    return flat_frame