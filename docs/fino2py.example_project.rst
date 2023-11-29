Example Project
===============

In this example, we will walk you through a project using the `fino2py` package for working with Finapress finometer data.
We'll cover the basic steps, including installation of the package, data loading, data cleaning, and visualization.

Installation
------------

To get started, you need to install the `fino2py` package. Open a terminal and run the following command:

.. code-block:: bash

   pip install fino2py

We recommend that you use a `virtual environment <https://realpython.com/python-virtual-environments-a-primer/>`_
to manage your project and keep your dependencies safe.

Once you've installed the package (and any others that you may need), you should be ready to start working with the data you've collected from participants
using the Finapress finometer. In this example project, we will be working with data from 3 participants (all ficticious) and providing examples of how you might wish to
work with the data. This is based on the experience of users in the University of Limerick and so there may be some differences in how your group work with the data, we'd love to hear from you
if you have any suggestions for improvements to the package or the documentation, especially if you have suggestions on generating the derived measures.

Raw Data
--------

The Finapress finometer automatically generates a folder for each participant's data collection. These folders are named
with a consistent pattern using the participant's identifier and the date and time of data collection, separated by underscores.

For example, if the identifier is 'Participant 1234' and data is collected at noon on the 8th of August 2022, the finometer
will create a folder named:

'Participant 1234_2022-08-08_12:00:03'

Inside this folder, three types of files are automatically generated:

.. code-block:: none

   Participant 1234_2022-08-08_12:00:03/
   ├── Participant 1234_2022-08-08_12:00:03.evt
   ├── Participant 1234_2022-08-08_12:00:03.fpf
   └── Participant 1234_2022-08-08_12:00:03.txt

These files serve different purposes:

- 'Participant 1234_2022-08-08_12:00:03.evt': Contains markers used by the finometer itself.
- 'Participant 1234_2022-08-08_12:00:03.fpf': Data files read by tools like Beatscope.
- 'Participant 1234_2022-08-08_12:00:03.txt': Raw data files which can be processed by the `fino2py` package.

The consistent naming and structure of these folders and files allow the `fino2py` package to efficiently ingest, clean,
 and reshape the data rather than having to manually ingest and reshape the data using a combination of Beatscope and Microsoft excel.

The data we want to work with is stored in the .txt files and so for each participant there will be a subfolder like the one
we have outlined above, and we can store these subfolders in a parent data folder.

For example, if we have data from 3 participants, the parent folder will contain 3 subfolders, one for each participant:

.. code-block:: none

   Participant 1234_2022-08-08_12:00:03/
   ├── Participant 1234_2022-08-08_12:00:03.evt
   ├── Participant 1234_2022-08-08_12:00:03.fpf
   └── Participant 1234_2022-08-08_12:00:03.txt

   Participant 5678_2022-08-07_11:33:52/
   ├── Participant 5678_2022-08-07_11:33:52.evt
   ├── Participant 5678_2022-08-07_11:33:52.fpf
   └── Participant 5678_2022-08-07_11:33:52.txt

   Participant 9012_2022-08-09_12:08:51/
   ├── Participant 9012_2022-08-09_12:08:51.evt
   ├── Participant 9012_2022-08-09_12:08:51.fpf
   └── Participant 9012_2022-08-09_12:08:51.txt

Before we get into the actual project we should speak briefly about the raw data itself.

Format of the Raw Data
----------------------

The .txt files contain the raw data collected by the finometer. There are actually 2 different datasets in each file.
The first is the participants' demographic data, which is entered by the researcher at the start of the data collection session.
The second is the data collected by the finometer during the data collection session. The data collected by the finometer represents 11 different
variables including Systolic Pressure (in mmHg), Diastolic Pressure (in mmHg), Mean Pressure (in mmHg), Heart rate (in beats per minute), 
Stroke Volume (in milliliters), Left Ventricular Ejection Time (in milliseconds), Pulse Interval (in milliseconds), Maximum Slope (in mmHg/s), 
Cardiac Output (in liters per minute), Total Peripheral Resistance in Medical Unit (in mmHg.min/l), Total Peripheral Resistance in CGS (in dyn.s/cm5), as well as the timestamp 
for each data point (in milliseconds) and any Markers that may have been captured on the finometer itself. 

