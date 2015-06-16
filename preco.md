# Pre-college

Documentation for pre-college imports.

Process:

- run **LIB-EP New Students for ILS Import** with a Starting Term like "2015pc"
- set expiry to first Monday after PC term, mid-July-ish
- patron type is `008` ("Special")—probably easiest to just edit the P TYPE default to be `output.write('008')` instead of blanks
- note field is like 'PC15'

So an example command:

```
> python csv2patron-marc.py -o data/2015-preco.ptfs -e 2015-07-13 data/2015-preco.csv PC
```
