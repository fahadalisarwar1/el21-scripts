#!/usr/bin/env python3
# Copyright 2020 Enapter, Alexander Shalin <ashalin@enapter.com>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from pymodbus.client.sync import ModbusTcpClient

ip = sys.argv[1]
PORT = 502

try:
    el21 = ModbusTcpClient(ip, PORT)
    firmware = el21.read_input_registers(0, 2, unit=1)

    if firmware.registers[0] == 17740 and firmware.registers[1] == 12849:  # check if device is EL2.1
        print("Modbus on EL2.1 found")
    else:
        print("Not EL2.1 device")

except IndexError:
    print('EL 2.1 IP address needed')

except Exception as conn_exception:
    print(conn_exception)
