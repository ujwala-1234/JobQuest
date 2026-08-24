from file_manager import load_jobs

def show_statistics():
    jobs = load_jobs()
    if not jobs:
        print("\nNo data available.")
        return

    total = len(jobs)
    counts = {
        "Applied": 0,
        "Online Assessment": 0,
        "Interview": 0,
        "Selected": 0,
        "Rejected": 0
    }

    for job in jobs:
        status = job.get("status", "Applied")
        if status in counts:
            counts[status] += 1

    print("\n========== JOB SEARCH ANALYTICS ==========")
    print("Total Applications :", total)
    print("Applied            :", counts["Applied"])
    print("Assessments        :", counts["Online Assessment"])
    print("Interviews         :", counts["Interview"])
    print("Selected           :", counts["Selected"])
    print("Rejected           :", counts["Rejected"])
    print(f"Selection Rate     : {(counts['Selected'] / total) * 100:.2f}%")