Below is an example of the raw data from a single participant (this is fake data):


.. code-block:: none
   :linenos:

    BeatScope Easy - v02.10 build 004

    Identification;Identification;Age (yrs);Height (cm);Weight (kg);Gender;Procedure;Model number
    Participant 1234;Participant 1234;26;153;60;Female;;9715

    Reconstructed pressure level: 
    brachial
    
    Time (s);Systolic Pressure (mmHg);Diastolic Pressure (mmHg);Mean Pressure (mmHg);Heart rate (bpm);Stroke Volume (ml);Left Ventricular Ejection Time (ms);Pulse Interval (ms);Maximum Slope (mmHg/s);Cardiac Output (l/min);Total Peripheral Resistance Medical Unit (mmHg.min/l);Total Peripheral Resistance CGS (dyn.s/cm5);Markers;
    12:00:03.005;0;0;0;89;0.0;0;675;0;0.0;0.000;0;;
    12:00:03.680;0;0;0;72;0.0;0;835;0;0.0;0.000;0;;
    12:00:04.515;0;0;0;71;0.0;0;845;0;0.0;0.000;0;;
    12:00:05.360;0;0;0;69;0 vc.0;0;870;0;0.0;0.000;0;;
    12:00:06.230;0;0;0;67;0.0;0;895;0;0.0;0.000;0;;
    12:00:07.125;0;0;0;70;0.0;0;855;0;0.0;0.000;0;;
    12:00:07.980;0;0;0;77;0.0;0;775;0;0.0;0.000;0;;
    12:00:08.755;0;0;0;75;0.0;0;795;0;0.0;0.000;0;;
    12:00:09.550;0;0;0;73;0.0;0;825;0;0.0;0.000;0;;
    12:00:10.375;0;0;0;72;0.0;0;835;0;0.0;0.000;0;;
    12:00:11.210;0;0;0;76;0.0;0;785;0;0.0;0.000;0;;
    12:00:11.995;0;0;0;76;0.0;0;790;0;0.0;0.000;0;;
    12:00:12.788;126;69;90;76;63.3;295;785;1546;4.8;1.117;1489;;
    12:00:13.571;126;69;90;72;68.3;290;835;1571;4.9;1.101;1468;;
    12:00:14.404;128;68;91;75;72.3;295;795;1625;5.5;1.001;1335;;
    12:00:15.201;126;69;91;77;69.5;300;775;1458;5.4;1.009;1346;;
    12:00:15.972;127;73;92;75;70.3;295;795;1467;5.3;1.035;1381;;
    12:00:16.770;129;72;92;75;75.0;300;800;1550;5.6;0.984;1312;;
    12:00:17.573;129;73;91;73;73.0;310;820;1554;5.3;1.025;1367;;
    12:00:18.390;125;73;90;78;63.8;295;770;1271;5.0;1.084;1445;;
    12:00:19.161;123;74;90;84;57.8;290;715;1225;4.8;1.114;1486;;
    12:00:19.876;124;75;90;82;57.8;290;735;1142;4.7;1.145;1527;;
    12:00:20.610;124;75;90;78;57.8;290;765;1142;4.5;1.192;1590;;
    12:00:21.375;124;75;90;74;57.8;290;815;1142;4.3;1.270;1694;;
    12:00:22.191;123;73;91;78;55.3;290;765;1250;4.3;1.260;1680;;
    12:00:22.952;122;76;94;82;54.5;290;730;1233;4.5;1.252;1670;;
    12:00:23.686;121;76;91;79;50.3;290;755;1008;4.0;1.371;1828;;
    12:00:24.437;120;77;92;78;53.8;330;765;1079;4.2;1.309;1746;;
    12:00:25.204;119;74;91;77;58.5;295;775;1129;4.5;1.206;1607;;
    12:00:25.979;117;75;92;84;55.0;285;715;1083;4.6;1.199;1599;;
    12:00:26.696;118;76;92;82;56.0;300;730;1071;4.6;1.199;1599;;
    12:00:27.424;120;75;93;78;60.8;310;765;1058;4.8;1.174;1566;;
    12:00:28.191;121;77;94;75;62.3;295;795;1188;4.7;1.194;1592;;
    12:00:28.982;121;75;94;81;62.3;295;740;1038;5.0;1.111;1482;;
    12:00:29.725;121;75;94;82;62.3;295;730;1038;5.1;1.096;1462;;
    12:00:30.455;121;75;94;77;62.3;295;780;1038;4.8;1.172;1562;;
    12:00:31.234;122;78;95;76;57.3;285;790;1383;4.3;1.314;1752;;
    12:00:32.028;122;78;94;75;54.5;295;795;1283;4.1;1.368;1823;;
    12:00:32.821;118;77;93;79;50.3;280;755;1333;4.0;1.394;1858;;
    12:00:33.576;119;78;93;81;50.3;290;745;1217;4.0;1.375;1833;;
    12:00:34.323;118;77;93;77;56.0;300;780;1138;4.3;1.288;1718;;
    12:00:35.101;121;77;93;74;57.8;290;810;1217;4.3;1.304;1739;;
    12:00:35.907;118;77;93;77;55.3;295;775;1254;4.3;1.298;1730;;
    12:00:36.688;118;77;94;81;55.5;285;740;1350;4.5;1.250;1667;;
    12:00:37.426;120;78;93;77;54.8;295;775;1300;4.2;1.313;1751;;
    12:00:38.201;120;78;93;77;54.8;295;775;1242;4.2;1.313;1751;;
    12:00:38.975;120;78;93;74;54.8;295;815;1242;4.0;1.381;1841;;
    12:00:39.790;120;78;93;74;54.8;295;810;1242;4.1;1.372;1830;;
    12:00:40.601;118;78;91;76;48.8;290;785;1413;3.7;1.465;1954;;
    12:00:41.386;117;75;92;76;53.8;290;790;1471;4.1;1.345;1793;;
    12:00:42.174;118;74;92;75;56.5;290;805;1354;4.2;1.304;1738;;
 
 
 
