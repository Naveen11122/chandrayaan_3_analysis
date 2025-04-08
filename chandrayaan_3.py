import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("D:\Data set Part 2 - propulsion_module.csv")
print(df)
print (df.head())
data={
    "Parameter":[
        "Lunar Polar Orbit",
        "Mission life",
        "Structure",
        "Dry Mass",
        "Propellant Mass",
        "Total PM Mass",
        "Power Generation",
        "Communication",
        "Attitude Sensors",
        "Propulasion System"
    ],
    "Specifications":[
        " From 170 x 36500 km to lunar polar orbit",
        "Carrying Lander Module & Rover upto ~100 x 100 km launch injection.",
        "Modified version of I-3 K",
        "448.62 kg (including pressurant)",
        "1696.39 kg",
        "2145.01 kg",
        "738 W, Summer solistices and with bias",
        "S-Band Transponder (TTC) â€“ with IDSN",
        "CASS, IRAP, Micro star sensor",
        "Bi-Propellant Propulsion System (MMH + MON3)"
    ]
}
df=pd.DataFrame(data)
print(df)

data={
    "Parameter":[
        "Mission life",
        "Mass",
        "Power",
        "Payloads",
        "Dimensions (mm3)",
        "Communication",
        "Landing site"
    ],
    "Specifications":[
        "1 Lunar day (14 Earth days)",
        "1749.86 kg including Rover",
        "738 W (Winter solstice)",
        "3",
        "2000 x 2000 x 1166",
        "ISDN, Ch-2 Orbiter, Rover",
        "69.367621 S, 32.348126 E"
    ]
}

lander_df=pd.DataFrame(data)
print(lander_df)

data={
    "Parameter":[
        "Mission life",
        "Mass",
        "Power",
        "Payloads",
        "Dimensions (mm3)",
        "Communication"
    ],
    "Specifications":[
        "1 Lunar day",
        "26 kg",
        "50 W",
        "2",
        "917 x 750 x 397",
        "Lander"
    ]
}
rover_df=pd.DataFrame(data)
print(rover_df)

import re
def extract_numerical_value(spec):
    numeric_pattren=r'(\d+(\.\d+)?)'
    custom_numeric_pattern=r"[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?"
    combined_pattern=f"({numeric_pattren}|{custom_numeric_pattern})"
    matches=re.findall(combined_pattern,spec)

    if matches:
        return float(matches[0][0])
    else:
        return None

df["numerical values"] = df["Specifications"].apply(extract_numerical_value)
print(df)
lander_df["numerical values"] = lander_df["Specifications"].apply(extract_numerical_value)
print(lander_df)
rover_df["numerical values"] = rover_df["Specifications"].apply(extract_numerical_value)
print(rover_df)

import math
rover_mass=26
lander_dry_mass=1749.86
total_mass=rover_mass+lander_dry_mass
delta_v_required=1500
ips_lander_engine=300
propellant_ass_required=total_mass*math.exp(delta_v_required/ips_lander_engine)- total_mass
propellant_ass_required=round(propellant_ass_required,2)

rover_power_requirement=50
lander_battery_capacity=2000

rover_operating_time_hourse=lander_battery_capacity/rover_power_requirement

print("Mass Budegt")
print(f"Lander mass{lander_dry_mass} kg")
print(f"rover mass:{rover_mass}kg")
print(f"propelent mass required: {propellant_ass_required} kg (matchs values in lander)")

print("\npower Budget:")
print(f"Rover Power requrement:{rover_power_requirement} w")
print(f"Lander battery capacity:{lander_battery_capacity}")
print(f"Rover can operate for {rover_operating_time_hourse:.2f} hours on stored power")


print("\nMobility Assessment:")
print("Low mass of the rover allows for mobility on unever lunar surface")
print("Number of payloads for science masurements is 2")

# visulysation
mass_labels=['Lander Dry Mass', 'Rover Mass','Propellant Mass']
mass_values=[lander_dry_mass,rover_mass,propellant_ass_required]
# plt.figure(figsize=(8,6))
# plt.bar(mass_labels,mass_values,color=['blue','pink','red'])
# plt.xlabel('components')
# plt.ylabel('Mass (kg)')
# plt.title('Mass Budget')
# plt.ylim(0,max(mass_values)*1.2)

# for i,v in enumerate(mass_values):
#     plt.text(i,v,str(v),ha='center', va='bottom')
# plt.show()


labels=['ROver Power Requriment','Lander Battry Capacity']
power_values=[rover_power_requirement,lander_battery_capacity]
# plt.figure(figsize=(8,6))
# plt.bar(labels,power_values,color=['blue','pink','red'])
# plt.xlabel('components')
# plt.ylabel('power (wall-hours)')
# plt.title('Power Budget')
# plt.ylim(0,max(power_values)*1.2)

# for i,v in enumerate(power_values):
#     plt.text(i,v,str(v),ha='center', va='bottom')
# plt.show()

# plt.figure(figsize=(20,20))
# plt.pie(mass_values,labels=mass_labels,autopct="%1.1f%%",startangle=140)
# plt.title("mass budget")
# plt.axis('equal')
# plt.show()


plt.figure(figsize=(20,20))
plt.pie(power_values,labels=labels,autopct="%1.1f%%",startangle=140)
plt.title("mass budget")
plt.axis('equal')
plt.show()

