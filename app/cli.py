import argparse
import csv
import sys
from pathlib import Path
from tabulate import tabulate
from app.reports import REPORTS, VideoMetrics

def parse_args():
    parser = argparse.ArgumentParser(description="YouTube metrics report generator")
    parser.add_argument(
        "--files", nargs="+", required=True,
        help="Paths to CSV files with video metrics"
    )
    parser.add_argument(
        "--report", required=True,
        choices=list(REPORTS.keys()),
        help="Report type to generate"
    )
    return parser.parse_args()

def load_csv(filepath: str) -> list[VideoMetrics]:
    path = Path(filepath)
    if not path.exists():
        print(f"Error: file not found '{filepath}'", file=sys.stderr)
        sys.exit(1)
    data = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(VideoMetrics(
                title=row["title"],
                ctr=float(row["ctr"]),
                retention_rate=float(row["retention_rate"]),
            ))
    return data

def main():
    args = parse_args()
    all_videos = []
    for filepath in args.files:
        all_videos.extend(load_csv(filepath))

    report = REPORTS[args.report]
    rows = report.generate(all_videos)

    if not rows:
        print("No videos matched the criteria.")
    else:
        print(tabulate(rows, headers="keys", tablefmt="grid", floatfmt=".1f"))

if __name__ == "__main__":
    main()