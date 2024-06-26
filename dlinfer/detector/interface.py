from abc import ABC, abstractmethod
import warnings
import numpy as np


class IDetectoBackends(ABC):
    class ColorStr:
        @staticmethod
        def info(str_info: str):
            # GREEN=$(echo -en '\033[00;32m')
            return f"\033[00;32m{str_info}\033[0m"

        @staticmethod
        def error(str_info):
            # RED=$(echo -en '\033[00;31m')
            return f"\033[00;31m{str_info}\033[0m"

        @staticmethod
        def warning(str_info):
            # YELLOW=$(echo -en '\033[00;33m')
            return f"\033[00;33m{str_info}\033[0m"

    # name of inference backend, must be rewritten in subclass for checking
    NAME = "IDetectoBackends"
    # supported versions of inference backend, must be rewritten in subclass for checking version
    SUPPORTED_VERISONS = []
    # supported devices of inference backend, must be rewritten in subclass for checking device
    SUPPORTED_DEVICES = []

    def __init__(self, version: str) -> None:
        super().__init__()
        if self.NAME == "IBackend":
            warning_message = "NAME must be rewritten in subclass"
            warnings.warn(f"\033[00;33m{warning_message}\033[0m")
        if not len(self.SUPPORTED_VERISONS) > 0:
            warning_message = "SUPPORTED_VERISONS must be rewritten in subclass"
            warnings.warn(f"\033[00;33m{warning_message}\033[0m")
        if not len(self.SUPPORTED_DEVICES) > 0:
            warning_message = "SUPPORTED_DEVICES must be rewritten in subclass"
            warnings.warn(f"\033[00;33m{warning_message}\033[0m")
        self._check_version(version)

    def _check_version(self, version: str):
        """
        Check if the version of inference backend is supported
        :param version: version of inference backend
        """
        for sv in self.SUPPORTED_VERISONS:
            if version.startswith(sv):
                return
        warnings.warn(
            f"{self.NAME} version {version} is not supported, "
            f"please upgrade to support version: {self.SUPPORTED_VERISONS}"
        )

    @abstractmethod
    def load_model(self, model_path: str, verbose: bool = False) -> None:
        """
        Load model from model_path, must be rewritten in subclass
        :param model_path: path to model
        """
        raise NotImplementedError

    @abstractmethod
    def infer(self, input: np.ndarray) -> np.ndarray:
        """
        Do inference, must be rewritten in subclass
        :param input: input tensor
        :return: output tensor
        """
        raise NotImplementedError
