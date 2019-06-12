    
# omniparser/gradebook_parser.py

import json
import os
import statistics

import pandas

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath) #df is a dataframe structure that is from the pandas package. We define the variable 
    #as df, similarly we could have named it anything.

    rows = df.to_dict("records") #converting df variable from a dataframe structure to a dictionary function
        #df. you have to use the same variable name you defined above
        #similarly rows is a variable that we could have named anything.

        #alternatively we could do
        # grades = df["final_grade"].to_list()

    grades = [r["final_grade"] for r in rows] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5]

    #alternatively and most condense:  avg_grade = df["final_grade"].mean()

    avg_grade = statistics.mean(grades)

    return avg_grade #90.64 #"OOPS"

def calculate_average_grade_from_json(x):
    with open(x, "r") as f: #with is a python function | "r" means read, "w" means write. there are other options too
        print(type(f))
        file_contents = f.read()
        print(type(file_contents)) #> str

    gradebook = json.loads(file_contents)

    print(type(gradebook))
    print(gradebook)

    return 10000



if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv") #__file__ is the current file path and the rest is the relative file path
        #.. moves up the file path
        #its important to know where you are working when creating the file path

    avg = calculate_average_grade_from_csv(gradebook_filepath)
    print(avg)

    print("PARSING SOME JSON EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.json") #__file__ is the current file path and the rest is the relative file path
        #.. moves up the file path
        #its important to know where you are working when creating the file path

    avg = calculate_average_grade_from_json(gradebook_filepath)
    print(avg)