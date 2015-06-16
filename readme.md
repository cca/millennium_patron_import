# Bulk Import Patron Data into Millennium ILS

CCA's outline of adding new patrons before the semester:

- Run Informer report to get new student list in CSV format
- Use "csv2patron-marc.py" to convert the CSV into a MARC-like format
- Load, prep, & finally import the resulting file in Millennium

## Details

Run Informer Report "LIB-EP New Students for ILS Import" & set the Start Term to the upcoming semester. In the CSV export, ensure **Columns Headers** is checked & that the **Multivalue Handler** is "List by comma". Then, on the command line, navigate to the directory with the "csv2patron-marc.py" script on it & run:

```
python csv2patron-marc.py -o output.txt -e 12-25-14 input.csv F
```

Where _output.txt_ is the name of the file you want created, _12-25-14_ is the expiration date for the created patron records, _input.csv_ is the Informer report used as input, & _F_ is the shortened form of the semester's season (one of F, sp, or Su). All of this information is contained in the help flag of csv2patron-marc.py; run `python csv2patron-marc.py -h`. If your file names have spaces in them, you can wrap them in quotation marks.

Inside Millennium Circulation, select the Data Exchange section & then Select Process "Load MARC Patron records from tape or FTS (pta)". Click **Get PC** to browse your hard drive for the import file & **choose the "ptfs" extension** (important!).

Highlight the newly loaded file & choose Tools > Prep > "PREPROCESS TEXT Patron records loaded via FTS", then click **Start**. A brief message appears as Millennium processes the records & when you close the dialog there will be a ".pat" file listed. Select the .pat, then Tools > Load > Load a MARC file (or just click **Load** in the upper right). Here you can first **Test** the MARC file, which provides warnings about improper PCODEs & such. Then, if the test is successful, hit **Load** to import the patron records.

## Overlaying Records

These are settings you can specify with Innovative. Below are the details of CCA specific setup.

Records are overlaid based on the "UNIV ID" (`u`) field. The logic is as such:

- If no patron record with the same `u` exists, create a new record
- If a patron record with the same `u` exists, all fields in the old record are discarded & new data from import inserted but associated data like checkouts & fines persist
- If 2 patrons with the same `u` exist, create a new (now 3rd) record. Note that this is theoretically impossible as `u` fields are unique.

## Testing

Included is a sample CSV export from Informer which can be used for test runs.

In CCA's Millennium, the "Test Import Patrons" review file can delete these records after testing. If that review file was overwritten, it's simply:

```sql
PATRON  PATRN NAME  starts with  "ZTEST"
```

## Customizing Further

CCA does not currently use several of the fixed-length fields in a patron record, such as "Home Library". Extending the current script to handle these isn't hard:

- Add a dict in mapping.py where CSV value keys are matched with patron record values, e.g. `homelib = { 'LoC': '00001'… }`
- Import the dict on the `from mapping import…` line
- In the appropriate place of the `for row in csv` loop, mimic the existing procedure for PTYPE & PCODE3—e.g. `if row['Home Library'] in homelib…`—putting your default value in the `else` clause

## Links & Documentation

Relevant manual pages:
- 101688 "Loading Patron Records" (load tables)
- 101871 "Edit overlay protection list"
- 106003 "Preprocessing Files for Import in Data Exchange"
- 106004 "Loading Records in Data Exchange"
- 107503 "Importing Patron Data"
- http://gsm.iii.com/data2_6.html
- http://gsm.iii.com/data3_1.html

# LICENSE

[Apache Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
