'''This file doesn't really require any other imports. It's just a function that reads in two files and appends the data from the second file to the bottom of the first file.
The first file is the one that has the header information, so we save that and then append the data from the second file to the bottom of the first file. then rewrite the first 
file with the header and the appended data.'''

from typing import Optional, List, Union
from ..dependencies import Path

def append_cardio_data(
    part1_file: Union[str, Path],
    part2_file: Union[str, Path],
    output_file: Optional[Union[str, Path]] = None
) -> List[str]:
    '''
    Appends cardiovascular data from part 2 file to part 1 file and optionally writes the combined data to an output file.

    Parameters
    ----------
    part1_file : Union[str, Path]
        File path of the part 1 file.
    part2_file : Union[str, Path]
        File path of the part 2 file.
    output_file : Union[str, Path], optional
        File path of the output file to write the combined data (default is None).

    Returns
    -------
    List[str]
        List of combined cardiovascular data.
    '''
    
    # Step 1: Read in the part 1 file
    with open(part1_file, 'r') as f:
        lines_part1 = f.readlines()

    # Step 2: Save the header above line 9 in file 1
    header_part1 = lines_part1[:8]

    # Step 3: Save the data from line 9 down from file 1
    data_part1 = lines_part1[8:]

    # Step 4: Save the data from line 9 down in file 2
    with open(part2_file, 'r') as f:
        lines_part2 = f.readlines()[9:]

    # Step 5: Append the data from file 2 to the bottom of the data from file 1
    combined_data = data_part1 + lines_part2
    
    if output_file is not None:
        # Step 6: Write all three things to a .txt file
        with open(output_file, 'w') as f:
            f.writelines(header_part1)
            f.writelines(combined_data)
    
    return combined_data