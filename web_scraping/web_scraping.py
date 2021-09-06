import csv
import json
import requests
from bs4 import BeautifulSoup


def get_district_links():
    result = []
    URL = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    URL_root = "https://volby.cz/pls/ps2017nss/"
    resp = requests.get(URL)
    resp = BeautifulSoup(resp.content)
    for tr in resp.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) >= 3:
            result.append({
                "district_url": URL_root + tds[0].find_all("a")[0]["href"],
                "district_name": tds[1].get_text(),
                "district_num": tds[0].get_text()
            })
    return result


def get_district_details(district_info):
    print(f"Parsing: {district_info['district_url']}")
    resp = requests.get(district_info["district_url"])
    resp = BeautifulSoup(resp.content)
    # ...
    table_one = resp.findAll("table",{"id":True})
    assert len(table_one) == 1
    table_one = table_one[0]
    tables_two = resp.findAll("table", {"summary": True})
    assert len(tables_two) == 2

    voters_in_list = table_one.find_all("td", {"headers": "sa2"})
    voters_in_list = int(voters_in_list[0].get_text().replace("\xa0", ""))
    district_info["voters_in_list"] = voters_in_list

    issued_envelopes = table_one.find_all("td", {"headers": "sa3"})
    issued_envelopes = int(issued_envelopes[0].get_text().replace("\xa0", ""))
    district_info["issued_envelopes"] = issued_envelopes

    valid_votes = table_one.find_all("td", {"headers": "sa6"})
    valid_votes = int(valid_votes[0].get_text().replace("\xa0", ""))
    district_info["valid_votes"] = valid_votes

    parties = []
    for table in tables_two:
        for row in table.find_all("tr")[1:]:
            cells = row.find_all("td")
            if len(cells) > 0:
                parties.append(cells[1].get_text())

    district_info["parties"] = parties
    return district_info

def parse_data(data):
    result = []
    row = {
        "code of the district":"",
        "name od the district":"",
        "voters in list":"",
        "issued envelopes":"",
        "valid votes":"",
        "parties":"",
        "debug":data
    }
    with open('votes.csv', mode='w') as csv_file:
        fieldnames = [
        "code of the district",
        "name od the district",
        "voters in list",
        "issued envelopes",
        "valid votes",
        "parties",
        "debug"
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({  "code of the district":"",
        "name od the district":"",
        "voters in list":"",
        "issued envelopes":"",
        "valid votes":"",
        "parties":"",
        "debug":data
        })
    result.append(data)
    return result

def main():
    districts = get_district_links()
    for district in districts:
        data = get_district_details(district)
    print(json.dumps(districts, indent=4))
    dict(data)

if __name__ == "__main__":
    main()





