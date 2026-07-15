# CLAUDE.md

이 파일은 Claude Code가 이 리포지토리에서 작업할 때 참고하는 규칙을 담는다.

## 기술 스택

- Python 3 (표준 라이브러리만 사용, 외부 의존성 없음)

## 실행 / 테스트

```
python monitor.py --once                     # 1회 조회
python monitor.py --interval 3               # 3초 간격 실시간 갱신
python monitor.py --data-dir <path> --once   # 다른 데이터 소스 조회
```

`--data-dir`로 임의의 `samples.json`/`orders.json` 폴더를 가리킬 수 있어야 하며,
이 도구는 데이터를 생성하는 다른 PoC(DataPersistence, DummyDataGenerator)의 산출물을 그대로 읽을 수 있어야 한다.

## 데이터 스키마 가정

- `samples.json`: `sample_id`, `name`, `avg_process_time`, `yield_rate`, `stock` 필드 사용
- `orders.json`: `order_id`, `sample_id`, `customer`, `quantity`, `status` 필드 사용
- 재고 상태 임계값(여유/부족/고갈)은 이 PoC 내부 정책이며, 최종 프로젝트에서 재정의될 수 있다.
