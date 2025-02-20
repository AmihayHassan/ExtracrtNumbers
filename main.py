import os
from collections import Counter

import pandas as pd
from bs4 import BeautifulSoup

PATH = r"call_history.xml"
NUMBERS_COL = "Phone Numbers"
FREQUENCY_COL = "Frequency"
OUTPUT_FOLDER = "output"

if not os.path.exists(path=OUTPUT_FOLDER):
    os.makedirs(name=OUTPUT_FOLDER)


def extract_datum_tags(soup: BeautifulSoup):
    return (
        (
            soup
            .find(name="AllInOneBackup")
            .find(name="Data")
        )
        .find_all(name="Datum")
    )


def extract_phone_numbers(data_tags):
    all_numbers = []

    for data_tag in data_tags:
        # get the PhoneNumber tag in it and extract the text
        phone_number = data_tag.find(name="PhoneNumber").text

        # append the phone number to the list
        all_numbers.append(phone_number)

    # count the frequency of each phone number
    all_numbers_counter = Counter(all_numbers)

    # sort the phone numbers based on their frequency
    all_numbers_counter = dict(sorted(all_numbers_counter.items(), key=lambda x: x[1], reverse=True))

    # get the unique phone numbers
    all_numbers = list(all_numbers_counter.keys())

    return all_numbers, all_numbers_counter


def main():
    with open(file=PATH, mode="r", encoding="utf-8") as file:
        content = file.read()

    soup = BeautifulSoup(markup=content, features="xml")

    data_tags = extract_datum_tags(soup=soup)

    all_numbers, counter = extract_phone_numbers(data_tags=data_tags)

    df_with_frequencies = pd.DataFrame(data=counter.items(), columns=[NUMBERS_COL, FREQUENCY_COL])
    df_with_frequencies = df_with_frequencies[df_with_frequencies[NUMBERS_COL] != ""]
    df_with_frequencies.to_excel(excel_writer=os.path.join(OUTPUT_FOLDER, "phone_numbers_freq.xlsx"),
                                 engine="xlsxwriter",
                                 index=False)

    clean_df = pd.DataFrame(data=all_numbers, columns=[NUMBERS_COL])
    clean_df = clean_df[clean_df[NUMBERS_COL] != ""]
    clean_df.to_excel(excel_writer=os.path.join(OUTPUT_FOLDER, "phone_numbers.xlsx"),
                      engine="xlsxwriter",
                      index=False)


if __name__ == "__main__":
    main()
