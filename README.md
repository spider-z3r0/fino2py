fino2py: A Python Package for Finometer Data Processing
================================================

fino2py is a Python package that provides tools for processing raw Finometer data. It offers a range of functions for ingesting, reshaping, and aggregating data, making it easier to work with cardiovascular data collected using the Finapress Finometer device.

Features
--------
- Import raw finometer data from `.txt` files generated by the finometer without needing to manually copy/paste from Beatscope
- Reshape finometer data into a minute-by-minute format to allow for trends to be identified
- Generate experimental protocol averages for each cardiovascular measure
- Append cardiovascular data from multiple files
- Save the processed data to `.csv` format for importing into python, R, SPSS or other stats software

Installation
------------
You can install fino2py using pip:

Windows

```
$ pip install fino2py
```


Documentation
-------------
The complete documentation for fino2py, including installation instructions and usage examples, can be found at [Read the Docs](https://fino2py.readthedocs.io/en/latest/).

Citing
------
If you use fino2py in your research or project, please cite it as:

Package Name: fino2py
Version: 0.1
Authors: Kev O'Malley, Ailbhe Dempsey, Siobhan Howard, Grace McMahon, Siobhan Griffin
Publication Date: May 2023

APA Style:
------------
O'Malley, K., Dempsey, A., Howard, S., McMahon, G., Griffen, G., (2023). fino2py (Version 0.1.0) [Software]. Available from https://pypi.org/project/fino2py


BibTeX:
------------
@misc{fino2py,
  title = {fino2py},
  version = {1.0},
  author = {O'Malley, Kev and Dempsey, Ailbhe and Howard, Siobhan and McMahon, Grace and Griffin, Siobhan},
  year = {2023},
  month = {June},
}


Contributing
------------
Contributions are welcome! If you find any issues or have suggestions for improvements, please submit them to the [GitHub repository](https://github.com/spider-z3r0/fino2py).


License
-------
This project is licensed under the MIT License

