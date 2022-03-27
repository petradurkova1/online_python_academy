import csv
import json
import argparse
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
    tables_two = resp.findAll("table", {"id": False})
    print(len(tables_two))
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

def parse_data(data,filename_csv):
    result = []
    for d in data:
        row = {
            "code of the district": d["district_num"],
            "name od the district": d["district_name"],
            "voters in list": d["voters_in_list"],
            "issued envelopes": d["issued_envelopes"],
            "valid votes": d["valid_votes"],
            "parties": d["parties"]
        }
        result.append(row)
    with open(filename_csv, mode='w') as csv_file:
        fieldnames = [
        "code of the district",
        "name od the district",
        "voters in list",
        "issued envelopes",
        "valid votes",
        "parties"
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for d in result:
            writer.writerow({
                "code of the district": d["code of the district"],
                "name od the district": d["name od the district"],
                "voters in list": d["voters in list"],
                "issued envelopes": d["issued envelopes"],
                "valid votes": d["valid votes"],
                "parties": ";".join(d["parties"])   
            })
    return result

def main():
    parser = argparse.ArgumentParser(description='Votes')
    parser.add_argument('--verbose',
                        action='store_true',
                        help='verbose flag')

    parser.add_argument("chosen_district")
    parser.add_argument("filename_csv")

    args = parser.parse_args()
    print(args)

    districts = get_district_links()
    districts_details = []
    for district in districts:
        if args.chosen_district == district["district_num"]:
            districts_details.append(get_district_details(district))
    print(json.dumps(districts, indent=4))
    test = parse_data(districts_details,args.filename_csv)

if __name__ == "__main__":
    main()





