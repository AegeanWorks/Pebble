"""License-file identity test: the two AL-1.1 copies must never drift apart."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LICENSE = ROOT / "LICENSE"
LICENSE_TEXT = ROOT / "LICENSES" / "LicenseRef-AL-1.1.txt"


class LicenseTests(unittest.TestCase):
    """The project ships two byte-identical copies of the Aegean License 1.1."""

    def test_license_and_reuse_copy_are_identical(self) -> None:
        """REUSE metadata names the SPDX text, so any edit must land in both files."""
        self.assertTrue(LICENSE.is_file(), "LICENSE is missing")
        self.assertTrue(LICENSE_TEXT.is_file(), "LICENSES/LicenseRef-AL-1.1.txt is missing")
        self.assertEqual(
            LICENSE.read_bytes(),
            LICENSE_TEXT.read_bytes(),
            "LICENSE and LICENSES/LicenseRef-AL-1.1.txt drifted; apply the same edit to both",
        )


if __name__ == "__main__":
    unittest.main()
