import subprocess
import re
from collections import Counter
from datetime import datetime

THRESHOLD = 5
failed_ips = Counter()

print("=== Linux SSH Live Incident Detector ===")
print("Monitoring SSH authentication events...")
print("Threshold:", THRESHOLD, "failed attempts")
print("Press Ctrl+C to stop.\n")

process = subprocess.Popen(
    [
        "journalctl",
        "-u", "ssh",
        "-f",
        "-n", "0",
        "--no-pager"
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1
)

try:
    for line in process.stdout:

        if "Failed password" in line:
            match = re.search(
                r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)",
                line
            )

            if match:
                ip = match.group(1)
                failed_ips[ip] += 1

                current_time = datetime.now().strftime("%H:%M:%S")

                print(
                    f"[{current_time}] "
                    f"Failed SSH login from {ip} "
                    f"| Attempts: {failed_ips[ip]}"
                )

                if failed_ips[ip] == THRESHOLD:
                    print(
                        f"🚨 INCIDENT DETECTED: "
                        f"Possible SSH brute-force attack from {ip}"
                    )

except KeyboardInterrupt:
    print("\nDetector stopped.")

finally:
    process.terminate()
