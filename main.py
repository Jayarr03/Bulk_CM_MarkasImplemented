import pandas as pd

data = pd.read_excel(r'C:\Users\jrabe_iriusrisk\PycharmProjects\bulk_rule_creator\xml_builder.xlsx')

counter = 0  # starting the counter at 0 ensures that the final output matches the expected qty of created rules

output = ""  # Initialize an empty string to hold the XML content

for index, row in data.iterrows():
    counter += 1

    rule_name = str(row['rule_name'])
    module = str(row['module'])
    cond1_name = str(row['cond1_name'])
    field1 = str(row['field1'])
    value1 = str(row['value1'])
    cond2_name = str(row['cond2_name'])
    field2 = str(row['field2'])
    value2 = str(row['value2'])
    project = str(row['project'])
    cm_value = str(row['cm_value'])
    cm_status = str(row['cm_status'])
    overide = str(row['overide']).lower()  # converts this value to all lowercase

    rule_xml = (f"<rule name= '{rule_name}' module= '{module}' generatedByGui= 'true'>\n"
                "  <conditions>\n"
                f"    <condition name='{cond1_name}' field='{field1}' value='{value1}'/>\n"
                f"    <condition name='{cond2_name}' field='{field2}' value='{value2}'/>\n"
                "  </conditions>\n"
                "  <actions>\n"
                f"    <action project='{project}' value='{cm_value}_::_{cm_status}_::__::_{overide}' name='MARK_CONTROL_AS'/>\n"
                "  </actions>\n"
                "</rule>\n")

    output += rule_xml

file_path = r"C:\Users\jrabe_iriusrisk\PycharmProjects\bulk_rule_creator\output.txt"

with open(file_path, "w") as f:
    f.write(output)

print("Output written to:", file_path)
print(counter, "Rules Created\n")