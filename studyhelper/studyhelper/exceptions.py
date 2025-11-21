class StudyHelperError(Exception):
    pass

class ImpossibleTargetError(StudyHelperError):
    def __init__(self, target_avg: float, max_possible_avg: float):
        msg = (
            f"요청한 목표 평균 {target_avg:.2f}점은 달성할 수 없습니다. "
            f"가능한 최대 평균은 {max_possible_avg:.2f}점 입니다."
        )
        super().__init__(msg)
        self.target_avg = target_avg
        self.max_possible_avg = max_possible_avg
