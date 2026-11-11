# ERPNext SCADA Energy & ESG Carbon Accounting Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ESG](https://img.shields.io/badge/ESG-GHG%20Protocol%20Scope%201%202%203-emerald.svg)](https://ghgprotocol.org/)

Industrial IoT SCADA telemetry receiver and enterprise greenhouse gas (GHG) Scope 1, 2, and 3 ESG compliance carbon accounting engine.

## Features
- **SCADA Meter Telemetry:** Active/reactive power, power factor, and consumption telemetry.
- **GHG Scope 1, 2 & 3:** Diesel generator combustion, CEA India grid electricity, and freight logistics emission computation.
- **Carbon Cap & Credits:** Automatically computes carbon offsets and credits required to achieve net-zero targets.

## Installation & Tests
```bash
python3 -m unittest discover tests
```
