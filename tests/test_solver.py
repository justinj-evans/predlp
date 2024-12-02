from predlp.solver import pred_prob_lp
import pytest

def test_pred_prob_lp():

    # Data format
    class_names = ['label_a', 'label_b', 'label_c']
    label_counts = {'label_a': 2, 'label_b': 1, 'label_c': 1}
    pred_probs = [
        [0.6, 0.3, 0.1],
        [0.2, 0.5, 0.3],
        [0.8, 0.1, 0.1],
        [0.5, 0.1, 0.4]
    ]

    # Run through solver to assess outputs
    predlp = pred_prob_lp(class_names=class_names, label_counts=label_counts, pred_probs=pred_probs)
    assert predlp == ['label_a', 'label_b', 'label_a', 'label_c']

# Testing Locally
# if __name__ == "__main__":
#     test_pred_prob_lp()