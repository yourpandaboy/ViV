from ViV_backend.model import Model
import pandas as pd

class Matcher():
    def __init__(self,bio,redownloadmodel=False) -> None:
        self.main_df = pd.read_csv("data/df_final_cleaned.csv")
        self.model = Model(redownloadmodel)
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

        self.filtered_df = self.main_df[self.main_df['Dominant_Topic'].isin(topics)]
        return self.filtered_df

    def top_matches(self):
        #return the top ten best matches from theoutput matches
        matches_df = self.output_matches()
        new_user_df = self. user_topic()
        topics = new_user_df['Dominant_No']
        bounds = new_user_df['Score']

        dfs = []
        for topic, bound in zip(topics, bounds):
            df = matches_df[matches_df['Dominant_Topic']==topic][(matches_df['Topic_Perc_Contrib'] >= bound*.95) & (matches_df['Topic_Perc_Contrib'] <= bound*1.05)]
            dfs.append(df)
        best_matches = self.best_matches = pd.concat(dfs)
        return best_matches

if __name__ == '__main__':
    temp_matcher = Matcher(bio= 'looking for someone to scroll endlessly through netflix. Or to yell out songs at the nearest karaoke. I enjoy cooking, travelling, singing, karaoke, gaming.')
    print(temp_matcher.top_matches())