As you can see, the file has a header on line 1 which indicates the version of Beatscope used to generate the file. Then, beginging on line 3 
there is a short table containing the participant's demographic data. And finally, beginning on line 9, there is a table containing the data collected by the finometer.

Times
-----

Many studies using the Finapress finometer will collect data with multiple phases *within a session*.
For example, a study may
1. collect baseline data (where the participant is asked to sit and allow the device to calibrate),
2. may then impose some kind of task or stressor on the participant (such as a math task, for example),
3. impose a recovery period (in which the participants again sit quietly).

In this example project, we will be working with data collected in 3 phases within the experimental protocol: baseline, task, and recovery.

The finometer can produce two different kinds of timestamps: 'absolute' and 'relative'.

Absolute timestamps are the time of day at which the data was collected, relative timestamps are the time since the start of the data collection.
The `fino2py` package can work with either of these timestamps, but for this example project, we will be using the relative timestamps,
as these are more complex to work with.

The first column of the .txt file contains the relative timestamps for each data point (in this case, a heartbeat).

As each participant had their own data collection slot the times for each participant researchers will often create a table
(saved as a .csv or .xlsx file) in the parent folder that has the time markers for each participant. This table contains the participant identifier,
the start time of the data collection, the key timestamps, and the end time of the data collection.
These timestamps are captured by the researcher and are often entered manually into a paper document or spreadsheet.
Often they are accurate to the second (not the millisecond), but there can be errors such as in cases where only the hour and minute are recorded.
This isn't ideal, but we can work with it (more on that later).

