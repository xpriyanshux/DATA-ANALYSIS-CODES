import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Check text presence in the XML content
def check_text_presence(xml_content, search_text):
    try:
        root = ET.fromstring(xml_content)

        if search_text in ET.tostring(root).decode():
            return "Yes"
        else:
            return "No"
    except ET.ParseError:
        return "Invalid XML content"

# Process Pubchem IDs in Excel file
def process_pubchem_ids(df, output_column):
    pubchem_ids = df['PubChem ID']

    results = []
    for pubchem_id in pubchem_ids:
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{pubchem_id}/XML/?response_type=display"

        response = requests.get(url)
        if response.status_code == 200:
            xml_content = response.content.decode('ISO-8859-1')  # Decode using ISO-8859-1
            result = check_text_presence(xml_content, "DrugBank")
            results.append(result)
        else:
            results.append("Failed to download")

    df[output_column] = results
    return df

# Example usage
input_file = "C:/Users/priya/OneDrive/Desktop/trial.xlsx"
output_column = "TextPresence"

df = pd.read_excel(input_file)
df = process_pubchem_ids(df, output_column)
df.to_excel(input_file, index=False)
print(f"Results updated in the input file: {input_file}")
