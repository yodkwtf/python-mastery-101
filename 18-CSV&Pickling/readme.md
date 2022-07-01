## CSV

- Comma Separated Values
- Common for tabular data

We use specific csv module to read/write csv files in a decent way

## Reading CSV Files

#### 2 Different Ways

- **reader** - iterates over rows of CSV as lists
- **DictReader** - iterates over rows of CSV as OrderedDicts

_reader_ is an iterator

**Note**: We can read data from csv files even if they are not separated by commas, as long as they are separated by the same character. That character is knows as _Delimiter_.

## Writing CSV Files

- **writer** - creates a writer object for writing to CSV
- **writerow** - method on a writer to write a row to the CSV

## Pickling

We can pickle some data by putting it into a specific pickle file using the pickle module.

Python serialize the data and converts into byte streams and later when we need the data we can unpickle it and convert it back to what it was.
