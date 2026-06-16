from logger_module import log_event

# DISK SCHEDULER CLASS

class DiskScheduler:
    """
    Simulates disk scheduling algorithms.
    Currently supports SSTF scheduling.
    """

    def __init__(self, requests, initial_head):

        self.requests = requests
        self.head = initial_head

        self.total_seek_time = 0
        self.sequence = []

    # SSTF DISK SCHEDULING

    def sstf(self):

        pending_requests = self.requests.copy()

        print("\n========================================")
        print("      SSTF DISK SCHEDULING STARTED")
        print("========================================\n")

        log_event("SSTF DISK SCHEDULING STARTED")

        while pending_requests:

            # Calculate distances from current head
            distances = [
                abs(request - self.head)
                for request in pending_requests
            ]

            # Find nearest request
            nearest_index = distances.index(min(distances))

            next_request = pending_requests.pop(nearest_index)

            # Calculate seek time
            seek_time = abs(next_request - self.head)

            # Update total seek time
            self.total_seek_time += seek_time

            # Display operation
            print(f"Current Head Position : {self.head}")

            print(f"Next Disk Request     : {next_request}")

            print(f"Seek Time             : {seek_time}")

            print("----------------------------------------")

            # Log operation
            log_event(
                f"DISK ACCESS | "
                f"Current Head: {self.head} | "
                f"Next Request: {next_request} | "
                f"Seek Time: {seek_time}"
            )

            # Move disk head
            self.head = next_request

            # Save sequence
            self.sequence.append(next_request)

        # FINAL RESULTS

        average_seek = (
            self.total_seek_time / len(self.sequence)
            if self.sequence else 0
        )

        print("\n========================================")
        print("         DISK SCHEDULING RESULTS")
        print("========================================\n")

        print("Request Handling Sequence:")

        print(" -> ".join(map(str, self.sequence)))

        print(f"\nTotal Seek Time   : {self.total_seek_time}")

        print(f"Average Seek Time : {average_seek:.2f}")

        print("\n========================================")

        # Final Logs
        log_event(
            f"DISK SCHEDULING COMPLETED | "
            f"Total Seek Time: {self.total_seek_time} | "
            f"Average Seek Time: {average_seek:.2f}"
        )