from helper import local_storage

# Create an instance of class: local_storage
local = local_storage()

# Process the ratings and movies files into DataFrames
ratings = local.process_ratings()
movies = local.process_movies()


# Export DataFrames to CSV in the 'results' directory
local.export_dataframe_to_csv(dataframe=ratings, csv_name='results/ratings')
local.export_dataframe_to_csv(dataframe=movies, csv_name='results/movies')