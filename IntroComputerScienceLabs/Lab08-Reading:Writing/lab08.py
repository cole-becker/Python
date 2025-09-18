import json

# ADD YOUR load_matching_data AND save_summary IMPLEMENTATIONS HERE
# format - {'address': '252  VICTORIA ST ', 'score': 95.0, 'num_stories': 37, 'num_units': 337}
def load_matching_data(min_score, min_stories, min_units):
    matching_data = []
    with open('apartment_building_evaluation.csv', 'r') as input_file:
        for line in input_file:
            data = line.split(',')
            building_address = data[26]
            building_score = float(data[24])
            building_num_stories = int(float(data[2]))
            building_num_units = int(float(data[3]))
            if min_score <= building_score and min_stories <= building_num_stories and min_units <= building_num_units:
                new_building = {
                    'address': building_address,
                    'score': building_score,
                    'num_stories': building_num_stories,
                    'num_units': building_num_units,
                }
                matching_data.append(new_building)
    
    return matching_data

def save_summary(results, output):
    with open(output, 'w') as output_file:
        json.dump(results, output_file)

results = load_matching_data(85, 28, 300)
save_summary(results, 'apartment_summary.json')