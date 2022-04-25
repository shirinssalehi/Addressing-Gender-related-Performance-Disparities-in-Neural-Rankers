import json
import random
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

female_train = pd.read_csv("./data/doct5/bm25_scores_female_train.tsv", sep="\t")
male_train = pd.read_csv("./data/doct5/bm25_scores_male_train.tsv", sep="\t")
# final_male_df = pd.DataFrame()
# final_female_df = pd.DataFrame()
mmm = 0
slots = np.linspace(min(male_train["score"].tolist()), max(male_train["score"].tolist()), num=10)
for idx, i in enumerate(range(9)):
    # selected_bin = female_df.filter(female_df.score.between(female_slots[i],female_slots[i+1]))
    selected_bin_female = female_train.loc[(slots[i] <= female_train["score"]) & (female_train["score"] < slots[i+1])]
    n_female = len(selected_bin_female.index)
    selected_bin_male = male_train.loc[(slots[i] <= male_train["score"]) & (male_train["score"] < slots[i + 1])]
    n_male = len(selected_bin_male.index)
    total_number = n_male - n_female
    print("We need {} samples in the range of {} and {}".format(total_number, slots[i], slots[i+1]))
    mmm += total_number
    final_female_df = selected_bin_female.sample(n=total_number)
    final_male_df = selected_bin_male.sample(n=total_number)
    final_male_df.to_csv("./data/final_male_df_{}.csv".format(idx), index=False)
    final_female_df.to_csv("./data/final_female_df_{}.csv".format(idx), index=False)
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