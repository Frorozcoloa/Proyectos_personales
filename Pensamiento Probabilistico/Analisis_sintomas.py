def calc_bayes(prior_H, pro_E_dado_H, pro_E):
    return (prior_H * pro_E_dado_H) / pro_E

if __name__ == '__main__':
    prob_cancer = 1/100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    for _ in range(11):
        prob_no_cancer = 1 - prob_cancer

        prob_sintoma = (prob_cancer * prob_sintoma_dado_cancer) + (prob_no_cancer * prob_sintoma_dado_no_cancer)

        prob_cancer_dado_sintoma = calc_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)
        print(f'{prob_cancer_dado_sintoma * 100}%')
        prob_cancer = prob_cancer_dado_sintoma
