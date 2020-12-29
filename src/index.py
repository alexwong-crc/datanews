# This module comes from datanews: https://datanews.io/docs
# Installed with pip3: https://pypi.org/project/datanews/
# This github page is here: https://github.com/DatanewsOrg/datanews-python
import datanews

# Api key goes here
datanews.api_key = "API_KEY"

# This will get all the articles for all the months in the year 1990
# Will need to make this generic so it will grab all the results for a set amount of years etc
for month in range(1, 13):
    strMonth = str(month)
    if len(strMonth) == 1:
        strMonth = f"0{strMonth}"

    response = datanews.news(
        q="war", language=["en"], from_date="1990-01-01", to_date=f"1990-{strMonth}-01"
    )

    print(f"For month {strMonth}, we had this many searches: {response['numResults']}")


# This grabs all the sources in GB and lists them
# It's paginated to only show 100 per response
response = datanews.sources(size=100, country="gb")
print(response["numResults"])

for source in response["hits"]:
    print(source["url"])

# You can run this file, (will fetch all the sources and the articles) with the command:
# python3 src/index.py
