# Working with time data

Managing data from the finometer requires us to work with timestamps from multiple sources, which can come to us in multiple formats. 

1. From the raw `.txt` files we get timestamps in the format
    - '10:34:01.340'
2. From the experimenters we get timesamps in either
    - '10:34:01'
    or
    - '10:34' (in the case of an error)

These need to be 'normalised to allow us to pull data together from various sources to make a complete data set, and as such we  have 3 functions

## converting the finometer time stamps

```
from ..dependencies import dt

def convert_fino_time(fino_time: str) -> dt.datetime.time:
    """
    Converts the string times produced by the Finometer to datime objects in the '%H:%M:%S.%f' format.

    Parameters:
    ----------
    fino_time : str
        The Finometer time in the format '%H:%M:%S.%f'

    Returns:
    -------
    datetime.time
        The time as a `datetime.time` object.
    """
    try:
        time = dt.datetime.strptime(fino_time, '%H:%M:%S.%f').time()
        time_str_no_ms = time.strftime('%H:%M:%S')
        time_obj_no_ms = dt.datetime.strptime(time_str_no_ms, '%H:%M:%S').time()
    except Exception as e:
        raise ValueError(f"Failed to convert time {fino_time} to datetime object. Error: {e}")

    return time_obj_no_ms
```

## 


