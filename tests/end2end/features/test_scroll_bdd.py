# SPDX-FileCopyrightText: Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pytest

# Increase test timeout to reduce flaky timeouts waiting for page/resource loads
pytestmark = pytest.mark.timeout(60)

import pytest_bdd as bdd

bdd.scenarios("scroll.feature")


@pytest.fixture(autouse=True)
def turn_on_scroll_logging(quteproc):
    quteproc.turn_on_scroll_logging(no_scroll_filtering=True)
