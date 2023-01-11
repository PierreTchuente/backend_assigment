from __future__ import annotations

import base64
import binascii
import json
from dataclasses import dataclass


@dataclass
class Data:
    serial: str
    application: int
    Time: str
    Type: str
    device: str
    v0: int
    v1: float
    v2: float
    v3: float
    v4: float
    v5: float
    v6: float
    v7: int
    v8: float
    v9: int
    v10: float
    v11: float
    v12: float
    v13: float
    v14: float
    v15: int
    v16: int
    v17: int
    v18: float

    @property
    def get_v18(self):
        return self.v18

    @staticmethod
    def get_data_from_base64(data):
        try:
            byte_data = base64.b64decode(data)
            dict_str = byte_data.decode("UTF-8")
            dict_data = json.loads(dict_str)
            return Data(
                serial=dict_data.get("serial"),
                application=dict_data.get("application"),
                Time=dict_data.get("Time"),
                Type=dict_data.get("Type"),
                device=dict_data.get("device"),
                v0=dict_data.get("v0"),
                v1=dict_data.get("v1"),
                v2=dict_data.get("v2"),
                v3=dict_data.get("v3"),
                v4=dict_data.get("v4"),
                v5=dict_data.get("v5"),
                v6=dict_data.get("v6"),
                v7=dict_data.get("v7"),
                v8=dict_data.get("v8"),
                v9=dict_data.get("v9"),
                v10=dict_data.get("v10"),
                v11=dict_data.get("v11"),
                v12=dict_data.get("v12"),
                v13=dict_data.get("v13"),
                v14=dict_data.get("v14"),
                v15=dict_data.get("v15"),
                v16=dict_data.get("v16"),
                v17=dict_data.get("v17"),
                v18=dict_data.get("v18"),
            )
        except binascii.Error as e:
            raise e
