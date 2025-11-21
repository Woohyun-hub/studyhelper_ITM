import time

def study_timer(seconds):
    if seconds <= 0:
        print("0초 이하는 타이머를 시작할 수 없습니다.")
        return

    print(f"⏱ 공부 타이머 시작! (총 {seconds}초)")
    remaining = seconds

    while remaining > 0:
        print(f"남은 시간: {remaining}초", end="\r")
        time.sleep(1)
        remaining -= 1

    print("\n✅ 타이머 종료! 수고했어요 :)")
