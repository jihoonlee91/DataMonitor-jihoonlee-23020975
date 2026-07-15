"""
DataMonitor-jihoonlee-23020975
현재 저장된 데이터(JSON) 상태를 콘솔에서 실시간으로 조회하는 관리자 도구.

사용법:
  python monitor.py --once           # 1회 조회 후 종료
  python monitor.py --interval 3     # 3초 간격으로 반복 조회 (Ctrl+C로 종료)
  python monitor.py --data-dir data  # 조회할 데이터 폴더 지정 (기본: data)
"""
import argparse
import json
import os
import time
from datetime import datetime

ORDER_STATUSES = ["RESERVED", "PRODUCING", "CONFIRMED", "RELEASE", "REJECTED"]


def load_json(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def stock_state(stock: int) -> str:
    if stock == 0:
        return "고갈"
    if stock < 100:
        return "부족"
    return "여유"


def render(data_dir: str) -> str:
    samples = load_json(os.path.join(data_dir, "samples.json"))
    orders = load_json(os.path.join(data_dir, "orders.json"))

    lines = []
    lines.append("=" * 64)
    lines.append(f" 데이터 모니터링 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 64)

    lines.append("[상태별 주문 현황]")
    status_counts = {status: 0 for status in ORDER_STATUSES}
    for order in orders:
        status_counts[order.get("status", "RESERVED")] = status_counts.get(
            order.get("status", "RESERVED"), 0
        ) + 1
    for status in ORDER_STATUSES:
        note = " (모니터링 제외)" if status == "REJECTED" else ""
        lines.append(f"  {status:<10} {status_counts.get(status, 0):>3}건{note}")

    lines.append("")
    lines.append("[시료별 재고 현황]")
    lines.append(f"  {'ID':<8}{'이름':<20}{'재고':<8}{'상태'}")
    for sample in samples:
        lines.append(
            f"  {sample['sample_id']:<8}{sample['name']:<20}"
            f"{sample['stock']:<8}{stock_state(sample['stock'])}"
        )

    lines.append("")
    lines.append("[주문 목록]")
    lines.append(f"  {'주문번호':<14}{'시료ID':<8}{'고객명':<16}{'수량':<8}{'상태'}")
    for order in orders:
        lines.append(
            f"  {order['order_id']:<14}{order['sample_id']:<8}"
            f"{order['customer']:<16}{order['quantity']:<8}{order['status']}"
        )

    return "\n".join(lines)


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    parser = argparse.ArgumentParser(description="JSON 데이터 실시간 모니터링 도구")
    parser.add_argument("--data-dir", default="data", help="모니터링할 데이터 폴더 경로")
    parser.add_argument("--interval", type=float, default=0, help="반복 조회 간격(초). 0이면 1회만 조회")
    parser.add_argument("--once", action="store_true", help="1회만 조회하고 종료")
    args = parser.parse_args()

    if args.once or args.interval <= 0:
        print(render(args.data_dir))
        return

    try:
        while True:
            clear_screen()
            print(render(args.data_dir))
            print(f"\n{args.interval}초마다 갱신 중... (Ctrl+C 로 종료)")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\n모니터링을 종료합니다.")


if __name__ == "__main__":
    main()
