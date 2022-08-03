from model import Model
import pandas as pd

class Matcher():
    def __init__(self,bio) -> None:
        self.main_df = pd.read_csv("/home/nibuntu/code/yourpandaboy/ViV/ViV_backend/df_final_cleaned.csv")
        self.model = Model()
        self.bio = bio

    def user_topic(self, bio = None):
        if bio is not None:
            self.bio = bio
        output = self.model.predict(self.bio)
        df = pd.DataFrame(output,columns=["Dominant_No","Score"])
        df["Dominant_No"] = df["Dominant_No"].apply(lambda x: x+1)
        df.sort_values(by = 'Score' , ascending = False , inplace =True)
        self.topics = df[:4]
        return self.topics

    def output_matches(self):

        topic_df = self.user_topic()

        topics = topic_df['Dominant_No']


        filtered_df = self.main_df[self.main_df['Dominant_Topic'].isin(topics)]
        return filtered_df

    def top_10_matches(self):
        #return the top ten best matches from theoutput matches
        pass

if __name__ == '__main__':
    temp_matcher = Matcher(bio= 'hey looking for friends here. male or female preferably people who likes to travel and outdoor activities.')
    print(temp_matcher.output_matches())
