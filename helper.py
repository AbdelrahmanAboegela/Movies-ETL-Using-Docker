import os
import pandas as pd

class local_storage:
    
    def __init__(self):
        pass

    def process_ratings(self, file_path='ml-100k/u.data'):
        '''
        Create Dataframe of movie ratings from the file u.data.

        Args:
            - file_path(str) - Path to u.data.

        Returns:
            - ratings(DataFrame)
        '''
        ratings = pd.read_csv(file_path, delimiter='\t', header=None, names=['user_id', 'item_id', 'rating', 'timestamp'])
        return ratings

    def process_movies(self, file_path='ml-100k/u.item'):
        '''
        Create Dataframe of movie names from the file u.item.

        Args:
            - file_path(str) - Path to u.item.

        Returns:
            - movies_df(DataFrame)
        '''
        with open(file_path, 'r', encoding="ISO-8859-1") as read_file:
            movies_df = pd.DataFrame(columns=['item_id', 'movie_name', 'release_timestamp'])
            for line in read_file:
                fields = line.split('|')
                item_id, movie_name, release_timestamp = fields[0], fields[1], fields[2]
                movie_name = movie_name[0:len(movie_name) - len(' (1234)')]
                line_data = [int(item_id), str(movie_name), release_timestamp]
                temp_df = pd.DataFrame(data=[line_data], columns=['item_id', 'movie_name', 'release_timestamp'])
                movies_df = pd.concat([temp_df, movies_df], ignore_index=True)
            movies_df.sort_values(by='item_id', ascending=True, inplace=True)
        return movies_df

    def export_dataframe_to_csv(self, dataframe, csv_name):
        '''
        Export DataFrame to CSV.

        Args:
            - dataframe(Pandas.DataFrame) = Name of the DataFrame to Export.
            - csv_name(str) = Name of the CSV file
        Returns:
            - None
        '''
        try:
            dataframe.to_csv(csv_name + '.csv', index=False)
        except Exception as e:
            print(e)
