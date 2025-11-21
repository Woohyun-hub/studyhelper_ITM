from .exceptions import ImpossibleTargetError

def calc_average(scores):
    if not scores:
        raise ValueError("점수 리스트가 비어 있습니다.")
    return sum(scores) / len(scores)

def needed_score(target_avg, current_scores, remaining_exams=1, max_score=100):
    if remaining_exams < 1:
        raise ValueError("남은 시험 수는 1 이상이어야 합니다.")

    scores = list(current_scores)
    n_done = len(scores)
    total_exams = n_done + remaining_exams

    current_total = sum(scores)
    required_total = target_avg * total_exams
    needed_total_for_rest = required_total - current_total

    needed_each = needed_total_for_rest / remaining_exams

    if needed_each > max_score:
        max_possible_avg = (current_total + max_score * remaining_exams) / total_exams
        raise ImpossibleTargetError(target_avg, max_possible_avg)

    if needed_each < 0:
        needed_each = 0

    return needed_each