.. table:: Participant Data
   :widths: 20 15 15 15 15 15 15 15

   +-----------------+--------------+------------------+----------------+---------------+------------+-----------------+-----------------+
   | Participant     | Start        | Start of Baseline| End of Baseline| Start of Task | End of Task| Start of Recovery| End            |
   +=================+==============+==================+================+===============+============+=================+=================+
   | Participant 1234| 12:00:03     | 12:03:07         | 12:10:07       | 12:11:07      | 12:16:07   | 12:17:07        | 12:22:07        |
   +-----------------+--------------+------------------+----------------+---------------+------------+-----------------+-----------------+
   | Participant 5678| 11:33:52     | 11:36:52         | 11:43:52       | 11:44:52      | 11:49:52   | 11:50:52        | 11:55:52        |
   +-----------------+--------------+------------------+----------------+---------------+------------+-----------------+-----------------+
   | Participant 9012| 12:08:51     | 12:09:51         | 12:16:51       | 12:17:51      | 12:22:51   | 12:23:51        | 12:28:51        |
   +-----------------+--------------+------------------+----------------+---------------+------------+-----------------+-----------------+


The times produced by the finometer are in the format 'hours:minutes:seconds.millisecond' and so the `fino2py` package has functions 
that allow us to convert all these times to the same format so we can work together with them to create a single dataframe for the project.

But first, lets take a look at ingesting the raw finometer data.

Ingesting the Raw demographic data
----------------------------------

As we said above, the raw data contains two datasets: the demographic data and the finometer data. The demographic data is stored at the top of the .txt file and we can use the 
`read_raw_demographics` function to ingest this data. This function can take the path to the participant's subfolder or the path to the .txt file itself. In this example we will use the path to the subfolder.


.. code-block:: python
   :linenos:

   import fino2py as f2p

   # path to the subfolder for participant 1234
   participant_folder = pl.Path('path/to/parent/folder/Participant 1234_2022-08-08_12:00:03')

   # ingest the demographic data
   demo_data = f2p.read_raw_demographics(participant_folder)

   # print the demographic data
   print(demo_data)

.. csv-table::
   :header: "Participant ID", "Age (years)", "Height (cm)", "Weight (kg)", "Gender"
   :widths: 20, 10, 12, 12, 10

   "Participant 1234", 26, 153, 60, "Female"

If we want to ingest the demographic data for all participants, we can use a `list comprehension <https://www.pythonforbeginners.com/basics/list-comprehensions-in-python>`_ 
to loop through the subfolders and ingest the data for each participant and `concat` them into a single dataframe.

.. code-block:: python
   :linenos:

   # path to the parent folder
   parent_folder = pl.Path('path/to/parent/folder')

   # ingest the demographic data for all participants

   demographics = pd.concat([f2p.read_raw_demographics(i) for i in parent_folder.glob('**/*.txt')], axis=0)

   # print the demographic data
   print(demographics)

.. csv-table::
   :header: "Participant ID", "Age (years)", "Height (cm)", "Weight (kg)", "Gender"
   :widths: 20, 10, 12, 12, 10

   "Participant 1234", 26, 153, 60, "Female"
   "Participant 5678", 30, 160, 65, "Male"
   "Participant 9012", 27, 165, 55, "Female"

In the above example we used the `glob <https://docs.python.org/3/library/glob.html>`_ function to find all the .txt files in the parent folder and then looped through them using a list comprehension. 
There are other ways to do this, but this is a simple and efficient way, especially if you have a large number of participants. Now that we have demographic data for all participants, we can move on to ingesting the hemodynamic data;
lets start by ingesting the data for a single participant.

