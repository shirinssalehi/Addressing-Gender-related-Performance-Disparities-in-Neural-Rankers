from pyserini.index import IndexReader
import pandas as pd

query_doc = pd.read_csv("./data/doct5/selected_male_df.tsv", sep="\t")
# query_doc= query_doc.drop_duplicates(subset="qid")
query_doc = query_doc[["qid", "pid"]]
queries_df = pd.read_csv("./data/doct5/msmarco_train_set_male_queries.tsv", names=["qid", "query"], sep="\t")
index_reader = IndexReader('/home/shirin/gender-performance/indexes/index-msmarco-passage-20201117-f87c94')
scores = []
i = 0
for qid, pid in query_doc.values:
    query_row = queries_df.loc[queries_df["qid"]==qid]
    query = query_row["query"].tolist()[0]
    score = index_reader.compute_query_document_score(str(pid), str(query))
    scores.append(score)
    i+=1
    print(i, "pid:", pid)
query_doc["score"] = scores

query_doc.to_csv("./data/doct5/bm25_scores_male_train.tsv", sep="\t", index=False)