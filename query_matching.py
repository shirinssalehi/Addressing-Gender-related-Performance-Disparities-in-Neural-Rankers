import json
import random
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

with open("./data/scores/scores_train_set_bm25.json", 'r') as scores_ance:
    bm25_scores = json.load(scores_ance)

female_scores = bm25_scores["female"]
male_scores = bm25_scores["male"]
neutral_scores = bm25_scores["neutral"]

female_df = pd.DataFrame(female_scores)
# shuffle the dataframe
female_df = female_df.sample(n=20000)
female_df_sorted = female_df.sort_values(by="score")
female_df_sorted["row_number"] = range(len(female_df_sorted.index))

male_df = pd.DataFrame(male_scores)
# shuffle the dataframe
male_df = male_df.sample(n=20000)
male_df_sorted = male_df.sort_values(by="score")
male_df_sorted["row_number"] = range(len(male_df_sorted.index))

neutral_df = pd.DataFrame(neutral_scores)
# shuffle the dataframe
neutral_df = neutral_df.sample(n=20000)
neutral_df_sorted = neutral_df.sort_values(by="score")
neutral_df_sorted["row_number"] = range(len(neutral_df_sorted.index))

sample_male = male_df_sorted["score"].tolist()[3500:17500]
sample_female = female_df_sorted["score"].tolist()[3500:17500]
sample_neutral = neutral_df_sorted["score"].tolist()[3500:17500]
# male_slots = np.linspace(min(sample_male), max(sample_male), num=10)
# slots = np.linspace(min(sample_female), max(sample_female), num=10)
slots = np.linspace(min(sample_male), max(sample_male), num=10)

print("min and max of sample_male are {} and {}".format(min(sample_male), max(sample_male)))
print("min and max of sample_female are {} and {}".format(min(sample_female), max(sample_female)))
numbers_female = []
numbers_male = []
selected_female_df = female_df_sorted.loc[(female_df_sorted["row_number"] >= 3500) & (female_df_sorted["row_number"] <17500) ]
selected_male_df = male_df_sorted.loc[(male_df_sorted["row_number"] > 3500) & (male_df_sorted["row_number"] <17500) ]

# final_male_df = pd.DataFrame()
# final_female_df = pd.DataFrame()
male_df_list = []
mmm = 0
for idx, i in enumerate(range(9)):
    # selected_bin = female_df.filter(female_df.score.between(female_slots[i],female_slots[i+1]))
    selected_bin_female = selected_female_df.loc[(slots[i] <= selected_female_df["score"]) & (selected_female_df["score"] < slots[i+1])]
    n_female = len(selected_bin_female.index)
    selected_bin_male = selected_male_df.loc[(slots[i] <= selected_male_df["score"]) & (selected_male_df["score"] < slots[i + 1])]
    n_male = len(selected_bin_male.index)
    total_number = min(n_male, n_female)
    mmm += total_number
    final_female_df = selected_bin_female.sample(n=total_number)
    final_male_df = selected_bin_male.sample(n=total_number)
    # final_male_df.to_csv("./data/final_male_df_{}.csv".format(idx), index=False)
    # final_female_df.to_csv("./data/final_female_df_{}.csv".format(idx), index=False)
print(mmm)




# plt.plot(numbers_female)
# plt.plot(numbers_male)
# plt.legend(['female', 'male'])
# plt.show()
# plt.hist(sample_female, bins=10, alpha=0.8)
# plt.hist(sample_male["score"], bins=10, alpha=0.5)
# fem_score = female_scores["score"][5:20000]
# fem_score = sorted(fem_score)
#
# random.shuffle(male_scores["score"])
# m_score = male_scores["score"][5:20000]
# m_score = sorted(m_score)
#
# random.shuffle(neutral_scores["score"])
# neutral_score = neutral_scores["score"][5:20000]
# neutral_score = sorted(neutral_score)
#
# selected_female = fem_score[3500:17500]
# selected_male = m_score[3500:17500]
# selected_neutral = neutral_score[3500:17500]
#
#
#
# plt.plot(sample_male)
# plt.plot(sample_female)
# plt.plot(sample_neutral)
# # plt.plot(m_score[3500:17500])
# # plt.plot(neutral_score[3500:17500])
# plt.legend(['male', 'female', 'neutral'])
# plt.legend(['female', 'male'])
# plt.show()