Ingesting the Raw Hemodynamic Data
-----------------------------------
Just as a reminder, the hemodynamic data begins on line 9 of the .txt file and contains 11 measures (listed above). These measures are captured at each heartbeat 
and so the data is stored in a table with a row for each heartbeat and a column for each measure. The first column contains the relative timestamps for each heartbeat measured in milliseconds.

The  `read_raw_finometer_data` function allows us to import and save (if desired) the raw data for a single participant. Again, this function can take the path to 
the participant's subfolder or the path to the .txt file itself. In this example we will use the path to the subfolder. In this first example we will simply import the raw data for
Participant 1234 without saving it or resampling it.

Note that the `read_raw_demographics` function returns 2 objects, the first is a dataframe containing the demographic data and the second is the Participant ID. This is to allow for
other functions to be used with the demographic data and protocol times, but for now we will just ignore the second object.

.. code-block:: python
   :linenos:

   import fino2py as f2p

   # path to the subfolder for participant 1234
   participant_folder = pl.Path('path/to/parent/folder/Participant 1234_2022-08-08_12:00:03')

   # ingest the raw hemodynamic data
   # note that we also get the participant ID (id) as the second object returned by the function
   raw_data, id = f2p.read_raw_finometer_data(participant_folder)

   # print the raw hemodynamic data
   raw_data.head()

.. csv-table::
   :header: "Time (s)", "Systolic Pressure (mmHg)", "Diastolic Pressure (mmHg)", "Mean Pressure (mmHg)", "Heart rate (bpm)", "Stroke Volume (ml)", "Left Ventricular Ejection Time (ms)", "Pulse Interval (ms)", "Maximum Slope (mmHg/s)", "Cardiac Output (l/min)", "Total Peripheral Resistance Medical Unit (mmHg.min/l)", "Total Peripheral Resistance CGS (dyn.s/cm5)", "Markers"
   :widths: 12, 24, 24, 20, 18, 18, 30, 24, 24, 22, 30, 40, 10

   "12:00:03.005", 120, 70, 90, 80, 60.0, 290, 800, 1300, 4.6, 1.2, 1600
   "12:00:03.680", 121, 72, 91, 82, 61.0, 295, 790, 1320, 4.7, 1.19, 1580
   "12:00:04.515", 122, 71, 92, 85, 62.0, 300, 780, 1350, 4.8, 1.18, 1560
   "12:00:05.360", 122, 73, 93, 88, 63.0, 305, 770, 1380, 4.9, 1.17, 1540


In general, we want to both save the imported data as a .csv file for easier access later and resample the data to a consistent sampling rate. The resampling is based on pandas resampling and so you can use any of the pandas resampling methods and so we pass a `string` indicating the sampling
frequncy as an argument to the `read_raw_finometer_data` finometer function call. In this example we will use a sampling frequency of 1 sample per second `('1s')` but you could also call 1 Minute `('1T')` or 30 seconds `('30s')` depending on your needs (check out the docs on `pandas resampling <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html>`_ for more info).


To save the data we pass the `save_csv=True` argument to the function call. This will save the data in the same folder as the .txt file and will name the file using the participant ID and the sampling frequency. In this example the file will be named 'imported 1s data for Participant 1234.csv'
(note that the file name will be different if you use a different sampling frequency).

.. code-block:: python
   :linenos:

   import fino2py as f2p

   # path to the subfolder for participant 1234
   participant_folder = pl.Path('path/to/parent/folder/Participant 1234_2022-08-08_12:00:03')

   # ingest the raw hemodynamic data
   # note that we also get the participant ID (id) as the second object returned by the function
   raw_data, id = f2p.read_raw_finometer_data(participant_folder, sampling_freq='1s', save=True)

   # print the raw hemodynamic data
   raw_data.head(4)

