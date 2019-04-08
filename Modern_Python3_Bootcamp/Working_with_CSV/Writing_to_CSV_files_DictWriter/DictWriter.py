from csv import DictWriter, DictReader

with open("demo.csv", 'w') as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadouken"})
    

def cm_to_inch(cm):
    return int(cm) * 0.393701

with open("fightersAll.csv", 'r') as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)
    
with open("inches_fighters.csv", 'w') as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            "Name": f["Name"],
            "Country": f["Country"],
            "Height": cm_to_inch(f["Height (in cm)"])
            })
        