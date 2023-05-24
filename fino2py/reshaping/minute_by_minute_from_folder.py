from ..dependencies import pd, Tuple
from .read_raw_finometer_data import read_raw_finometer_data
from .minute_by_minute import minute_by_minute

def minute_by_minute_from_folder(path, int = '1T', save_raw = False, save = False) -> Tuple[pd.DataFrame, str]:
    frame, id = read_raw_finometer_data(path, interval= int, save_csv= save_raw)

    minute_frame = minute_by_minute(frame, id)
    
    if save == True:
        minute_frame.to_csv(path / f'{id} minute_by_minute.csv', index = False)

    return minute_frame, id