# AsicLinux - Linux on Apple M-series Macs
# Copyright (C) 2026 AsicLinux Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import http

def ci_run():
    print("CI run started!")
    http.start_server()

def ci_stop():
    print("CI stop requested!")
    http.stop_server()

# if __name__ == '__main__':
#     ci_run()