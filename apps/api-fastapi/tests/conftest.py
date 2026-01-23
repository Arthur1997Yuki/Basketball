from __future__ import annotations

import sys
from pathlib import Path

# テストからアプリのモジュール（Application/ や Models/）を参照できるようにする。
APP_ROOT = Path(__file__).resolve().parents[1]
if str(APP_ROOT) not in sys.path:
    # 先頭に入れてローカルのモジュールが優先されるようにする。
    sys.path.insert(0, str(APP_ROOT))