.. csv-table::
   :header: "Time (s)", "Systolic Pressure (mmHg)", "Diastolic Pressure (mmHg)", "Mean Pressure (mmHg)", "Heart rate (bpm)", "Stroke Volume (ml)", "Left Ventricular Ejection Time (ms)", "Pulse Interval (ms)", "Maximum Slope (mmHg/s)", "Cardiac Output (l/min)", "Total Peripheral Resistance Medical Unit (mmHg.min/l)", "Total Peripheral Resistance CGS (dyn.s/cm5)", "Markers"
   :widths: 12, 24, 24, 20, 18, 18, 30, 24, 24, 22, 30, 40, 10

   "12:00:03.000", 120.5, 71.0, 90.5, 81.0, 60.5, 292.5, 795.0, 1310.0, 4.65, 1.195, 1590.0
   "12:00:04.000", 122.0, 71.0, 92.0, 85.0, 62.0, 300.0, 780.0, 1350.0, 4.8, 1.18, 1560.0
   "12:00:05.000", 122.0, 73.0, 93.0, 88.0, 63.0, 305.0, 770.0, 1380.0, 4.9, 1.17, 1540.0
   "12:00:06.000", 123.0, 75.0, 94.0, 90.0, 64.0, 310.0, 760.0, 1410.0, 5.0, 1.16, 1520.0

The above example has resampled the data to 1 sample per second and saved the data as a .csv file into the same folder as the main data. At each stage we have chosen to allow you to save new data
so that it can be visually inspected and checked for errors. This is especially important when working with the raw data as there can be errors in the data collection process (such as finometer errors) and in the 'munging'
process (such as errors in the protocol times). You do not have to save new data at each stage, but the option is there and it costs very little in terms of time and memory to do so.

We have seen how we might ingest the raw data for a single participant, but in the context of research studies we have multiple participants, and so we need to be able to manipulate (as minimally as possible)
the data to allow us to analyse the data for all participants. In this case we can see that each participant's data is 'tall' with each row representing a single heartbeat. This is not ideal for analysis and 
so we need to 'reshape' the data to be 'wide' with each row representing a single participant and each column representing a single measure *at a single time*; this allows for the data to be analysed using standard 
statistical methods in SPSS (which hopefully packages like this will help us move away from).

Reshaping the Data
------------------

The `fino2py` package has a few functions that allow us to reshape the data depending on our needs. Most commonly, we need to generate the 1 minute averages for each participant before we do anything else with the data, as such our
first reshaping is called `minute_by_minute` and it generates the 1 minute averages for each participant and then moves all this data to be a single row. This is a little confusing for people who are new to managing data, but once you see the output it is easier to make sense of.

The `minute_by_minute` function takes the `DataFrame` produced by the `read_raw_finometer_data` function as it's argument, there is a `minute_by_minute_from_folder` function that allows you
to pass the path to your subfolders (essectially calling both the `read_raw_finometer_data` and `minute_by_minute` functions in one go) but we will use the `minute_by_minute` functionin this first example.

.. code-block:: python
   :linenos:

   import fino2py as f2p

   # path to the subfolder for participant 1234
   participant_folder = pl.Path('path/to/parent/folder/Participant 1234_2022-08-08_12:00:03')

   # ingest the raw hemodynamic data
   # note that we also get the participant ID (id) as the second object returned by the function
   # also note, that in order for this example to work you must call the function with the '1T' value
   raw_data, id = f2p.read_raw_finometer_data(participant_folder, '1T', save_csv=True)

   # reshape the data to be 1 minute averages
   reshaped_data = f2p.minute_by_minute(raw_data, id)

   # select just the first 2 minutes of data so that the table isn't crazy long, there's actually 41 minutes of data
   # This would result in a table with 41 * 14 columns = 574 columns
   end_col_index = reshaped_data.columns.get_loc('Time (s)_minute_1')

   # Select columns up to and including 'Time(s)_minute_1'
   subset_df = reshaped_data.iloc[:, :end_col_index + 1]

   subset_df

