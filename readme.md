Outline of adding new patrons before the semester:

- Run an Informer report to get new student list in CSV format
- Use "csv2patron-marc.py" to convert the CSV into a MARC-like format
- Load, prep, & finally import the resulting file in Millennium

#### Details

Run Informer Report "LIB-EP New Students for ILS Import" and set the Start Term to the upcoming semester. In the CSV export, ensure that Columns Headers is checked (NB: multivalue handler?). Then, on the command line, navigate to the directory with the "csv2patron-marc.py" script on it and run:

```
python csv2patron-marc.py -o output.txt -e 12-12-14 input.csv F
```

Where _output.txt_ is the name of the file you want created, _12-12-14_ is the expiration date for the created patron records, _input.csv_ is the Informer report used as input, and _F_ is the shortened form of the semester's season (one of F, sp, or Su). All of this information is contained in the help flag of csv2patron-marc.py; run `python csv2patron-marc.py -h`. If your file names have spaces in them, you can wrap them in quotation marks.

Inside Millennium Circulation, select the Data Exchange section and then Select Process "Load MARC Patron records from tape or FTS (pta)". Click **Get PC** to browse your hard drive for the import file and choose the "ptfs" extension.

Highlight the newly loaded file and choose Tools > Prep > "PREPROCESS TEXT Patron records loaded via FTS", then click **Start**. A brief message appears as Millennium processes the records and when you close the dialog there will be a ".pat" file listed. Select the .pat, then Tools > Load > Load a MARC file (or just click **Load** in the upper right). Here you can first **Test** the MARC file, which provides warnings about improper PCODEs and such. Then, if the test is successful, hit **Load** to import the patron records.

#### Customizing Further

We do not currently use several of the fixed-length fields in a patron record, such as "Home Library". Extending the current script to handle these should be simple:

- Add a dict in mapping.py where CSV value keys are matched with patron record values, e.g. `homelib = { 'LoC': '00001'… }`
- Import the dict on the `from mapping import…` line
- In the appropriate place of the `for row in csv` loop, mimic the existing procedure for PTYPE & PCODE3—e.g. `if row['Home Library'] in homelib…`—putting your default value in the `else` clause

#### Links & Documentation

Relevant manual pages: 
101688 "Loading Patron Records" (load tables)
101871 "Edit overlay protection list"
106003 "Preprocessing Files for Import in Data Exchange"
106004 "Loading Records in Data Exchange"
107503 "Importing Patron Data"
http://gsm.iii.com/data2_6.html
http://gsm.iii.com/data3_1.html
