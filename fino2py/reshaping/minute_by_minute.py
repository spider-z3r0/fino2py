'''
This module provides a function for reshaping participant's minute-by-minute data into a single row.

The main function, `minute_by_minute`, takes a DataFrame containing finometer data and performs reshaping of the data. It converts the index into a column named "Time (s)" to preserve the original time information. The DataFrame is then flattened, creating a new DataFrame with each minute's data in separate columns. The column names are generated by appending "_minute_i" to the original column names, where "i" represents the minute index. The Participant ID is added as a column at the beginning of the new DataFrame, facilitating concatenation of participant data for sample-level analysis.

Note: The `minute_by_minute` function assumes that the input DataFrame contains the necessary columns and structure for reshaping.

Functions
---------
minute_by_minute(df: pd.DataFrame, df_id: str) -> pd.DataFrame:
    Reshape the participant's minute-by-minute data into a single row.
    Returns a DataFrame with each minute's data in separate columns.

    Parameters
    ----------
    df : pandas DataFrame
        The DataFrame containing finometer data.
    df_id : str
        The Participant ID associated with the data.

    Returns
    -------
    pandas DataFrame
        The reshaped minute-by-minute data DataFrame.
        Each minute's data is in separate columns, with column names reflecting the original column names and minute indices. The Participant ID column is included at the beginning.
'''


from ..dependencies import pd, Tuple #importing pandas and Tuple from dependencies.py

def minute_by_minute(df: pd.DataFrame, df_id: str) -> pd.DataFrame:
    '''
    Reshape the participant's minute by minute data into a single row 

    This function takes a DataFrame containing finometer data (`df`). It converts the index of the DataFrame into a column named "Time (s)" to preserve the original time information.

    The DataFrame is then flattened to create a new DataFrame (`flat_frame`) with each minute's data in a separate column. The column names are generated by appending "_minute_i" to the original column names, where "i" represents the minute index.

    The Participant ID (`df_id`) is added as a column at the beginning of the `flat_frame` DataFrame. This allows for participant data to be easily concatenated into a single DataFrame for sample level analysis.

    Parameters
    ----------
    df : pandas DataFrame
        The DataFrame containing the finometer data.
    df_id : str
        The Participant ID associated with the data.

    Returns
    -------
    pandas DataFrame
        The minute-by-minute analysis DataFrame.

        The `flat_frame` DataFrame contains each minute's data in separate columns, with column names reflecting the original column names and minute indices. The Participant ID column is included at the beginning.
    '''

    df['Time (s)'] = df.index
    flat_array = df.values.flatten()
    flat_frame = pd.DataFrame(flat_array).T




    new_columns = [[f"{col}_minute_{i}" for col in df.columns] for i in range(df.shape[0])]
    new_columns_flat = [item for sublist in new_columns for item in sublist]



    flat_frame.columns = new_columns_flat
    flat_frame.insert(0, 'Participant ID', df_id)
   

    return flat_frame