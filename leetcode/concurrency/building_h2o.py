from threading import Barrier, Semaphore
from typing import Callable


class H2O:
    def __init__(self):
        self.water_barrier = Barrier(3)
        self.hydrogen_semaphore = Semaphore(2)
        self.oxygen_semaphore = Semaphore(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.hydrogen_semaphore:
            releaseHydrogen()
            self.water_barrier.wait()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.oxygen_semaphore:
            releaseOxygen()
            self.water_barrier.wait()
