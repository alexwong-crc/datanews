# POC for using datanews api

In the src folder, we have a basic script that will execute the /source and /news endpoint for the datanews api.

You can find more information on the [datanews documentation](https://datanews.io/docs)

You can run the script using the command:

```bash
python3 src/index.py
```

The script is a POC so it currently does a for loop over the months in year 1990, and list how many articles are found related to the search term "war". It then looks for all sources that are from GB and lists out the first 100.

### To do

- We need to make the function generic so it will loops through the months of a given time frame.
- We need to make the search term an input
  - Either via the terminal or change it in the script
- We need to specify to search only on specific sources (eg GB sources only)
- We may want to think about how we want to output this.
  - Easiest method: print to console
  - Realistic method: write it to a csv
  - OTT method: look for a graph generating library

### Gotchas

- Datanews has a free tier which we can take advantage of. Currently allows only 3k search requests only.
- Remember to keep your API key secret. Do not commit it to github.

### Additional tools

#### Postman

[Postman](https://www.postman.com/) is a application you can download to test the api. It has a more friendly user interface than using CURL and scripts.
