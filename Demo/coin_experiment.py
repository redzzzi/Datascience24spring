import numpy as np
import pandas as pd

# head-tail 분포를 정의한다
coin_distribution = [0.5, 0.5]

# coin_one_experiment 함수를 정의한다
# 첫 번째 요소를 head, 두 번째 요소를 tail이라고 하자
def coin_one_experiment():
    return np.random.multinomial(n=2000, pvals=coin_distribution)

# test statistic을 수집한다
# 실험 결과를 저장하기 위해 head_counts라는 배열을 생성한다
head_counts = np.array([])

repetitions = 10000
# 실험 횟수: 10000
for i in range(repetitions):
    head_counts = np.append(head_counts, coin_one_experiment()[0])

# head_counts 배열을 DataFrame으로 변환한다
head_counts = pd.DataFrame({'Head Counts': head_counts})

# 'test statistic'이라는 열을 추가한다
head_counts['test statistic'] = abs(head_counts['Head Counts'] - 1000)

print(head_counts)
