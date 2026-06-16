from collections import deque
from logger_module import log_event

# MEMORY MANAGER CLASS

class MemoryManager:
    """
    Simulates memory management using
    FIFO page replacement algorithm.
    """

    def __init__(self, frames):

        self.frames = frames

        self.memory = deque()

        self.page_faults = 0

        self.total_requests = 0

    # ACCESS PAGE

    def access_page(self, page):

        self.total_requests += 1

        print("\n========================================")

        print(f"Requesting Page : {page}")

        # PAGE FAULT

        if page not in self.memory:

            self.page_faults += 1

            print("Status          : PAGE FAULT")

            log_event(
                f"PAGE FAULT | "
                f"Requested Page: {page}"
            )

            # Remove oldest page if memory full
            if len(self.memory) == self.frames:

                removed_page = self.memory.popleft()

                print(f"Removed Page    : {removed_page}")

                log_event(
                    f"PAGE REMOVED | "
                    f"Removed Page: {removed_page}"
                )

            # Add new page
            self.memory.append(page)

        # PAGE HIT

        else:

            print("Status          : PAGE HIT")

            log_event(
                f"PAGE HIT | "
                f"Page: {page}"
            )

        # DISPLAY MEMORY

        print(f"Current Frames  : {list(self.memory)}")

        utilization = (
            len(self.memory) / self.frames
        ) * 100

        print(f"Memory Usage    : {utilization:.2f}%")

        print("========================================")

        # Log memory status
        log_event(
            f"MEMORY STATUS | "
            f"Frames: {list(self.memory)} | "
            f"Usage: {utilization:.2f}%"
        )

    # SHOW MEMORY STATISTICS

    def show_statistics(self):

        print("\n========================================")
        print("         MEMORY STATISTICS")
        print("========================================")

        print(f"Total Requests     : {self.total_requests}")

        print(f"Total Page Faults  : {self.page_faults}")

        fault_rate = (
            (self.page_faults / self.total_requests) * 100
            if self.total_requests > 0 else 0
        )

        print(f"Page Fault Rate    : {fault_rate:.2f}%")

        print(f"Frames Allocated   : {self.frames}")

        print("========================================")

        # Log statistics
        log_event(
            f"MEMORY STATISTICS | "
            f"Requests: {self.total_requests} | "
            f"Page Faults: {self.page_faults} | "
            f"Fault Rate: {fault_rate:.2f}%"
        )
