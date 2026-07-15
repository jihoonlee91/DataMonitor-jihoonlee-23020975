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

## 관련 리포지토리

개인과제 미션1(PoC 4종) + 미션2(최종 프로젝트)의 일부입니다. 여기서 검증한 상태별 집계(REJECTED 제외)/
재고 상태 분류(여유·부족·고갈) 로직은 최종 프로젝트인
[SampleOrderSystem-jihoonlee-23020975](https://github.com/jihoonlee91/SampleOrderSystem-jihoonlee-23020975)의
`app/controllers/monitoring_controller.py`로 계승되었습니다.

- [SampleOrderSystem-jihoonlee-23020975](https://github.com/jihoonlee91/SampleOrderSystem-jihoonlee-23020975) (미션2, 최종 프로젝트)
- [ConsoleMVC-jihoonlee-23020975](https://github.com/jihoonlee91/ConsoleMVC-jihoonlee-23020975) (PoC: MVC 스켈레톤)
- [DataPersistence-jihoonlee-23020975](https://github.com/jihoonlee91/DataPersistence-jihoonlee-23020975) (PoC: 데이터 영속성, 본 PoC가 조회하는 데이터의 출처)
- [DummyDataGenerator-jihoonlee-23020975](https://github.com/jihoonlee91/DummyDataGenerator-jihoonlee-23020975) (PoC: 더미 데이터 생성, 본 PoC로 조회할 데이터를 대량 생성)