.. csv-table:: Participant Data
   :header: "Participant ID", "Systolic Pressure (mmHg)_minute_0", "Diastolic Pressure (mmHg)_minute_0", "Mean Pressure (mmHg)_minute_0", "Heart rate (bpm)_minute_0", "Stroke Volume (ml)_minute_0", "Left Ventricular Ejection Time (ms)_minute_0", "Pulse Interval (ms)_minute_0", "Maximum Slope (mmHg/s)_minute_0", "Cardiac Output (l/min)_minute_0", "Total Peripheral Resistance Medical Unit (mmHg.min/l)_minute_0", "Total Peripheral Resistance CGS (dyn.s/cm5)_minute_0", "Time (s)_minute_0", "Systolic Pressure (mmHg)_minute_1", "Diastolic Pressure (mmHg)_minute_1", "Mean Pressure (mmHg)_minute_1", "Heart rate (bpm)_minute_1", "Stroke Volume (ml)_minute_1", "Left Ventricular Ejection Time (ms)_minute_1", "Pulse Interval (ms)_minute_1", "Maximum Slope (mmHg/s)_minute_1", "Cardiac Output (l/min)_minute_1", "Total Peripheral Resistance Medical Unit (mmHg.min/l)_minute_1", "Total Peripheral Resistance CGS (dyn.s/cm5)_minute_1", "Time (s)_minute_1"
   :widths: auto

   "Participant 1234", 99.26470588235294, 61.88235294117647, 75.61764705882354, 76.66176470588235, 47.26029411764706, 241.83823529411765, 783.1617647058823, 1052.9558823529412, 3.65, 1.030985294117647, 1374.6911764705883, "14:12:00.000", 108.16, 68.42666666666666, 84.02666666666667, 75.77333333333333, 55.34, 294.6, 797.8666666666667, 1103.9733333333334, 4.190666666666667, 1.2168400000000001, 1622.5333333333333, "14:13:00.000"

In the above example you can see that there minute 1 is *appended* to the end of minute 0. In the full output produced by the `minute_by_minute` function there are 41 minutes of data for each participant and so the table is 574 columns wide. 
Hopefully this gives you a sense of what this reshaping does. 

As stated above, the `minute_by_minute_from_folder` function allows you to do a lot of the work we've talked about in one go, and now that we've given a sense of the individual steps we can use this function to do the same thing as above.

.. code-block:: python
   :linenos:

   import fino2py as f2p

   # path to the participant folder
   participant_folder = pl.Path('path/to/parent/folder/participant_folder')

   # ingest the raw hemodynamic data and reshape to 1 minute averages
   reshaped_data = f2p.minute_by_minute_from_folder(participant_folder, '1T', save_csv=True)


We're just capturing the data from a single participant here however, and in most studies we have multiple participants and so we need to be able to reshape the data for all participants, bringing them into a single dataset for analysis and visualisation. 
We can use the `minute_by_minute_from_folder` to do this along with a `list comprehension` to loop through all the subfolders and ingest the data for each participant.

.. code-block:: python
   :linenos:

   import fino2py as f2p
   import warnings

   # Turning off pandas dpereciation warnings (for now)
   warnings.filterwarnings('ignore')

   frame_list = []  # List to store the dataframes

   for i in data_dir.iterdir():
      if i.is_dir():
         try: 
               minute_frame, _ = f2p.minute_by_minute_from_folder(i, save_raw=True, save=True)
               frame_list.append(minute_frame)
               print(f'Processed {i.name}')
         except:
               print(f'Failed to process {i.name}')

   # Concatenate the dataframes in the list
   minute_by_minute = pd.concat(frame_list, axis=0, ignore_index=True)

Congratulations! You've completed the quick start guide for using the `fino2py` package. This example project covered installing the package, loading, ingesting, cleaning, reshaping, and visualizing Finapress finometer data.

Explore the `fino2py` documentation further to learn about advanced features and functionalities for comprehensive analysis.

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
