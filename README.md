# DataMonitor-jihoonlee-23020975

**데이터 모니터링 Tool** PoC입니다. 현재 저장된 JSON 데이터 상태를
콘솔에서 실시간으로 조회하는 관리자 도구를 검증합니다.

## 구조

```
monitor.py     # 조회/렌더링/반복 갱신 로직
data/          # 데모용 샘플 데이터 (samples.json, orders.json)
```

## 실행

```
python monitor.py --once                       # 1회 조회
python monitor.py --interval 3                 # 3초 간격 실시간 갱신 (Ctrl+C 종료)
python monitor.py --data-dir ../DataPersistence-jihoonlee-23020975/data --once   # 다른 저장소 데이터 조회
```

상태별 주문 건수(REJECTED 제외), 시료별 재고 현황(여유/부족/고갈), 주문 목록을 표시합니다.
`--data-dir` 옵션으로 다른 PoC(DataPersistence 등)가 생성한 JSON 데이터도 그대로 조회할 수 있습니다.
