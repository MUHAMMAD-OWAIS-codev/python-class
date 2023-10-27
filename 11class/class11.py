import pandas as pd
# Pandas mein row name ki cheez nahi hoti hai usmein sirf index hota hai or column alag hota hai
df = pd.read_csv("Data/pokemon_data.csv")
# print(df) # Display all the data in your file
# print(list(df.columns)) # Display all columns of the file
# print(df.head()) # First Five rows print
# print(df.tail()) # last five rows print
# print(df.head(10)) # First ten rows
# print(df.tail(10)) # last ten rows

# print(df.loc[10]) # First value index yaani ke row ki hogi or second value column ki hogi agar sirf ek argument pass karenge to wo usko index suppose karega
# print(df["Name"])
# print(len(df.loc[: , "Type 1"]))
# Multiple rows print karwani hon to yeh karenge hum
# print(df.loc[[10, 15],['Name', "Type 1"]])

# new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Flying")] # Ye round bracket bohat zyada important hain agar ye nahi lagaenge to ye koi error nahi dega magar koi  data bhi nahi dikhaye ga
# print(new_df.loc[:, ["Type 1", "Type 2"]])

# valid_categories = ["Grass", "Fire"]
# new_df = df[~df["Type 1"].isin(valid_categories)] #agr is condition ko false karna hai to ~ sign lagaeynge
# print(new_df)

# new_df = df.loc[df["Name"].str.contains("Mega")]
# print(new_df)

# print(df.shape) #Print Rows and columns of the file
# Axis = 0 (row) and Axis = 1 (column)

# df.sort_index(axis=1, ascending=True, inplace=True) # This will sort index according to ascending order and inplace is used to change in the original value to optimize memory consumption but this will not sort oura data values it will only sort columns or rows
# print(list(df.columns))

# df.sort_values(by=["Name"], ascending=True, inplace=True)
# print(df["Name"].head())