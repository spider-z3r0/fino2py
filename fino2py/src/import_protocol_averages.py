from .dependencies import pl, pd
from .create_chunk import create_chunk
from functools import reduce

def import_protocol_averages(frame, id, times=None, save_csv=None):
    '''A function that imports the averaged finometer files (which have already been processed from the raw data)
    to produce averages for each section of the experimental protocol.

    Parameters
    ----------
    frame : pandas.DataFrame 
        The DataFrame containing the averaged finometer data
    id : str
        The participant ID
    save_csv : bool, optional
        If True, the imported data will be saved as a .csv file in the same folder as the .csv file, 
        this is not always needed and should be used sparingly
    times : dict, optional
        A dictionary of tuples of times, with the keys being the names of the time periods.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with the mean values of the given columns during each time period of the study.

    Raises
    ------
    TypeError
        If frame is not a pandas.DataFrame object
        If id is not a string
    ValueError
        If times is not provided as a dictionary with at least one key-value pair
        If there are not enough times provided for a given time period
        If there are too many times provided for a given time period
    '''

    # check if frame is a pandas.DataFrame object
    if not isinstance(frame, pd.DataFrame):
        raise TypeError('''
        frame must be a pandas.DataFrame object, produced by the read_raw_finometer_data function, 
        have you run the read_raw_finometer_data function on the data?''')

    if not isinstance(id, str):
        raise TypeError('id must be a string')

    if not times:
        raise ValueError("times must be a dictionary and at least one key-value pair must be provided.")
    
    # Create an empty list of dataframes, each representing a chunk of the protocol
    chunks = []
    
    for i in times.keys():
        if len(times[i]) < 2:
            raise ValueError(f"There are not enough times provided for the {i}.")
        elif len(times[i]) > 2:
            raise ValueError(f"There are too many times provided for the {i}.")
        elif len(times[i]) == 2:
            if times[i][0] < times[i][1]:
                chunks.append(create_chunk(frame, id, i, times[i][0], times[i][1]))



    data_merge = reduce(lambda left, right: pd.merge(left, right, on=["Participant ID"], how="outer"), chunks)
    data_merge.set_index('Participant ID', inplace=True)

    if save_csv:
        path = pl.Path(save_csv)
        data_merge.to_csv( path / f"{id} protocol_averages.csv")
        print(f"Saved {id} protocol averages.csv to {path.stem}")

    return data_merge