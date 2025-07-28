"""Dobot API Python Package"""

from .api import (
    DobotApi,
    DobotApiDashboard,
    DobotApiMove,
    DobotApiFeedBack,
    MyType,
    alarmAlarmJsonFile,
)

__all__ = [
    "DobotApi",
    "DobotApiDashboard",
    "DobotApiMove",
    "DobotApiFeedBack",
    "MyType",
    "alarmAlarmJsonFile",
]

__version__ = "3.0.1"
