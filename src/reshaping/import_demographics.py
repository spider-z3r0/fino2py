
from ..dependencies import pd, pl

def import_demographics(folder_path: str) -> pd.DataFrame:
    """
    Reads in the demographics from the .txt file and returns a DataFrame row containing the data.

    Parameters:
    file_path (str): Path to the demographics file.

    Returns:
    demographics_df (pd.DataFrame): DataFrame containing the demographics data.
    """

    try:
        folder_path = pl.Path(folder_path)
    except TypeError:
        raise TypeError('folder_path must be a pathlib.Path object or a string')

    if not folder_path.exists():
        raise ValueError('folder_path does not exist')

    if folder_path.is_dir():
        files = [file for file in folder_path.glob('*.txt')]
        if len(files) != 1:
            raise ValueError(f'Expected one .txt file, but found {len(files)} in the folder')
        file = files[0]
    elif folder_path.is_file():
        file = folder_path

    ID = file.stem.split('_')[0]

    # Read in the demographics data from the file
    df = pd.read_csv(
        file,
        sep=';',
        header=0,
        skiprows=2,
        nrows=1,
        engine='python'
        )

    # Select the relevant columns from the DataFrame
    demographics_df = df.loc[:, ['Identification', 'Age (yrs)', 'Height (cm)', 'Weight (kg)', 'Gender']]

    # Rename the columns
    demographics_df.columns = ['Participant ID', 'Age (years)', 'Height (cm)', 'Weight (kg)', 'Gender']


    return demographics_df