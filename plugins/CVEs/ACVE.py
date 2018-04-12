from abc import ABC, abstractmethod

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class ACVE(ABC):
    """CVE abstract class inforcing structure.
    """

    @abstractmethod
    def check(self, version):
        """CVE entrypoint.
        """

        pass
