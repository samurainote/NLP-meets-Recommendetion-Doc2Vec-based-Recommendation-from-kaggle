
"""
Input: Question Title,Body,Tag
Output: Answer User

New Table 1 マッチングシート
0. Answer User id
1. Positive Answer num（回数）
2. Active_class（1,2,3,4,5, 回答回数）
3. 3ヶ月以内の回答 0 or 1
4. Answer User Score 回答者としてのユーザースコア
5. Answered questions id List in the past

New Table 2 過去回答・感情分析 （1. Positive Answer num（回数）知る）
0. Answer text id
1. Answer Text
2. Answer User id
3. Comment Yes/No
4. Comment Text (List)
5. Positive/Negative

New Table 3 過去質問
0. Question text id
1. Question Text
2. Question User id
3. Answer Yes/No
4. Answer Text (List)
5. Answer User id

y: 解答者スコア
X: 文章の類似度（Sim Score）, Positive Num, Answer Num, 直近3ヶ月解答
配分: 30, 30, 30, 10

スコア回帰（重み決められる？ 0-30に直したい）
y = w1x1 + w2x2 + w3x3 + b(0 or 10)

処理の手順
1. Input question
2. Text Processing (Title, Body, Tag)
3. Doc2vec&Cosine Sim&Top500Answers
4. スコア回帰にTop500のCossim（30スケール）と重みを設定して打ち込む
5. 回答者スコアがTopの100人を高順でアウトプット

- 3 過去質問シートの質問テキストでDoc2Vec -> Cosine Similaruty(30点満点に直す)で類似度が高い過去の質問順に高順ソート -> 回答があるものからユニーク回答者を500人上限にピックアップ
- 2 過去回答シートのAnswer User Scoreで500人のユニーク回答者を高順ソート -> Top100人に送る

"""
