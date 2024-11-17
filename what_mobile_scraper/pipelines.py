'''
    Define your item pipelines here
'''
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import json
from itemadapter import ItemAdapter
from prettytable import PrettyTable

class WhatMobileScraperPipeline:
    '''
        This class is used to print the scraped data in a table.
    '''
    def __init__(self):
        '''
            This function is called when the spider is opened.
        '''
        self.table = PrettyTable()
        self.table.field_names = ["Sr. No", "Name", "Price"]
        self.counter = 1
        self.details = []
        self.data = []

    def process_item(self, item, spider):
        '''
            This function is called for every item pipeline component.
        '''
        if spider.name != "whatspider":
            print("Pipeline not configured for this spider")

        adapter = ItemAdapter(item)

        self.data.append({
            "Sr. No": self.counter,
            "Name": adapter.get("name", ""),
            "Price": adapter.get("price", ""),
            "Details URL": adapter.get("details_url", "")
        })

        # Add a row to the table
        self.table.add_row([self.counter, adapter.get("name", ""), adapter.get("price", "")])
        self.counter += 1
        self.details.append(adapter.get("details", ""))

        return item

    def close_spider(self, spider):
        '''
            This function is called when the spider is closed.
            It prints the table and prompts the user to view additional details.
        '''
        if spider.name != "whatspider":
            print("Pipeline not configured for this spider")

        # Save data to JSON file
        with open('output.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, indent=4)

        # Save data to CSV file
        with open('output.csv', 'w', newline='', encoding='utf=8') as csv_file:
            fieldnames = ["Sr. No", "Name", "Price", "Details URL"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for row in self.data:
                writer.writerow(row)
        additonal_details = []
        for detail in self.details:
            if detail is not None:
                additonal_details.append(detail)
        # Save additional details to JSON file (for debugging purposes)
        with open('details.json', 'w', encoding='utf-8') as json_file:
            json.dump(additonal_details, json_file, indent=4)

        while True:
            print("\n\n\nPress enter to continue or 0 to stop: ", end="")
            if input() == "0":
                break

            print(self.table)
            sr_no = int(input("Enter Sr. No for additional details or 0 to stop: "))

            if sr_no == 0:
                break

            # Fetch and print additional details based on Sr. No
            try:
                if 1 <= sr_no <= len(self.details):
                    if self.details[sr_no - 1] is not None:
                        print("\n\n\nAdditional details (",\
                                self.details[sr_no - 1]["name"]['Name'], ")\n")
                        for section, section_details in self.details[sr_no - 1].items():
                            print(f"{section}:")
                            for sub_heading, value in section_details.items():
                                print(f"\t{sub_heading}: {value}")
                            print()
                    else:
                        print("No additional details available")
                else:
                    print("Invalid Sr. No")
            except ValueError:
                print("Invalid Sr. No")

        print("Goodbye!")
