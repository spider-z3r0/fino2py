
from ..dependencies import pd, dt



def convert_time(time: str) -> str:
    '''
    This function converts the time stamps in the timesheets to datetime objects suitable for the other functions in this module.

    Parameters:
    -----------
    time : str
        The time stamp in the timesheets

    Returns:
    --------
    str:
        The time stamp converted to a string format of '%H:%M:%S.%f' with microseconds removed.
    '''

    try:
        time = dt.strptime(time, '%H:%M:%S.%f')
    except Exception as e:
        raise ValueError(f"Failed to convert time {time} to datetime object. Error: {e}")

    time_str = time.strftime('%H:%M:%S.%f')[:-3]
    
    return time_str