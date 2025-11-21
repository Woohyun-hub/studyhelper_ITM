from studyhelper import (
    calc_average,
    needed_score,
    study_timer,
    ImpossibleTargetError,
)

def demo_grade():
    print("=== 점수 평균 및 필요 점수 데모 ===")
    scores = [95, 88, 76]
    avg = calc_average(scores)
    print(f"현재 점수들: {scores}")
    print(f"현재 평균: {avg:.2f}점")

    target = 90.0
    remaining = 1

    try:
        need = needed_score(target, scores, remaining)
        print(f"목표 평균 {target}점을 위해 필요한 점수: {need:.2f}")
    except ImpossibleTargetError as e:
        print("[경고] 목표 평균 달성 불가!")
        print(e)

def demo_timer():
    print("\n=== 타이머 데모 (5초) ===")
    study_timer(5)

if __name__ == "__main__":
    demo_grade()
    demo_timer()
