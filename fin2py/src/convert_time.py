
from .dependencies import pd

def convert_time(time):
    '''This function converts the time stamps in the timesheets to datetime objects suitable for the other functions in this module
    Parameters
    ----------
    time : str
        The time stamp in the timesheets
    Returns
    -------
    datetime.datetime
        The time stamp converted to a datetime object
    '''
    time = pd.to_datetime(time)
    time = time.strftime('%H:%M:%S.%f')[:-3]
    return time
